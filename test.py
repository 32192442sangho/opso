import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://games-stats.com/steam/game/tom-clancys-rainbow-sixr-siege/'  #'https://games-stats.com/steam/game/tom-clancys-rainbow-sixr-siege/' 'https://games-stats.com/steam/game/grand-theft-auto-v/'
#url = 'https://games-stats.com/steam/game/grand-theft-auto-v/'
driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 20)
wait.until(
    EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div/div/div[1]/p[14]/strong"))
)

game_name = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/h1/strong").text
print(game_name)
release_date = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[1]/p[7]/span[1]").text
print(release_date)
profit = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[1]/p[14]").text
print(profit)
tags = driver.find_elements(By.XPATH, "/html/body/section/div[1]/div/div/div[1]/p[12]/span/a")
print(len(tags))
for tag in tags:
    print(tag.text)
print("@@@@@@@@@@@@@@@@@")
try:
    game_price = driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/p[8]/span[1]").text
except:
    game_price = driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/p[8]").text
print(game_price)

time.sleep(60)

