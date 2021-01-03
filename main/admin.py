from django.contrib import admin
from .models import Company, Operation, BankCalculation, Card, BankCalculationHeaders


admin.site.register(Company)
admin.site.register(Operation)
admin.site.register(BankCalculation)
admin.site.register(Card)
admin.site.register(BankCalculationHeaders)