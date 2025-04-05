from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.vendor_list, name="vendor_list"),
    path("register/", views.register_vendor, name="register_vendor"),
]
