from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("webdriver.chrome.driver=Drivers/chromedriver.exe")

driver = webdriver.Chrome(chrome_options)

driver.maximize_window()
driver.get("https://www.udemy.com/")
driver.close()