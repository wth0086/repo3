from django.urls import path
from . import views

app_name = "employees"

urlpatterns = [
    path("reg/", views.regEmployee, name="reg"),
    path("regCon/", views.regConEmployee, name="regCon"),
    path("emAll/", views.readEmployeeAll, name="emAll"),
    path("<str:ID>/info/", views.Employeeinfo, name="information"),
    path("<str:ID>/mod/", views.readEmployeeOne, name="Modify"),
    path("modCon/", views.modConEmployee, name="modCon"),
    path("<str:ID>/del/", views.delConEmployee, name="Delete"),
]