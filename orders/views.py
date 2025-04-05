from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Order
from customers.models import Customer
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def order_list(request):
    """List all orders for the logged-in customer"""
    orders = Order.objects.filter(customer__user=request.user).order_by('-order_date')
    return render(request, "orders/order_list.html", {"orders": orders})

@login_required
def order_detail(request, order_id):
    """View details of a specific order"""
    order = get_object_or_404(Order, id=order_id, customer__user=request.user)
    return render(request, "orders/order_detail.html", {"order": order})

@login_required
@csrf_exempt
def create_order(request):
    """Create a new order"""
    if request.method == "POST":
        customer = get_object_or_404(Customer, user=request.user)
        total_price = 100.00  # Example fixed price; modify this dynamically

        order = Order.objects.create(customer=customer, total_price=total_price)
        return JsonResponse({"order_id": order.id, "message": "Order created successfully!"})
    
    return render(request, "orders/create_order.html")

@login_required
@csrf_exempt
def update_order(request, order_id):
    """Update the status of an order"""
    order = get_object_or_404(Order, id=order_id, customer__user=request.user)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            order.status = data.get("status", order.status)
            order.save()
            return JsonResponse({"message": "Order updated successfully!"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@login_required
@csrf_exempt
def delete_order(request, order_id):
    """Delete an order"""
    order = get_object_or_404(Order, id=order_id, customer__user=request.user)
    
    if request.method == "POST":
        order.delete()
        return JsonResponse({"message": "Order deleted successfully!"})
    
    return JsonResponse({"error": "Invalid request method"}, status=405)
