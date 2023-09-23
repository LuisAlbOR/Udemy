from selenium import webdriver
import time
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("webdriver.chrome.driver=Drivers/chromedriver.exe")

driver = webdriver.Chrome(chrome_options)

driver.maximize_window()
time.sleep(1)
driver.get("https://apps.cognitiveclass.ai/authn/login?next=%2Foauth2%2Fauthorize%3Fclient_id%3DXCTzu9NHWn%26redirect_uri%3Dhttps%253A%252F%252Fcognitiveclass.ai%252Fauth%252Fopen_edx%252Fcallback%26response_type%3Dcode%26scope%3Duser_id%2Bprofile%2Bemail%26state%3D9d93a296bdad24becbb5ee9d29225138557bfb118afd8456")

time.sleep(5)
email = driver.find_element(By.ID,"emailOrUsername")
password = driver.find_element(By.ID,"password")

email.send_keys("ortizrlalberto@gmail.com")
time.sleep(2)
password.send_keys("ClashRoyale-1")
time.sleep(2)
boton = driver.find_element(By.ID,"sign-in")
boton.click()
time.sleep(10)
driver.close()