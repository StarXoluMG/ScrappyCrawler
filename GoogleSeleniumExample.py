#import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#holding a list
element_list = []

for page in range (1,3,1):
    page_url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}"
    # Create a Service object
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(page_url)

    title = driver.find_elements(By.CLASS_NAME,"title")
    price = driver.find_elements(By.CLASS_NAME,"price")
    description = driver.find_elements(By.CLASS_NAME,"description")
    ratings = driver.find_elements(By.CLASS_NAME,"ratings")

    for i in range(len(title)):
        element_list.append([title[i].text,price[i].text, description[i].text, ratings[i].text])

print(element_list)

driver.close()