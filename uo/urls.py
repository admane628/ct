from django.urls import path

from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("formation/<id>", views.formation, name="formation"),
    path("formations/", views.formations, name="formations"),
    path("ue/<id>", views.ue_view, name="ue_view"),
    path("ues/", views.ues, name="ues"),


    path("exclusive/", views.exclusive, name="exclusive"), #q20)
]
