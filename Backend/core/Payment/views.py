from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json

@csrf_exempt
def khalti_ok_verify(request):
    if request.method == "POST":
        data = json.loads(request.body)
        token = data.get("token")
        amount = data.get("amount")  # Amount in paisa (e.g., 1000 = Rs. 10)
        
        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
            "token": token,
            "amount": amount
        }
        headers = {
            "Authorization": "Key YOUR_KHALTI_SECRET_KEY"
        }
        response = requests.post(url, data=payload, headers=headers)
        resp_data = response.json()
        if response.status_code == 200:
            # Payment verified successfully
            return JsonResponse({"status": "success", "data": resp_data})
        else:
            # Verification failed
            return JsonResponse({"status": "error", "data": resp_data}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
# ...existing code...