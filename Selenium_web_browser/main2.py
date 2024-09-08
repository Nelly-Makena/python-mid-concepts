from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# Find event dates
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

# Print each date in a simple format (YYYY-MM-DD)
for time in event_times:
    full_date = time.get_attribute('datetime')
    # Convert the datetime string to a date object and format it
    formatted_date = datetime.fromisoformat(full_date).strftime('%Y-%m-%d')
    print(formatted_date)


event_name = driver.find_elements(By.CSS_SELECTOR, value =".event-widget li a")

for name in event_name:
    # Convert the datetime string to a date object and format it
    print(name.text)


events ={}

for n in range(len(event_times)):
    events[n] ={
        "time": event_times[n].text,
        "name": event_name[n].text,
    }


print(events)
