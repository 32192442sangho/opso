import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# 크롤링할 페이지 범위 설정 (1부터 3545까지)
start_page = 1
end_page = 30   #3568

# href 속성을 저장할 리스트 생성
total_href_list = []

# 각 페이지에 접속하고 데이터 크롤링
for page_number in range(start_page, end_page):
    print(f"@@@@@{page_number}@@@@@")
    # 페이지 URL 생성
    url = f"https://games-stats.com/steam/?title=&page={page_number}"

    # 페이지 열기
    driver.get(url)

    # 페이지가 로드될 때까지 기다리기 (최대 10초 대기)
    wait = WebDriverWait(driver, 20)
    try:
        element = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/section/div[1]/div/div[4]/table/tbody/tr[1]/td[2]/a[1]"))
        )
    except:
        try:
            element = wait.until(
                EC.presence_of_element_located((By.XPATH, "/html/body/section/div[1]/div/div[3]/table/tbody/tr[1]/td[2]/a[1]"))
            )
        except:
            print(f"페이지 {page_number}에서 요소를 찾을 수 없습니다.")
            continue

    # 모든 <a> 태그에서 href 속성 추출하여 리스트에 저장
    for i in range(1, 31):
        xpath = f"/html/body/section/div[1]/div/div[4]/table/tbody/tr[{i}]/td[2]/a[1]"
        try:
            element = driver.find_element(By.XPATH, xpath)
        except:
            try:
                xpath = f"/html/body/section/div[1]/div/div[3]/table/tbody/tr[{i}]/td[2]/a[1]"
                element = driver.find_element(By.XPATH, xpath)
            except:
                print(f"페이지 {page_number}의 {i}번째 요소를 찾을 수 없습니다.")
                continue
        href = element.get_attribute("href")
        if href:
            total_href_list.append(href)
        time.sleep(1)
        print(len(total_href_list))
    time.sleep(3)
print(f"추출된 href 리스트 ({len(total_href_list)}개): {total_href_list}")

#######################################################################################################################

"""
url = f"https://games-stats.com/steam/?title=&page=last"

# 페이지 열기
driver.get(url)

# 페이지가 로드될 때까지 기다리기 (최대 10초 대기)
wait = WebDriverWait(driver, 20)
try:
    wait.until(
        EC.presence_of_element_located((By.XPATH, "/html/body/section/div[1]/div/div[4]/table/tbody/tr[1]/td[2]/a[1]")))
except:
    try:
        wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/section/div[1]/div/div[3]/table/tbody/tr[1]/td[2]/a[1]")))
    except:
        print("마지막 페이지를 찾을 수 없습니다.")

# 각 페이지에서 게임 링크 추출
for i in range(1, 31):
    xpath = f"/html/body/section/div[1]/div/div[4]/table/tbody/tr[{i}]/td[2]/a[1]"
    try:
        element = driver.find_element(By.XPATH, xpath)
    except:
        xpath = f"/html/body/section/div[1]/div/div[3]/table/tbody/tr[{i}]/td[2]/a[1]"
        try:
            element = driver.find_element(By.XPATH, xpath)
        except:
            print("마지막 페이지에서 게임 링크를 찾을 수 없습니다.")
            break
    href = element.get_attribute("href")
    if href:
        total_href_list.append(href)
    time.sleep(3)

print(f"추출된 href 리스트 ({len(total_href_list)}개): {total_href_list}")

# 브라우저 종료
"""
driver.quit()
