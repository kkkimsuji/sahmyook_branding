from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.maximize_window()
	driver.get('https://www.univ100.kr/review/56') #대학후기 주소

time.sleep(3)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
time.sleep(1)
same_count = 0
saved_comment = []
saved_comment_re = []

for temp1 in range(10000):
    review_list = []
    comment_list = driver.find_elements(By.CSS_SELECTOR,'div.review__content')
    print(len(comment_list))

    for temp in comment_list:
        print(temp.text)
        saved_comment.append(temp.text)

    print('******************')
    print(temp.text)
    print(saved_comment[-1])
    print('******************')
    if  len(saved_comment_re) > 0 and temp.text == saved_comment_re[-1]:
        same_count += 1
    else:
        same_count=0

    if same_count == 5:
        break

    saved_comment_re = saved_comment.copy()

    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    print('-------------------------------------------------------------------')

df = pd.DataFrame(saved_comment)
df.to_csv('대학백과_리뷰.csv')