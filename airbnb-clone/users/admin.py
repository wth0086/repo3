from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# 아래의 데코레이션은 admin.site.register(models.User, CustomUserAdmin) 과 같다.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avator",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    # 지난 시간에 했던 예제 admin.ModelAdmin을 상속받아 진행했었다.
    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = (
    #     "language",
    #     "superhost",
    # )
