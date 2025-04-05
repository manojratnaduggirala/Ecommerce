# E:\E-commerce app\ecommerce\accounts\forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Role

class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating new users. Includes all required fields, plus custom fields.
    """
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone", "address", "role", "password1", "password2"]

class CustomUserChangeForm(UserChangeForm):
    """
    Form for updating existing users. Includes all fields on the user model.
    """
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone", "address", "role", "is_role_approved"]

class CustomUserEditForm(forms.ModelForm):
    """
    Form for editing existing users. Includes all fields on the user model.
    """
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone", "address", "role", "is_role_approved"]
