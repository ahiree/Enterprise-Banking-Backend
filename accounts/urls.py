# urls.py
from django.urls import path
from .views import LoginAPIView,SendOTPAPIView,VerifyOTPAPIView

urlpatterns = [
    path('send-otp/', SendOTPAPIView.as_view()),
    path('verify-otp/', VerifyOTPAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]

