from django import forms
from .models import BankCalculation, BankCalculationHeaders


class BankCalculationForm(forms.ModelForm):
    class Meta:
        model = BankCalculation
        
        fields = [
            'instution_title', 'time', 'appointment', 'income_1', 'income_2', 'expense', 'expense_1', 'expense_2', 'expense_3', 'expense_4', 'expense_5', 'expense_6', 'expense_7', 'expense_8', 'expense_9', 'expense_10', 'expense_11', 'expense_12'
        ]



class BankCalculationHeadersForm(forms.ModelForm):
    class Meta:
        model = BankCalculationHeaders

        fields = (
            'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num8', 'num9', 'num10', 'num11', 'num12', 'num13', 'num14',
        )