from django import forms
from .models import UserStatus

class UserStatusForm(forms.ModelForm):
    class Meta:
        model = UserStatus
        fields = ['status']
