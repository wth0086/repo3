from django.utils import timezone
from django.views.generic import ListView
from . import models


class HomeView(ListView):
    model = models.Room  # View 클래스의 속성에 대한 정보를 얻고 싶다면  ccbv.co.uk로 가보아라
    paginate_by = 10
    paginate_orphans = 4
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context
