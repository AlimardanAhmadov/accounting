from django.urls import path
from knox import views as knox_views
from . import views


urlpatterns = [
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logoutall/', views.LogoutAllView.as_view(), name='logoutall'),
    path('api/user/', views.UserAPI.as_view(), name='user'),
    path('api/şifrənidəyişmək/<int:pk>/', views.ChangePasswordView.as_view(), name='changepassword'),
    path('api/updateprofile/<int:pk>/', views.UpdateProfileView.as_view(), name='updateprofile'),
]