from invoke import run as local
from invoke.tasks import task


@task
def cover(c):
    return local(
        "coverage erase && coverage run manage.py test --settings=wagtail_testing.settings.test && coverage report"
    )
