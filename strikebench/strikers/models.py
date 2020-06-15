from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

from django_countries.fields import CountryField

class Striker(TimeStampedModel):

    class Role(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        PRESSING_FORWARD = "pressing forward", "Pressing Forward"
        COMPLETE_FORWARD = "complete forward", "Complete Forward"
        ADVANCED_FORWARD = "advanced forward", "Advanced Forward"
        DEEP_LYING_FORWARD = "deep lying forward", "Deep Lying Forward"
        POACHER = "poacher", "Poacher"
        TARGET_MAN = "target man", "Target Man"
        FALSE_NINE = "false nine", "False Nine"
        TREQUARTISTA = "trequartista", "Trequartista"

    name = models.CharField("Name of Striker", max_length=255)
    slug = AutoSlugField("Striker Address", unique=True, always_update=False, populate_from='name')
    description = models.TextField("Description", blank=True)
    age = models.IntegerField("Age", blank=True)
    club = models.CharField("Current Club", max_length=255)
    nationality = CountryField("Nationality", max_length=255, unique=False, null=True, blank=True)
    role = models.CharField("Role", max_length=30, choices=Role.choices, default=Role.UNSPECIFIED)

    def __str__(self):
        return self.name




