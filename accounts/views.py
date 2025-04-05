from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from .decorators import role_required
from .forms import CustomUserEditForm, CustomUserCreationForm, CustomUserChangeForm

# Login view
def user_login(request):
    if request.user.is_authenticated:
        return redirect_dashboard(request.user)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the user has a role
            if not user.role:
                messages.error(request, "Your account does not have a role assigned. Please contact support.")
                return redirect("login") 

            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect_dashboard(user)
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")

# Helper function to redirect users based on their role
def redirect_dashboard(user):
    role_redirects = {
        "Admin": "admin_dashboard",
        "Vendor": "vendor_dashboard",
        "Customer": "customer_dashboard",
    }
    return redirect(role_redirects.get(getattr(user.role, "name", "Customer"), "customer_dashboard"))

# Admin dashboard
@login_required
@role_required("Admin")
def admin_dashboard(request):
    users = CustomUser.objects.all()  # Fetch all users
    return render(request, "accounts/admin_dashboard.html", {"users": users})

# Vendor dashboard
@login_required
@role_required("Vendor")
def vendor_dashboard(request):
    return render(request, "accounts/vendor_dashboard.html")

# Customer dashboard
@login_required
@role_required("Customer")
def customer_dashboard(request):
    return render(request, "accounts/customer_dashboard.html")

# Order list view
@login_required
@role_required("Customer")  # Restrict orders to customers
def order_list(request):
    return render(request, 'accounts/order_list.html')

# Logout view
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("login")

# Custom error views
def custom_permission_denied(request, exception=None):
    return render(request, "accounts/403.html", status=403)

def page_403(request):
    return render(request, 'accounts/403.html')

def page_404(request, exception=None):
    return render(request, 'accounts/404.html', status=404)

# Home view
def home(request):
    return render(request, 'home.html')

# Approve User
@login_required
@role_required("Admin")
def approve_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if user.is_role_approved:  # If already approved, don't do it again
        messages.info(request, f"{user.username} is already approved.")
        return redirect("admin_dashboard")

    user.is_role_approved = True  # Approve the user
    user.save(update_fields=["is_role_approved"])  # Save only this field

    messages.success(request, f"{user.username} has been approved successfully!")
    return redirect("admin_dashboard")

# Remove User
@login_required
@role_required("Admin")
def remove_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, f"User {user.username} has been removed.")
    return redirect("admin_dashboard")

# Edit User
@login_required
@role_required("Admin")
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        form = CustomUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f"{user.username}'s information has been updated.")
            return redirect("admin_dashboard")
    else:
        form = CustomUserEditForm(instance=user)

    return render(request, "accounts/edit_user.html", {"form": form, "user": user})

# Add User
@login_required
@role_required("Admin")
def add_user_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Additional processing if needed
            user.save()
            return redirect('admin_dashboard')  # Redirect to the admin dashboard or appropriate page
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/add_user.html', {'form': form})
