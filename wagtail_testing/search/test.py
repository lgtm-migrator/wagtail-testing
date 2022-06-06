from django.core.paginator import Page
from django.test import TestCase
from django.test.client import RequestFactory
from wagtail.test.utils import WagtailTestUtils

from wagtail_testing.search.views import search as search_view


class TestSearch(TestCase, WagtailTestUtils):
    def setUp(self):
        super().setUp()

    def get(self, query=None):
        return self.client.get(f"/search/?query={query}")

    def test_search_template(self):
        response = self.get()
        self.assertTemplateUsed(response, "search/search.html")
        self.assertEqual(response.render().status_code, 200)

    def test_search_query_no_results(self):
        response = self.get(query="home")
        self.assertContains(response, "No results found")

    def test_view_search_query(self):
        r = RequestFactory().get("/search/", {"query": "about"})
        search = search_view(request=r)
        self.assertEqual(search.context_data["search_query"], "about")
        self.assertTrue(isinstance(search.context_data["search_results"], Page))
