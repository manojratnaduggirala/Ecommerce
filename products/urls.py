from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path("", views.product_list, name="product_list"),  # Sample route
]
