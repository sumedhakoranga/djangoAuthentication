from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('email-check/', views.email_check, name='email_check'),
    path('verify-email/<str:token>/', views.verify_email, name='verify_email'),
    path('', RedirectView.as_view(pattern_name='register', permanent=False)),
]
