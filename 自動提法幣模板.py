print("測試開始")
#導入套件
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from datetime import datetime
#顯性等待​
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

###

#版本：0.0.1，既有帳號並已綁定GA，自動化登入
#版本：0.0.2，帳號登入成功，並跳轉到資產管理
#版本：0.0.3，帳號登入成功，並跳轉到資產管理，自動法幣提款
#版本：0.0.4，帳號登入成功，並跳轉到資產管理，自動法幣提款，加入while迴圈調整次數
#版本：0.0.5，改寫顯性等待，讓它更穩定一點
#版本：0.0.6，需調整的資訊變數化

###

### 設定區開始 ###

#帳號、密碼、GA驗證碼
account = ""
password = ""
code = ""

#提領金額
amount = ""

#環境，要切環境改environment裡面的值
stage = ""
uat = ""
environment = f"{uat}"

#執行重複次數
repeat_times = 3

#計數用，初始為0，不用動
count = 0
#記金額用，初始為0，不用動
total = 0

### 設定區結束 ###


### 程式運行區 ###

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)
driver.get(f"{environment}")
driver.maximize_window()
driver.implicitly_wait(10)
driver_wait = WebDriverWait(driver,timeout= 2, poll_frequency=0.5)

sleep(1)

#點登入按鈕
search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-zn7x6a")))
search_box.click()


#帳號密碼
search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"account")))
search_box.send_keys(f"{account}")

search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"password")))
search_box.send_keys(f"{password}")


#點擊登入按鈕
search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-fullWidth.MuiButtonBase-root.css-8y0pui")))
search_box.click()

#驗證碼
search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"code")))
search_box.send_keys(f"{code}")


#移動到個人中心
search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-1bvwbgo")))
actions = ActionChains(driver)
actions.move_to_element(search_box).perform()
search_box.click()

sleep(1)

#點資產管理
search_box = driver_wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='___gatsby']/header/div[3]/div[1]/div[2]/div/ul/div[2]/li/a")))
search_box.click()

#點提領
search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-1ku9dxb")))
search_box.click()  

#while迴圈

while count < repeat_times:

#focus輸入金額欄位
    # search_box = driver.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[2]/div/div/input')
    # driver.execute_script("arguments[0].click();", search_box)

    search_box = driver_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[2]/div/div/input')))
    search_box.click()

#輸入金額
    search_box = driver_wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[2]/div/div/input')))
    search_box.send_keys(f"{amount}")

#點提款頁面輸入金額的確定
    search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-g6apxk.er50xhr0")))
    search_box.click()

#資金密碼，預設同登入密碼
    search_box = driver_wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/div/input')))
    search_box.send_keys(f"{password}")

#google驗證碼
    search_box = driver_wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[4]/div/input')))
    search_box.send_keys(f"{code}")

#確定提款
    search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-1385iwp.er50xhr0")))
    search_box.click()

#繼續提領
    search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-y1z3yc")))
    search_box.click()

    sleep(1)

    total += int(amount)
    count += 1
    print(f"完成第{count}次")

# 獲取當下時間
current_time = datetime.now()

# 格式化當下時間並印出
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"\n請求時間：{formatted_time}")

print(f"法幣提款次數：{count}")
print(f"法幣提款金額：{total}")


driver.quit()