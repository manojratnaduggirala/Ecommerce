from django.urls import path
from .views import create_order, order_list, order_detail, update_order, delete_order

urlpatterns = [
    path("", order_list, name="order_list"),
    path("<int:order_id>/", order_detail, name="order_detail"),
    path("create/", create_order, name="create_order"),
    path("update/<int:order_id>/", update_order, name="update_order"),
    path("delete/<int:order_id>/", delete_order, name="delete_order"),
]
