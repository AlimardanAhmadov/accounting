from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField('Name', max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class Operation(models.Model):
    related_company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    title = models.CharField('Title', max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media', default='default.png')

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title


class Card(models.Model):
    card_title = models.CharField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)
    related_operation = models.ForeignKey(Operation, on_delete=models.CASCADE, null=True, related_name='cards', verbose_name='Cards')

    class Meta:
        ordering = ['published']

    def __str__(self):
        return self.card_title


class BankCalculation(models.Model):
    related_card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, related_name='operations', verbose_name='Operations')
    time = models.DateTimeField(default=timezone.now, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    instution_title = models.CharField('Instution', max_length=200, blank=True, null=True)
    appointment = models.CharField('Appointment', max_length=150, blank=True, null=True)
    income_1 = models.PositiveIntegerField('Income_1', blank=True, null=True)
    income_2 = models.PositiveIntegerField('Income_2', blank=True, null=True)
    expense = models.PositiveIntegerField('Expense', blank=True, null=True)
    expense_1 = models.PositiveIntegerField('Expense_1', blank=True, null=True)
    expense_2 = models.PositiveIntegerField('Expense_2', blank=True, null=True)
    expense_3 = models.PositiveIntegerField('Expense_3', blank=True, null=True)
    expense_4 = models.PositiveIntegerField('Expense_4', blank=True, null=True)
    expense_5 = models.PositiveIntegerField('Expense_5', blank=True, null=True)
    expense_6 = models.PositiveIntegerField('Expense_6', blank=True, null=True)
    expense_7 = models.PositiveIntegerField('Expense_7', blank=True, null=True)
    expense_8 = models.PositiveIntegerField('Expense_8', blank=True, null=True)
    expense_9 = models.PositiveIntegerField('Expense_9', blank=True, null=True)
    expense_10 = models.PositiveIntegerField('Expense_10', blank=True, null=True)
    expense_11 = models.PositiveIntegerField('Expense_11', blank=True, null=True)
    expense_12 = models.PositiveIntegerField('Expense_12', blank=True, null=True)

    class Meta:
        ordering = ['time']


    def __str__(self):
        return self.instution_title       


class BankCalculationHeaders(models.Model):
    related_bank_operation = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    num1 = models.CharField('Num1', max_length=20)
    num2 = models.PositiveIntegerField('Num2', blank=True, null=True)
    num3 = models.PositiveIntegerField('Num3', blank=True, null=True)
    num4 = models.PositiveIntegerField('Num4', blank=True, null=True)
    num5 = models.PositiveIntegerField('Num5', blank=True, null=True)
    num6 = models.PositiveIntegerField('Num6', blank=True, null=True)
    num7 = models.PositiveIntegerField('Num7', blank=True, null=True)
    num8 = models.PositiveIntegerField('Num8', blank=True, null=True)
    num9 = models.PositiveIntegerField('Num9', blank=True, null=True)
    num10 = models.PositiveIntegerField('Num10', blank=True, null=True)
    num11 = models.PositiveIntegerField('Num11', blank=True, null=True)
    num12 = models.PositiveIntegerField('Num12', blank=True, null=True)
    num13 = models.PositiveIntegerField('Num13', blank=True, null=True)
    num14 = models.PositiveIntegerField('Num14', blank=True, null=True)
    num14 = models.PositiveIntegerField('Num15', blank=True, null=True)