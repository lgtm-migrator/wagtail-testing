from django.test import TestCase
from django.urls import reverse
from wagtail.models import Page, Site
from wagtail.test.utils import WagtailTestUtils
from wagtail.test.utils.form_data import inline_formset, nested_form_data
from wagtail.tests.utils import WagtailPageTests

from wagtail_testing.home.factories import HomePageFactory
from wagtail_testing.home.models import HomePage
from wagtail_testing.standardpages.factories import InformationPageFactory
from wagtail_testing.standardpages.models import IndexPage, InformationPage
from wagtail_testing.utils.models import PageRelatedPage


class TestInformationPage(WagtailPageTests):
    def test_can_create_index_page_under_home_page(self):
        self.assertCanCreateAt(HomePage, IndexPage)

    def test_can_create_information_page_under_index_page(self):
        self.assertCanCreateAt(IndexPage, InformationPage)

    def test_related_pages(self):
        p1 = InformationPageFactory()
        p2 = InformationPageFactory()
        p3 = InformationPageFactory()
        p4 = InformationPageFactory()

        info_page = InformationPageFactory()
        info_page.page_related_pages = [
            PageRelatedPage(page=p1, sort_order=0),
            PageRelatedPage(page=p2, sort_order=3),
            PageRelatedPage(page=p3, sort_order=1),
            PageRelatedPage(page=p4, sort_order=2),
        ]
        info_page.save()
        info_page.refresh_from_db()

        self.assertEqual(list(info_page.related_pages), [p1, p3, p4, p2])


class TestInformationPageCreation(TestCase, WagtailTestUtils):
    def setUp(self):
        super().setUp()
        self.home_page = HomePageFactory()
        self.superuser = self.create_superuser(
            "superuser", "superuser@example.com", "password"
        )
        self.client.force_login(self.superuser)

        # As a tip to get the post data needed here, add a page via the browser,
        # open console and inspect the post request data when you publish the page.
        self.post_data = nested_form_data(
            {
                "title": "Information Page",
                "slug": "information_page",
                "introduction": "Example introduction for information page",
                "page_related_pages": inline_formset([]),
                "body-count": 1,
                "body-0-deleted": "",
                "body-0-order": 0,
                "body-0-type": "heading",
                "body-0-value": "A heading block",
            }
        )

    def _post(self, post_data):
        return self.client.post(
            reverse(
                "wagtailadmin_pages:add",
                # app, model, parent
                args=("standardpages", "informationpage", self.home_page.id),
            ),
            post_data,
        )

    def test_can_create_standard_content_page(self):
        self._post(self.post_data)
        page = Page.objects.get(slug="information_page")
        self.assertTrue(page)


class TestInformationPageRendering(TestCase, WagtailTestUtils):
    """Test template rendering"""

    def setUp(self):
        super().setUp()
        self.root_page = Page.objects.first()

        self.home_page = HomePageFactory()
        self.default_site = Site.objects.get(is_default_site=True)
        self.default_site.root_page_id = self.home_page.id
        self.default_site.save()
        self.superuser = self.create_superuser(
            "superuser", "superuser@example.com", "password"
        )
        self.client.force_login(self.superuser)
        self.information_page = InformationPage(
            title="Information page render title",
            slug="information_page_render",
            introduction="Information page introduction",
            page_related_pages=[],
            body=[
                ("heading", "Test heading 2"),
            ],
        )
        self.home_page.add_child(instance=self.information_page)

    def get(self):
        return self.client.get(self.information_page.url)

    def test_response(self):
        response = self.get()
        self.assertEqual(response.render().status_code, 200)

    def test_information_page_template(self):
        response = self.get()
        self.assertTemplateUsed(response, "standardpages/information_page.html")
        # Also check the streamfield template was used
        self.assertTemplateUsed(response, "streamfield/blocks/heading_block.html")
        self.assertTemplateUsed(response, "streamfield/stream_block.html")

    def test_information_page_rendered_values(self):
        response = self.get()
        self.assertContains(response, "Information page render title")
        self.assertContains(response, "Information page introduction")
        self.assertNotContains(response, "Some value that we know shouldn't be there")


# set up InformationPageIndex and add
# test related_pages stuff
# test form valid in admin
