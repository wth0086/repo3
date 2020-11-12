from django.urls import path
from rooms import views as room_views

app_name = "core"  # 이건 config에 있는 urls.py의 namespace와 이름이 같아야한다.

urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
