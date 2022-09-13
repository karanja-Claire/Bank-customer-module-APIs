import requests
class StockService():


    def currency(self):
        url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"

        payload = {}
        headers= {
        "apikey": "m4fcBSntFnKkgNDWU51J7JP18GQHiiii"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        result = response.text




