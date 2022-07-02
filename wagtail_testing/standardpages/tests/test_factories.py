from wagtail.tests.utils import WagtailPageTests

from wagtail_testing.standardpages.factories import (
    IndexPageFactory,
    InformationPageFactory,
)


class StandrdPageFactoryTests(WagtailPageTests):
    def test_factories(self):
        InformationPageFactory()
        IndexPageFactory()
