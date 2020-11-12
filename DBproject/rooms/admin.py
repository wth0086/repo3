from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.BedType, models.Amenity)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    filedsets = (
        (
            "fields",
            {
                "fields": (
                    "room_number",
                    "room_type",
                    "bed_type",
                    "amenities",
                    "room_state",
                )
            },
        ),
    )

    list_display = (
        "room_number",
        "room_type",
        "bed_type",
        "room_state",
    )

    filter_horizontal = ("amenities",)