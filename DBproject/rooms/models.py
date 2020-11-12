from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class BedType(AbstractItem):
    class Meta:
        verbose_name = "Bed Type"
        ordering = ["name"]


class Amenity(AbstractItem):

    """ Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Room(core_models.TimeStampedModel):
    room_number = models.CharField(max_length=5)
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    bed_type = models.ForeignKey(
        BedType, related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    room_state = models.BooleanField(default=True)
