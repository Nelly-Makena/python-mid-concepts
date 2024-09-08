from selenium import webdriver
from selenium.webdriver.common.by import By

#keep browser open

chrome_options =webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_3?crid=1I2AKL4C0T4NN&dib=eyJ2IjoiMSJ9.A57Pfadt9NRA6JrICgAO3w4OaSgCclf4cbX0_uI0bIGytG8-A_6_RQ0PcwDHCwKqtdMwzFWPk1a4W2VY2_ecL1_S_GCYEubIRxM-F_AcswHK4VIhb5H9iyDnKHOWNWP86u_4fy80Ql5zA0KxBGH_QINEQo7_P94A66Jn7G6IjNL_6wxAiQzPpqG_QGcuGTRRdUQz7oBlaYL_AT1i5rLf8flb3dL_UHfXh7_3UurxzNk.xJKEUfwTu-RqWuQtVMc4JBUFVPDryXOXMRLdM5EJgPE&dib_tag=se&keywords=instant%2Bpot&qid=1723899347&sprefix=instant%2B%2Caps%2C1001&sr=8-3&th=1")

price_dollar =driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents  =driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text} . {price_cents.text}")











driver.quit()

