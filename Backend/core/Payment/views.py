from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

KHALTI_SECRET_KEY = "59fc9e58316142ec81decf458444fdec"

class KhaltiBankListView(APIView):
    def get(self, request):
        payment_type = request.GET.get("payment_type", "ebanking")
        url = f"https://khalti.com/api/v5/bank/?payment_type={payment_type}"
        response = requests.get(url)
        return Response(response.json(), status=response.status_code)

class KhaltiEpaymentInitiateView(APIView):
    def post(self, request):
        url = "https://khalti.com/api/v2/epayment/initiate/"
        headers = {
            "Authorization": f"Key {KHALTI_SECRET_KEY}",
            "Content-Type": "application/json"
        }
        payload = request.data
        response = requests.post(url, json=payload, headers=headers)
        return Response(response.json(), status=response.status_code)

class KhaltiEpaymentLookupView(APIView):
    def post(self, request):
        url = "https://khalti.com/api/v2/epayment/lookup/"
        headers = {
            "Authorization": f"Key {KHALTI_SECRET_KEY}",
            "Content-Type": "application/json"
        }
        payload = request.data
        response = requests.post(url, json=payload, headers=headers)
        return Response(response.json(), status=response.status_code)