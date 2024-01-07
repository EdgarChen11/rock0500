# 測試開始
print("測試開始")

# 導入套件
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from datetime import datetime
# 顯性等待​
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

### 設定區開始 ###

# 帳號、密碼
account = "test001@gmail.com"
password = "abab12"

stage = "https://www.dogcatstar.com/"
uat = ""
environment = f"{stage}"


### 設定區結束 ###

### 程式運行區 ###

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)
driver.get(f"{environment}")
driver.maximize_window()
driver.implicitly_wait(10)
driver_wait = WebDriverWait(driver,timeout= 2, poll_frequency=0.5)

# 點登入按鈕，帳號密碼
search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".nav-top-link.nav-top-not-logged-in.icon.primary.button.circle.is-small")))
search_box.click()

search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"username")))
search_box.send_keys(f"{account}")

search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"password")))
search_box.send_keys(f"{password}")

# 點登入
try:
    search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"login")))
    search_box.click()
except TimeoutException:
    print("等待超時，無法找到元素")
except Exception as error:
    print(f"發生未知錯誤：{error}")

sleep(1)

# 登入成功與否確認
page_source = driver.page_source
keyword = "我的帳號"
assert keyword in page_source, f"根本就不能用啊: {keyword}"
print("登入成功")

# 模擬滑鼠移動到[我的帳號]上面
search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".account-link.account-login.icon.primary.button.circle.is-small")))
actions = ActionChains(driver)
actions.move_to_element(search_box).perform()

# 點登出
try:
    search_box = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-2648")))
    search_box.click()
except TimeoutException:
    print("等待超時，無法找到元素")
except Exception as error:
    print(f"發生未知錯誤：{error}")

sleep(1)

# 登出成功與否確認
page_source = driver.page_source
keyword = "即可直接解鎖推薦碼，分享賺取點數！"
assert keyword in page_source, f"根本就不能用啊: {keyword}"
print("登出成功")


driver.quit()

# 測試結束
print("測試結束")