import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = "https://games-stats.com/steam/game/grand-theft-auto-v/"
#url = 'https://games-stats.com/steam/game/tom-clancys-rainbow-sixr-siege/'

# 페이지 열기
driver.get(url)

# 페이지가 로드될 때까지 기다리기 (최대 10초 대기)
wait = WebDriverWait(driver, 3000)
time.sleep(3000)

driver.close()