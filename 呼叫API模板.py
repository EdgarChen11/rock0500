import requests
import json

url = "https://api.bitopro.com/v3/tickers/usdt_twd"

response = requests.get(url)


headers:{
    "Authorization": "Bearer token",
}

body:{
    "key": "value", 
}



if response.status_code == 200:
    data2 = response.json()
    formatted_data = json.dumps(data2, indent=4, sort_keys=True)
    print(formatted_data)
else:
    print(f"無法執行，狀態碼:, {response.status_code}")