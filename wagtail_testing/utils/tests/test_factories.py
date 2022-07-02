from wagtail.tests.utils import WagtailPageTests

from wagtail_testing.utils.factories import SocialMediaSettingsFactory, TrackingFactory


class TestUtilFactories(WagtailPageTests):
    def test_factories(self):
        TrackingFactory()
        SocialMediaSettingsFactory()
