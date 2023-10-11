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

#版本：1.0.0，基於提法幣改寫
#版本：1.1.0，改寫顯性等待，讓它更穩定一點
#版本：1.2.0，需調整的資訊變數化

###

### 設定區開始 ###

#帳號、密碼、GA驗證碼
account = ""
password = ""
code = ""

#幣種、公鏈名稱
coin = ""
chain_name = ""

#提幣數量
amount = ""

#提幣地址
inner_address = ""
outer_address = ""
address = f"{inner_address}"

#環境，要切環境改environment裡面的值
stage = ""
uat = ""
environment = f"{uat}"

#執行重複次數
repeat_times = 2

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

#點提幣
search_box = driver_wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/div/p[2]')))
search_box.click()  

#選擇幣種button
search_box = driver_wait.until(EC.presence_of_element_located((By.ID,"mui-component-select-currencyId")))
search_box.click()

#選擇幣種USDT
search_box = driver_wait.until(EC.presence_of_element_located((By.XPATH,f"//li[text()='{coin}']")))
search_box.click()


#while迴圈
while count < repeat_times:

    #選擇公鏈
    search_box = driver_wait.until(EC.presence_of_element_located((By.ID,"mui-component-select-subCoinId")))
    search_box.click() 

    #選擇鏈
    search_box = driver_wait.until(EC.presence_of_element_located((By.XPATH,f"//li[text()='{chain_name}']")))
    search_box.click() 

    #填提幣地址
    search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"address")))
    search_box.send_keys(f"{address}")

    #填金額
    search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"amount")))
    search_box.send_keys(f"{amount}")

    #填收款者姓名
    search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"beneficiary")))
    search_box.send_keys("提款機器人")

    #填收幣地址資訊
    search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"beneficiaryAddressInfo")))
    search_box.send_keys("機油好難喝")
    
    #填提幣用途
    search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"withdrawalRemarks")))
    search_box.send_keys("自動化提幣")

    #填資金密碼
    search_box = driver_wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div/div/div[1]/div[2]/div/div/div/div[11]/div/input')))
    search_box.send_keys(f"{password}")

    #填Google驗證碼
    search_box = driver_wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div/div/div[1]/div[2]/div/div/div/div[12]/div/input')))
    search_box.send_keys(f"{code}")

    #打勾
    search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".PrivateSwitchBase-input.css-1m9pwf3")))
    search_box.click()

    #點確認提幣
    search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-g6apxk.er50xhr0")))
    search_box.click()

    total += int(amount)
    count += 1
    print(f"完成第{count}次")
    
    #瀏覽器滑到最上面
    driver.execute_script("window.scrollTo(0, 0);")

    sleep(1.5)
    
# 獲取當下時間
current_time = datetime.now()

# 格式化當下時間並印出
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"\n請求時間：{formatted_time}")

print(f"幣種：{coin}")
print(f"公鏈：{chain_name}")
print(f"數幣提款次數：{count}")
print(f"數幣提款金額：{total}")


driver.quit()

