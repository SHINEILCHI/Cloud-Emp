import ssl
import time

import websockets
from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio
from websockets.server import serve
from websockets.sync.client import connect

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://challenge.longshotsystems.co.uk/go")

# submit button
submit_button = driver.find_element(By.XPATH, value="//button[normalize-space()='Submit']")
nb_0 = driver.find_element(By.ID, value="number-box-0").get_attribute("textContent").split()[0]
nb_1 = driver.find_element(By.ID, value="number-box-1").get_attribute("textContent").split()[0]
nb_2 = driver.find_element(By.ID, value="number-box-2").get_attribute("textContent").split()[0]
nb_3 = driver.find_element(By.ID, value="number-box-3").get_attribute("textContent").split()[0]
nb_4 = driver.find_element(By.ID, value="number-box-4").get_attribute("textContent").split()[0]
nb_5 = driver.find_element(By.ID, value="number-box-5").get_attribute("textContent").split()[0]
nb_6 = driver.find_element(By.ID, value="number-box-6").get_attribute("textContent").split()[0]
nb_7 = driver.find_element(By.ID, value="number-box-7").get_attribute("textContent").split()[0]


number_combinations = nb_0 + nb_1 + nb_2 + nb_3 + nb_4 + nb_5 + nb_6 + nb_7
print(number_combinations)
answer_box = driver.execute_script(f"document.getElementById('answer').value = '{number_combinations}'")
name_box = driver.execute_script("document.getElementById('name').value = 'Neil Patrick Elison'")
driver.execute_script("arguments[0].click();", submit_button)

# driver.quit()
