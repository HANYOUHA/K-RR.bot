from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



  
customa = 250

sale = 100

customz = 245

count = 50





driver = webdriver.Chrome(크롬 드라이버 경로)

driver.get("https://rivalregions.com/#parliament")
time.sleep(5)
driver.maximize_window()

time.sleep(10)

elem = driver.find_element_by_xpath("/html/body/div[4]/div[2]/a[1]/div").click()
time.sleep(5)

driver.find_element_by_name("email").click()
elem1 = driver.find_element_by_name("email")
time.sleep(7)

elem1.send_keys(face_book_id) 

time.sleep(7)

driver.find_element_by_name("pass").click()
elem2 = driver.find_element_by_name("pass")
time.sleep(7)

elem2.send_keys(face_book_pw) 
time.sleep(7)
driver.find_element_by_name("login").click()

time.sleep(15)

elem3 = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[6]").click()
time.sleep(10)


driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[3]/div[1]").click()
time.sleep(5)
price = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[3]/span/span").text#원하는 자원 선택
time.sleep(5)

str(price)
price2 = price[0:3]
# price3 = price[4:7]
print(price)

print(price2)

# print(price3)

# price4 = str(price2 + price3)

# int(price4)

# print(price4)

int(price2)

ad = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[3]/span/span").text 




driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[3]/div[1]").click()    #원하는 자원 칸 클릭

    

print(price2)



while int(price2) > 100: 
    
    

    
    customa = 250

    sale = 100

    customz = 245

    count = 50

 
  

    time.sleep(30)

  
    driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[3]/div[1]").click() 
        
    if int(price2) > customa:
        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[3]/div[1]").click()    #원하는 자원 칸 클릭
        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[1]/div/span").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/div[3]/input").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/div[3]/input").click()
        rem = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/div[3]/input")
        rem.send_keys(sale)
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/div[4]/div").click()
        time.sleep(5)
    elif int(price2) < customz:
        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[3]/div[1]").click()    #원하는 자원 칸 클릭


        driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[5]").click()
        time.sleep(10)

        rb = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[5]/input")
        time.sleep(5)
        rb.send_keys(count)
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/div[6]/div[1]/span[1]").click()
        time.sleep(2)

        time.sleep(60)

    driver.refresh()