from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

query = input('검색할 키워드를 입력하세요 : ')

url = "https://www.naver.com/" #접속할 사이트 지정
driver = webdriver.Chrome() #
driver.get(url) #
time.sleep(3)

search_box = driver.find_element(By.CSS_SELECTOR, '#query') #엘리먼트 찾기 엘리먼트는 페이지 안에 있는 요소들 검색창 같은거 CSS Selector 이걸 제일 많이 씀
search_box.send_keys(query) #마우스 키 입력
search_box.send_keys(Keys.RETURN) #마우스 키 입력 리턴은 엔터를 의미
time.sleep(2)

#뉴스 탭 클릭
driver.find_element(By.CSS_SELECTOR,'#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_btn_page._nav_btn_root > div.btn_next._next > a > span').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(8) > a').click()
time.sleep(3)

#텍스트와 링크 가져오기
news_titles = driver.find_elements(By.CSS_SELECTOR, ".news_tit")
print(news_titles)

for i in news_titles:
    title = i.text
    href = i.get_attribute('href')
    print(title , " : ", href)