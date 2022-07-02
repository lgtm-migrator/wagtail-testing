from django.test import TestCase
from django.test.client import RequestFactory

from wagtail_testing.utils import views as util_views


class TestUtilViews(TestCase):
    def test_page_not_found(self):
        r = RequestFactory()
        get_request = r.get("/should404/")
        response = util_views.page_not_found(request=get_request, exception=[])
        self.assertEqual(response.status_code, 404)

    def test_server_error(self):
        r = RequestFactory()
        get_request = r.get("/should500/")
        response = util_views.server_error(request=get_request)
        self.assertEqual(response.status_code, 500)
