from django.shortcuts import redirect

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.path.startswith("/accounts/admin-dashboard/") and not request.user.is_admin():
                return redirect("403")
            if request.path.startswith("/accounts/vendor-dashboard/") and not request.user.is_vendor():
                return redirect("403")
            if request.path.startswith("/accounts/customer-dashboard/") and not request.user.is_customer():
                return redirect("403")
        return self.get_response(request)
