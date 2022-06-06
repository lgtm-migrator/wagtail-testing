from django.test import TestCase
from wagtail.test.utils import WagtailTestUtils


class TestSearch(TestCase, WagtailTestUtils):
    def setUp(self):
        super().setUp()

    def get(self):
        return self.client.get("/search/")

    def test_search_template(self):
        response = self.get()
        print(response)
        self.assertTemplateUsed(response, "search/search.html")
        self.assertEqual(response.render().status_code, 200)
