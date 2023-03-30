import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains
import functions
import csv

# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

file = open('Naver.csv', mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["title","outlines","director","grade"])

# 실행 반복 (네이버영화)
for i in range(2,23,1):
    driver.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
    driver.implicitly_wait(5)
    if i == 12:
        continue
    rank = driver.find_element(By.XPATH, 
            f'//*[@id="old_content"]/table/tbody/tr[{i}]/td[2]/div/a')
    rank.click()
    driver.implicitly_wait(5)

    title, outlines, director, grade = functions.find_main_module(driver.current_url)
    writer.writerow([title, outlines, director, grade])

file.close()

# //*[@id="old_content"]/table/tbody/tr[11]/td[2]/div/a
# //*[@id="old_content"]/table/tbody/tr[12]/td
# //*[@id="old_content"]/table/tbody/tr[13]/td[2]/div/a


# //*[@id="old_content"]/table/tbody/tr[2]/td[2]/div/a
# //*[@id="old_content"]/table/tbody/tr[3]/td[2]/div/a
# //*[@id="old_content"]/table/tbody/tr[22]/td[2]/div/a
