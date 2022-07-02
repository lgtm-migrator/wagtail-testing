import factory
import wagtail_factories

from .models import HomePage


class HomePageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = HomePage

    title = factory.Faker("text", max_nb_chars=25)
