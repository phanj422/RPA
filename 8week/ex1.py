from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = "https://www.google.co.kr/" #접속할 사이트 지정
driver = webdriver.Chrome() #
driver.get(url) #
time.sleep(3)

search_box = driver.find_element(By.CSS_SELECTOR, '#APjFqb') #엘리먼트 찾기 엘리먼트는 페이지 안에 있는 요소들 검색창 같은거 CSS Selector 이걸 제일 많이 씀
search_box.send_keys("KBO 한국 시리즈") #마우스 키 입력
search_box.send_keys(Keys.RETURN) #마우스 키 입력 리턴은 엔터를 의미
time.sleep(20)