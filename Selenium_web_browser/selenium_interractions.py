from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name= driver.find_element(By.NAME, value="fName")
last_name= driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")


#filling the form
first_name.send_keys("Nelly")
last_name.send_keys("Makena")
email.send_keys("nellymakenakarithi@gmail.com")

button =driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()