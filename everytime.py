import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from bs4 import BeautifulSoup

# selenium 사용 코드 : 자동화
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 창 최대화
driver.maximize_window()

# 주소 가져 오기
driver.get('https://everytime.kr/')
time.sleep( random.uniform(2,4) )

#로그인 클릭
driver.find_element(By.XPATH,'/html/body/aside/div[1]/a[2]').click()

#로그인 정보 입력
driver.find_element(By.XPATH,'//*[@id="container"]/form/p[1]/input').send_keys('') #본인 아이디
driver.find_element(By.XPATH,'//*[@id="container"]/form/p[2]/input').send_keys('') #본인 비밀번호
time.sleep( random.uniform(15,20) )

#로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="container"]/form/p[3]/input').click()
time.sleep( random.uniform(2,4) )



link =['https://everytime.kr/384376/v/300184406','https://everytime.kr/384376/v/299356097'] # 가져올 링크 리스트에 담기
reply_list = []


result = []
html = driver.page_source
bs = BeautifulSoup(html,'html.parser')

#링크에 접속하기
for temp in link:
    driver.get(temp)
    time.sleep(random.uniform(4, 6))
    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    # 글 적혀있는 부분 가져오기
    content = bs.find_all('p', class_ = 'large')

    for temp1 in content:
        print(temp1.text)
        result.append(temp1.text)

df = pd.DataFrame(result)
df.to_csv('에타_result.csv')