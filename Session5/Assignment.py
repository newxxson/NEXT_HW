from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.request
from selenium.webdriver.common.by import By
from functions import find_data
import pandas as pd


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'C:/Users/Liam/Documents/NEXT_HW/Session5/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)


origin = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
driver.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
driver.implicitly_wait(3)

request_headers = { 
'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36'), } 

crawled_data = []

for i in range(2,23): #2부터 시작 12없음 23까지
    if i == 12:
        continue
    chartbtn = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{i}]/td[2]/div/a')
    chartbtn.click()
    row = find_data(driver=driver, header=request_headers)

    crawled_data.append(row)

    driver.get(origin)
    driver.implicitly_wait(3)

to_cv = pd.DataFrame(crawled_data, columns=['Title', 'Outline', 'director', 'rate'])

to_cv.to_csv('./product.csv', encoding='cp949')
to_cv.head()
