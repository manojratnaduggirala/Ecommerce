from django.shortcuts import render

def track_order(request):
    return render(request, "logistics/track_order.html")

def update_logistics(request):
    return render(request, "logistics/update_logistics.html")
