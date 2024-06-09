import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

# 크롤링할 페이지 범위 설정 (1부터 3545까지)
start_page = 3
end_page = 4   #3568

# href 속성을 저장할 리스트 생성
total_href_list = []

# 각 페이지에 접속하고 데이터 크롤링
for page_number in range(start_page, end_page):
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
            print(f"can't find element at page {page_number}")
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
                print(f"The {i}th element of page {page_number} could not be found.")
                continue
        href = element.get_attribute("href")
        if href:
            total_href_list.append(href)
        time.sleep(1)
    time.sleep(3)

game_info = []
code = ''

for game in total_href_list:
    # 페이지 URL 생성
    url = game
    driver.get(url)

    wait = WebDriverWait(driver, 20)
    wait.until(
        EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div/div/div[1]/p[14]/strong"))
    )

    game_name = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/h1/strong").text  # 이름 v

    release_date = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[1]/p[7]/span[1]").text  # 출시일  v
    temp = release_date.split()
    if temp[0] == 'Jan':
        temp[0] = '01'
    elif temp[0] == 'Feb':
        temp[0] = '02'
    elif temp[0] == 'Mar':
        temp[0] = '03'
    elif temp[0] == 'Apr':
        temp[0] = '04'
    elif temp[0] == 'May':
        temp[0] = '05'
    elif temp[0] == 'Jun':
        temp[0] = '06'
    elif temp[0] == 'Jul':
        temp[0] = '07'
    elif temp[0] == 'Aug':
        temp[0] = '08'
    elif temp[0] == 'Sep':
        temp[0] = '09'
    elif temp[0] == 'Oct':
        temp[0] = '10'
    elif temp[0] == 'Nov':
        temp[0] = '11'
    elif temp[0] == 'Dec':
        temp[0] = '12'
    release_date = temp[2] + '-' + temp[0] + '-' + temp[1][:-1]

    revenue = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[1]/p[14]").text
    temp = revenue.split()
    if len(temp) == 3:
        unit = 1
    elif len(temp) == 4:
        unit = 1000000
    else:
        unit = 0
    num = int(temp[2][2:])
    revenue_in_int = num * unit
    price = float(driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[1]/p[8]").text.split()[1][1:])
    sales_numbers = str(int(revenue_in_int / price))
    sales_numbers = sales_numbers[:2] + '0' * (len(sales_numbers) - 2)
    if int(sales_numbers[1]) > 4:
        sales_numbers = sales_numbers[0] + '5' + sales_numbers[2:]
    else:
        sales_numbers = sales_numbers[0] + '0' + sales_numbers[2:]
    sales_numbers_reverse = sales_numbers[::-1]
    parts = [sales_numbers_reverse[i:i + 3] for i in range(0, len(sales_numbers_reverse), 3)]
    sales_numbers = ','.join(parts)[::-1]
    sales_numbers = sales_numbers + '+'

    genre_t = driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/p[13]").text.split()  # 카테고리, 장르
    genre = ""
    for i in genre_t[1:]:
        genre = genre + i


    youtube_trailer = "None"

    game_info.append([game_name, genre, release_date, sales_numbers, youtube_trailer])

for i in game_info:
    temp = f"""[
    'title' => '{i[0]}',
    'category' => '{i[1]}',
    'release_date' => '{i[2]}',
    'sales_numbers' => '{i[3]}',
    'github_username' => '32192442sangho',
    'youtube_trailer' => '{i[4]}'
],
"""
    code = code + temp

print(code)