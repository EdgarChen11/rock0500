import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup

def API(url, headers=None, body=None):
    if headers is None:
        headers = {}
    if body is None:
        body = {}

    if body:
         #如果body不是空的，requests使用post 
        response = requests.post(url, headers=headers, json=body)
    else:
         #如果body是空的，requests使用get
        response = requests.get(url, headers=headers)
    
    return response

# API串列
api_array = [

    {  
        "name": "ACE",
        "url": "https://ace.io/polarisex/oapi/v2/list/tradePrice",
        "headers": None,
        "body" : None
    },
    
    {
        "name": "MAX",
        "url": "https://max-api.maicoin.com/api/v2/tickers",
        "headers": None,
        "body" : None
    },

    {
        "name": "BITO",
        "url": "https://api.bitopro.com/v3/tickers/usdt_twd",
        "headers": None,
        "body" : None
    },
    
    {
        "name": "台灣期貨交易所",
        "url": "https://openapi.taifex.com.tw/v1/DailyForeignExchangeRates",
        "headers": None,
        "body" : None
    },

]



#從字典中取特別的值，找到USDT/TWD
def process_response(api_name, data):
    #ACE，USDT/TWD的資料結構處理
    if api_name == "ACE":
        specific_value = data.get("USDT/TWD").get("last_price")
        return specific_value
    
    if api_name == "MAX":
        specific_value = data.get("usdttwd").get("last")
        return specific_value
    
    if api_name == "BITO":
        specific_value = data.get("data").get("lastPrice")
        return specific_value

    if api_name == "台灣期貨交易所":
        latest_date = None
        latest_usd_ntd = None

        for item in data:
            date_str = item["Date"]
            if date_str:
                date = datetime.strptime(date_str, "%Y%m%d")
                if latest_date is None or date >= latest_date:
                    latest_date = date
                    latest_usd_ntd = item["USD/NTD"]

        return latest_usd_ntd

    return None


# 獲取當下時間
current_time = datetime.now()

# 格式化當下時間並印出
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"\n請求時間：{formatted_time}\n")



#處理API的資料
for api_info in api_array:
    url = api_info["url"]
    headers = api_info["headers"]
    body = api_info["body"]

    response = API(url, headers=headers, body=body)

    #判斷是否請求成功
    if response.status_code == 200:
        data = response.json()
        specific_value = process_response(api_info["name"], data) 
        formatted_specific_value = json.dumps(specific_value, indent=4, sort_keys=True)
        
        #鎖定精度
        if api_info["name"] in ["ACE","MAX","BITO"]:
            formatted_specific_value = "{:.3f}".format(float(specific_value))
            print(f"{api_info['name']} 的USDT/TWD匯率: \n{formatted_specific_value}")
        # 台灣期貨交易所
        # else:
        #     formatted_specific_value = "{:.3f}".format(float(specific_value))
        #     print(f"{api_info['name']} 的USD/TWD匯率: \n{formatted_specific_value}")

    else:
        print("API 請求失敗，HTTP 狀態碼：", response.status_code)

#台灣銀行牌告匯率網頁
url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
#定義一個變數為response，它是使用requests套件的get函式，對指定的url發起請求。
response = requests.get(url)
#將回應內容轉換為純文字
html_doc = response.text

# 使用BeautifulSoup解析HTML內容
soup = BeautifulSoup(html_doc, "html.parser")

# 找到該元素
element = soup.find("td", {"data-table": "本行即期賣出", "class": "rate-content-sight"})

# 提取出數字
number = element.text.strip()
formatted_number = "{:.3f}".format(float(number))
print(f"台灣銀行 的USD/TWD匯率:\n{formatted_number}")
