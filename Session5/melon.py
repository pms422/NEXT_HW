from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (멜론 차트)
driver.get("https://www.melon.com/index.htm")

# 멜론 차트 버튼 클릭
chartbtn = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]')
chartbtn.click()

# 1위곡명 가져오기
# first = driver.find_element(By.XPATH, '//*[@id="lst50"]/td[6]/div/div/div[1]/span/a').text
# print(first)
# time.sleep(3)

# 1위부터 20위까지 가져오기
# for i in range(20):
#    first = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i+1}]/td[6]/div/div/div[1]/span/a').text
#    print(first)
#    time.sleep(3)

# 스크롤 내리기

# 곡의 장르 가져오기
# chartbtn2 = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[1]/td[4]/div/a/span')
# chartbtn2.click()
# first = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/div[2]/dl/dd[2]').text
# print(first)

# 실시간 급상승 가수 가져오기

# 좋아하는 가수의 곡명 10개
# chartbtn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/fieldset/input[1]')
# chartbtn.click()
# time.sleep(3)

# chartbtn.send_keys('아이유')
# time.sleep(3)
# chartbtn2 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/fieldset/button[2]/span')
# chartbtn2.click()

# for i in range(10):
#    first = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div[1]/div[4]/div/form[1]/div/table/tbody/tr[{i+1}]/td[3]/div/div/a[2]').text
#    print(first)
#    time.sleep(3)

# 순위, 곡명, 가수명 가져오기
# csv 파일로 변환

import csv

file = open('melon.csv', mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["first"])

for i in range(10):
    first = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i+1}]/td[6]/div/div/div[1]/span/a').text
    print(first)

    writer.writerow([first])
file.close()


