from django.test import TestCase
from wagtail.models import Site

from wagtail_testing.standardpages.factories import InformationPageFactory
from wagtail_testing.utils.factories import SocialMediaSettingsFactory
from wagtail_testing.utils.templatetags import util_tags


class TestSocialTextTemplateTag(TestCase):
    def setUp(self):
        self.page = InformationPageFactory()
        self.default_site = Site.objects.get(is_default_site=True)

    def test_no_social_text(self):
        social_text = util_tags.social_text(self.page, self.default_site)
        self.assertEqual(social_text, "")

    def test_page_social_text(self):
        page = InformationPageFactory(social_text="Share this page")
        social_text = util_tags.social_text(page, self.default_site)
        self.assertEqual(social_text, "Share this page")

    def test_site_social_text(self):
        # No page.social_text attribute should fall back to
        # a site settings object `default_sharing_text`
        SocialMediaSettingsFactory(site=self.default_site)
        social_text = util_tags.social_text([], self.default_site)
        self.assertEqual(social_text, "A site about testing Wagtail")
