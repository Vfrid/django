from django.urls import path
from . import views

# app_name = "render"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("patient_list", views.patient_list, name="patient_list"),
    path("add_patient", views.add_patient, name="add_patient"),
    # path("add_vital", views.add_vital, name="add_vital"),
    path("update_patient/<patient_id>", views.update_patient, name="update_patient"),
]