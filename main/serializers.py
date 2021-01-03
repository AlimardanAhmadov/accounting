from rest_framework import serializers
from .models import Company, Operation, BankCalculation, Card, BankCalculationHeaders


class CompanySerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Company
        fields = (
            'created', 'name'
        )


class OperationSerializer(serializers.ModelSerializer):
    related_company = CompanySerializer
    created_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Operation
        fields = (
            'related_company', 'title', 'created_date', 'image'
        )


    def create(self, validated_data):
        company = validated_data.pop('related_company')
        company_instance, created = Company.objects.get_or_create(name=company)
        operation_instance = Operation.objects.create(**validated_data, related_company=company_instance)
        return operation_instance



class CardSerializer(serializers.ModelSerializer):
    related_operation = OperationSerializer
    published = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Card
        fields = (
            'related_operation', 'published', 'card_title'
        )

    def create(self, validated_data):
        card = validated_data.pop('related_operation')
        operation_instance, created = Operation.objects.get_or_create(title=card)
        card_instance = Card.objects.create(**validated_data, related_operation=operation_instance)
        return card_instance
    


class BankCalculationSerializer(serializers.ModelSerializer):
    related_card = CardSerializer(read_only=True)

    class Meta:
        model = BankCalculation

        fields = (
            'related_card', 'time', 'id', 'instution_title', 'appointment', 'income_1', 'income_2', 'expense', 'expense_1', 'expense_2', 'expense_3', 'expense_4', 'expense_5', 'expense_6', 'expense_7', 'expense_8', 'expense_9', 'expense_10', 'expense_11', 'expense_12' 
        )

    def create(self, validated_data):
        related_card = validated_data.pop('related_card')
        card_instance, created = Card.objects.get_or_create(card_title=related_card)
        bank_instance = BankCalculation.objects.create(**validated_data, related_card=card_instance)
        return bank_instance



class BankCalculationHeadersSerializer(serializers.ModelSerializer):
    related_bank_operation = CardSerializer

    class Meta:
        model = BankCalculationHeaders

        fields = (
            'related_bank_operation', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num8', 'num9', 'num10', 'num11', 'num12', 'num13', 'num14',
        )

    def create(self, validated_data):
        related_bank_operation = validated_data.pop('related_bank_operation')
        card_instance, created = Card.objects.get_or_create(card_title=related_bank_operation)
        header_instance = BankCalculationHeaders.objects.create(**validated_data, related_bank_operation=card_instance)
        return header_instance