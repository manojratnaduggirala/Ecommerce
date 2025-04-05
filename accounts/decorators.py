from django.shortcuts import redirect
from functools import wraps
from django.core.exceptions import PermissionDenied

def role_required(role_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role and request.user.role.name == role_name:
                return view_func(request, *args, **kwargs)
            return redirect("403")
        return _wrapped_view
    return decorator
