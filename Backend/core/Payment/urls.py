# urls.py
from django.urls import path
from .views import khalti_ok_verify

urlpatterns = [
    path('khalti/verify/', khalti_ok_verify, name='khalti_ok_verify'),
]