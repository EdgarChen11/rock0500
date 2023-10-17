import requests
import json

url = "https://api.bitopro.com/v3/tickers/usdt_twd"

headers = {
    "Authorization": "Bearer token",
}

data = {
    "key": "value", 
}



response = requests.post(url, data=data, headers=headers)

if response.status_code == 200:
    data = response.json()
    formatted_data = json.dumps(data, indent=4, sort_keys=True)
    message = formatted_data.encode("UTF-8").decode('unicode_escape')
    print(message)
else:
    print(f"無法執行，狀態碼:, {response.status_code}")
