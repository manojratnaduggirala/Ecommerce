from django.shortcuts import render

def admin_dashboard(request):
    return render(request, 'adminpanel/dashboard.html')  # Ensure the template exists
