from django import forms

import datetime

from .models import Loan


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = [
            'returning_date',
            ]
        widgets = {
            'returning_date': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
