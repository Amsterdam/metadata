import factory
from factory import fuzzy

from .. import models


class MetaDataFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.MetaData

    id = fuzzy.FuzzyText(length=40)
    title = fuzzy.FuzzyText(length=100)
