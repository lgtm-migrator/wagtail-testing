from factory.django import DjangoModelFactory
from faker import Factory as FakerFactory
from wagtail.models import Site

from .models import SocialMediaSettings, Tracking

faker = FakerFactory.create()


class TrackingFactory(DjangoModelFactory):
    class Meta:
        model = Tracking

    site = Site.objects.get(is_default_site=True)
    google_tag_manager_id = "GTM-123456"


class SocialMediaSettingsFactory(DjangoModelFactory):
    class Meta:
        model = SocialMediaSettings

    site = Site.objects.get(is_default_site=True)
    twitter_handle = "@wagtailtesting"
    default_sharing_text = "A site about testing Wagtail"
    site_name = "Wagtail Testing"
