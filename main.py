import time, json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

browser.get('https://www.decolar.com/lugares-para-viajar/orlando')
assert 'Guia Completo para Conhecer Orlando | Decolar' in browser.title

time.sleep(2)

# elem = WebDriverWait(browser, 10).until(
#   EC.element_to_be_clickable((By.CLASS_NAME, "offer-card-pricebox-price-amount"))
# )

elements = browser.find_elements(By.CLASS_NAME, 'offer-card-pricebox-price-amount')  # Find the search box
dados = {}

for elem in elements:
  dados['value'] = elem.text

jsonObject = json.dumps(dados, indent=4)

with open("myJsn.json", "w") as outfile:
  outfile.write(jsonObject)

print(dados)

browser.quit()
