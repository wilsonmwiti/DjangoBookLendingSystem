from django import forms

from django.contrib.auth.models import User


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined'
        ]
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'class': 'input-box'
                    }
                ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'input-box'
                    }
                ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'input-box'
                    }
                ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'input-box'
                    }
                ),
            'date_joined': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'class': 'input-box'
                    }
                ),
        }