from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

search = '강아지'
fileName = './dog/dog_image'
number = 30

driver = webdriver.Chrome("./chromedriver")

#이미지 검색
driver.get(f'https://www.google.com/search?q={search}&tbm=isch&hl=ko&tbs=il:ol&sa=X&ved=0CAAQ1vwEahcKEwjgsYnZmu76AhUAAAAAHQAAAAAQCA&biw=1265&bih=976')

#첫번째 이미지 선택
firstImage = driver.find_element(By.CSS_SELECTOR,"#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img")

firstImage.click()

for i in range(number):
    try:
        time.sleep(0.5)
        # 선택한 이미지 다운
        image = driver.find_element(By.CSS_SELECTOR,"#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id.b0vFpe > div > a > img")

        imageSrc = image.get_attribute('src')
        urllib.request.urlretrieve(imageSrc, f'{fileName}_{i+1}.jpg')
    except:
        print(f'{i+1} 번째 이미지 오류')

    finally:
        #다음 이미지 이동
        nextBtn = driver.find_element(By.CSS_SELECTOR,"#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.mWagE.fDqwl > a:nth-child(4)")
        nextBtn.click()

time.sleep(1)
driver.quit()