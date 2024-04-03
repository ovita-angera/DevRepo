import requests

API_KEY = 'fca_live_GOA1oKPh5ZRo2qhRL58ud2lsMcNx8KT1WB7bPzm6'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    
    try:
        # whenever you send a request, you get a response
        response = requests.get(url)
        
        # it will be a json file
        data = response.json()
        return data["data"]

    except:
        print("Invalid Currency")
        return None
   
while True:
    # prompt the user for input
    base = input("Enter the base currency or q to quit the program: ").upper()
    
    # check base
    if base == "Q":
        break
    
    data = convert_currency(base)
    if not data:
        continue
    
    del data[base]
    # use a for loop together with dictionary synctactic sugar
    for ticker, value in data.items():
        print(f"{ticker}: {value}")