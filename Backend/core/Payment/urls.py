from django.urls import path
from .views import (
    KhaltiBankListView,
    KhaltiEpaymentInitiateView,
    KhaltiEpaymentLookupView,
)

urlpatterns = [
    path('khalti/banks/', KhaltiBankListView.as_view(), name='khalti_bank_list'),
    path('khalti/epayment/initiate/', KhaltiEpaymentInitiateView.as_view(), name='khalti_epayment_initiate'),
    path('khalti/epayment/lookup/', KhaltiEpaymentLookupView.as_view(), name='khalti_epayment_lookup'),
]