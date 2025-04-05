from django.shortcuts import render
from django.http import JsonResponse

def payment_home(request):
    return render(request, "payments/payment_home.html")  # Ensure template exists

def process_payment(request):
    return JsonResponse({"message": "Payment processed successfully!"})

def payment_history(request):
    return JsonResponse({"message": "Payment history retrieved successfully!"})
