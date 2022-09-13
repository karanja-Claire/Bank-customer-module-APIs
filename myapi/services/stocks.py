import requests

from bank.settings import  APPID
class StockService():


    def currency(self,to,From,amount):
        url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={From}&amount={amount}"

        payload = {}
        headers= {
        "apikey": APPID
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        result = response.text
        print(result)
        print(status_code)
       

