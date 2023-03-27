from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'C:/Users/Liam/Documents/NEXT_HW/Session5/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (멜론 차트)
driver.get("https://www.melon.com/index.htm")
driver.implicitly_wait(3)
# 멜론 차트 버튼 클릭
chartbtn = driver.find_element(By.XPATH, "//*[@id='gnb_menu']/ul[1]/li[1]/a/span[2]")
chartbtn.click()
# 1위곡명 가져오기

driver.implicitly_wait(20)

first = driver.find_element(By.XPATH, '(//*[@id="lst50"]/td[6]/div/div/div[1]/span/a)[2]').text
print(first)

sc = driver.find_element(By.XPATH, '//*[@id="lst50"]/td[6]/div/div/div[1]/span/a').text
print(sc)


# 1위부터 20위까지 가져오기
# //*[@id="lst50"]/td[6]/div/div/div[1]/span/a
# //*[@id="lst50"]/td[6]/div/div/div[1]/span/a
# 스크롤 내리기

# 실시간 급상승 가수 가져오기

# 곡의 장르 가져오기
l = driver.find_element(By.XPATH, '//*[@id="top_search"]')
l.send_keys('김승민')
l.send_keys(Keys.ENTER)

# 좋아하는 가수의 곡명 10개

for i in range(1,11):
    sc = driver.find_element(By.XPATH, f'//*[@id="frm_searchArtist"]/div/table/tbody/tr[{i}]/td[3]/div/div/a[2]').text
    print(sc)
# 순위, 곡명, 가수명 가져오기
# //*[@id="frm_searchArtist"]/div/table/tbody/tr[2]/td[3]/div/div/a[2]

# csv 파일로 변환