from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('vendor-dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('orders/', views.order_list, name='order_list'),
    path('403/', views.page_403, name='403'),
    path('', views.home, name='home'),
    # path('403/', views.page_403, name='403'),
    path('404/', views.page_404, name='404'),
 
   
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/approve/<int:user_id>/', views.approve_user, name='approve_user'),
    path('admin/remove/<int:user_id>/', views.remove_user, name='remove_user'),
    path('admin/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('add-user/', views.add_user_view, name='add_user'),
    # path('add-user/', add_user_view, name='add_user'),
]




