from django.urls import path
from .views import (
    KhaltiOKVerifyView,
    KhaltiEpaymentInitiateView,
    KhaltiEpaymentLookupView,
)

urlpatterns = [
    path('khalti/verify/', KhaltiOKVerifyView.as_view(), name='khalti_ok_verify'),
    path('khalti/epayment/initiate/', KhaltiEpaymentInitiateView.as_view(), name='khalti_epayment_initiate'),
    path('khalti/epayment/lookup/', KhaltiEpaymentLookupView.as_view(), name='khalti_epayment_lookup'),
    
]