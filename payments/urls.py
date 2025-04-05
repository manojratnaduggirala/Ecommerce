from django.urls import path
from . import views

urlpatterns = [
    path("", views.payment_home, name="payment_home"),
    path("process/", views.process_payment, name="process_payment"),
    path("history/", views.payment_history, name="payment_history"),
]
