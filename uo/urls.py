from django.urls import path

from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("formation/<id>", views.formation, name="formation"),
    path("ue/<id>", views.ue_view, name="ue_view"),
]
