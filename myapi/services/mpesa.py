import requests
class MpesaService:
    def auth(self):
        url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
        querystring = {"grant_type":"client_credentials"}
        payload = ""
        headers = {"Authorization": "Basic Key"}
        
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        print(response.text)