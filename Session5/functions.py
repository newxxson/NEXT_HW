from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.request
from selenium.webdriver.common.by import By
import requests

def find_title(soup):
    text = soup.select('.h_movie > a')[0].text
    return text

def find_outline(soup):
    span = soup.select(".info_spec > dd > p > span")[0]

    outlines = []

    for a in span:
        temp = str(a.text)
        temp = temp.strip()
        if len(temp)==0 or temp==',':
            continue
        outlines.append(temp)

    return ', '.join(outlines)

def find_director(soup):
    dd = soup.select('.info_spec > dd')[1]
    a = dd.select('p > a')
    t = a[0].text
    return t

def find_rate(soup):
    text = soup.select('.sc_view > .star_score > em')[0].text

    return text



def find_data(driver, header):
    driver.implicitly_wait(3)
    current_url = str(driver.current_url)
    
    raw = requests.get(current_url, headers=header)
    soup = BeautifulSoup(raw.text, 'html.parser')

    title = find_title(soup)
    outline = find_outline(soup)
    director = find_director(soup)
    rate = find_rate(soup)

    return [title, outline, director, rate]


    