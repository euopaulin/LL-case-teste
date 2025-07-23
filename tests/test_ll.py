import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-proxy-server")     # Ignora proxy de sistema
options.add_argument('--proxy-server=')       # Zera explicitamente o proxy

driver = webdriver.Chrome(options=options)

# Inicia o navegador
driver = webdriver.Chrome()

# Abre a página
driver.get("https://ll.ipea.gov.br/")

# Interação de exemplo
driver.find_element(By.ID, "username").send_keys("t07692665176s")

driver.find_element(By.ID, "password").send_keys("Spfc202430")

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

driver.find_element(By.XPATH, '//button[contains(@onclick, "dadosdelogoff.php)]').click()



# Encerra o navegador
