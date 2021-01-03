import json

from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import get_object_or_404, render,redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, viewsets, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from django.db.models import FloatField, Sum
from django.db.models.functions import Cast

from .forms import BankCalculationForm, BankCalculationHeadersForm, AddCompanyForm, CreateNewOperationForm, CreateMonthlyOperationForm
from .models import BankCalculation, Card, Company, Operation, BankCalculationHeaders
from .serializers import (BankCalculationSerializer, CardSerializer, CompanySerializer, OperationSerializer, BankCalculationHeadersSerializer)



class CompanyList(APIView):
    serializer_class = CompanySerializer
    template_name = 'companies.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        print(serializer.data)
        return Response({'data': queryset, 'serializer': serializer})


    def post(self, request):
        if request.method == 'POST':
            form = AddCompanyForm(request.POST or None)
            if form.is_valid():
                instance = form.save()
                instance.save()
                redirect('home')
        else:
            form = AddCompanyForm()
        return Response({'form': form})    



class OperationList(APIView):
    serializer_class = OperationSerializer
    template_name = 'operations_template.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get_object(self, pk):
        try:
            return Company.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk):
        related_company = self.get_object(pk)
        operations = Operation.objects.filter(related_company=related_company)
        serializer = OperationSerializer(operations, many=True)
        print(serializer.data)
        return Response({'operations': operations, 'related_company': related_company, 'serializer': serializer}) 


    def post(self, request, pk):
        related_company = self.get_object(pk)
        
        if request.method == 'POST':
            form = CreateNewOperationForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.related_company = related_company
                instance.save()
        else:
            form = CreateNewOperationForm()
        return Response({'form': form, 'related_company': related_company})    


class CardList(APIView):
    serializer_class = CardSerializer
    template_name = 'cards.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get_object(self, pk):
        try:
            return Operation.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk):
        related_operation = self.get_object(pk)
        cards = Card.objects.filter(related_operation=related_operation)
        print(cards)
        return Response({'related_operation': related_operation, 'cards': cards})

    def post(self, request, pk):
        related_operation = self.get_object(pk)
        
        if request.method == 'POST':
            form = CreateMonthlyOperationForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.related_operation = related_operation
                instance.save()
        else:
            form = CreateMonthlyOperationForm()
        return Response({'form': form, 'related_operation': related_operation})    


class CreateFormView(APIView):
    """Create Table"""

    serializer_class = BankCalculationSerializer
    template_name = 'table.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get_object(self, pk):
        try:
            return Card.objects.get(id=pk)
        except:
            raise Http404


    def get(self, request, pk, format=None):
        related_card = self.get_object(pk)
        details = BankCalculation.objects.filter(related_card=related_card)
        all_sum = details.annotate(as_float=Cast('income_1', FloatField())).aggregate(sum=Sum('as_float'))['sum']
        serializer = BankCalculationSerializer(details, many=True)
        print(details)
        print(all_sum)
        return Response({'related_card': related_card, 'details': details, 'serializer': serializer, 'all_sum': all_sum})
    

    def post(self, request, pk):
        related_card = self.get_object(pk)

        if request.method == 'POST':
            form = BankCalculationForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.related_card = related_card
                instance.save()
        else:
            form = BankCalculationForm()
        return Response({'form': form, 'related_card': related_card})
 

class UpdateView(APIView):

    """Update Details"""

    serializer_class = BankCalculationSerializer

    def get_object(self, pk):
        try:
            return BankCalculation.objects.get(pk=pk)
        except BankCalculation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        selected_details = self.get_object(pk)
        serializer = BankCalculationSerializer(selected_details)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        selected_details = self.get_object(pk)
        serializer = BankCalculationSerializer(selected_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        selected_details = self.get_object(pk)
        selected_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(["DELETE", "GET"])
def delete_detail(request, pk):
    details = get_object_or_404(BankCalculation, id=pk)
    details.save()
    return JsonResponse({"message": "Deleted successfully!"})



class HeadersView(APIView):
    """Add Header Numbers To Table"""

    serializer_class = BankCalculationHeadersSerializer

    def get_object(self, pk):
        try:
            return Card.objects.get(id=pk)
        except:
            raise Http404


    def get(self, request, pk, format=None):
        related_bank_operation = self.get_object(pk)
        serializer = BankCalculationHeadersSerializer(related_bank_operation)
        print(headers)
        return Response(serializer.data)
    

    def post(self, request, pk):
        related_bank_operation = self.get_object(pk)

        if request.method == 'POST':
            form = BankCalculationHeadersForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.related_bank_operation = related_bank_operation
                instance.save()
        else:
            form = BankCalculationForm()
        return Response({'form': form, 'related_bank_operation': related_bank_operation})
        


class UpdateHeadersView(APIView):
    """Update Header"""

    serializer_class = BankCalculationHeadersSerializer

    def get_object(self, pk):
        try:
            return BankCalculationHeaders.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        selected_headers = self.get_object(pk)
        serializer = BankCalculationHeadersSerializer(selected_headers)
        print(serializer.data)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        selected_headers = self.get_object(pk)
        serializer = BankCalculationHeadersSerializer(selected_headers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


