from django.urls import path
from . import views

urlpatterns = [
    path("track/", views.track_order, name="track_order"),
    path("update/", views.update_logistics, name="update_logistics"),
]

