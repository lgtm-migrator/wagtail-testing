from wagtail.tests.utils import WagtailPageTests

from wagtail_testing.home.factories import HomePageFactory


class HomePageFactoryTests(WagtailPageTests):
    def test_factories(self):
        HomePageFactory()
