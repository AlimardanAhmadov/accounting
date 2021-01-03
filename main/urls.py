from django.conf.urls import include
from rest_framework import routers
from . import views
from django.urls import path


router = routers.DefaultRouter()
router.register('companies/', views.CompanyViewSet, basename='Company')
router.register('operations/', views.OperationViewSet, basename='Operation')
router.register('cards/', views.CardViewSet, basename='Card')
router.register('bank_headers/', views.BankCalculationHeadersViewSet, basename='Headers'),


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.CompanyList.as_view(), name='home'),
    path('əməliyyat/<str:pk>/', views.OperationList.as_view(), name='operations'),
    path('əməliyyat/siyahı/<str:pk>/', views.CardList.as_view(), name='card_list'),
    path('bank_əməliyyatı/<str:pk>/', views.CreateFormView.as_view(template_name='table.html'), name='chosen_operation'),
    path('yenilə/<str:pk>/', views.UpdateView.as_view(), name="api_update_view"),
    path('delete_detail/<str:pk>/', views.delete_detail, name="delete_detail"),
    path('add_headers/<str:pk>/', views.HeadersView.as_view(), name='add_headers'),
    path('update_headers/<str:pk>/', views.UpdateHeadersView.as_view(), name='update_headers'),
]