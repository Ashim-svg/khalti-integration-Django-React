from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

KHALTI_SECRET_KEY = "59fc9e58316142ec81decf458444fdec"




class KhaltiOKVerifyView(APIView):
    def post(self, request):
        token = request.data.get("token")
        amount = request.data.get("amount")
        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
            "token": token,
            "amount": amount
        }
        headers = {
            "Authorization": f"Key {KHALTI_SECRET_KEY}"
        }
        response = requests.post(url, data=payload, headers=headers)
        resp_data = response.json()
        if response.status_code == 200:
            return Response({"status": "success", "data": resp_data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": resp_data}, status=status.HTTP_400_BAD_REQUEST)

class KhaltiEpaymentInitiateView(APIView):
    def post(self, request):
        url = "https://khalti.com/api/v2/epayment/initiate/"
        headers = {
            "Authorization": f"Key {KHALTI_SECRET_KEY}",
            "Content-Type": "application/json"
        }
        payload = request.data
        response = requests.post(url, json=payload, headers=headers)
        resp_data = response.json()
        if response.status_code == 200:
            return Response({"status": "success", "data": resp_data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": resp_data}, status=status.HTTP_400_BAD_REQUEST)

class KhaltiEpaymentLookupView(APIView):
    def post(self, request):
        url = "https://khalti.com/api/v2/epayment/lookup/"
        headers = {
            "Authorization": f"Key {KHALTI_SECRET_KEY}",
            "Content-Type": "application/json"
        }
        payload = request.data
        response = requests.post(url, json=payload, headers=headers)
        resp_data = response.json()
        if response.status_code == 200:
            return Response({"status": "success", "data": resp_data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": resp_data}, status=status.HTTP_400_BAD_REQUEST)