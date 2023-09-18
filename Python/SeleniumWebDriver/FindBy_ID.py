from selenium import webdriver
import time

from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("webdriver.chrome.driver=Drivers/chromedriver.exe")

driver = webdriver.Chrome(chrome_options)

driver.get("https://store.steampowered.com/login/?redir=%3Fl%3Dspanish&redir_ssl=1&snr=1_4_4__global-header")

email = driver.find_element(By.ID,"")
password = driver.find_element("newlogindialog_TextInput_2eKVn")

email.send_keys("luiaballz.laor@gmail.com")
password.send_keys("")