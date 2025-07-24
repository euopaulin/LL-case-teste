import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--no-proxy-server")     # Ignora proxy de sistema
options.add_argument('--proxy-server=')       # Zera explicitamente o proxy

driver = webdriver.Chrome(options=options)

# Abre a página
driver.get("https://ll.ipea.gov.br/")

def fazer_login(driver):
    driver.find_element(By.ID, "username").send_keys("t07692665176s")

    driver.find_element(By.ID, "password").send_keys("Spfc202430")

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    time.sleep(2)  # Aguarda o login ser processado

def acessar_logoff(driver):
    driver.find_element(By.XPATH, '//button[contains(@onclick, "dadosdelogoff.php")]').click()

    driver.find_element(By.ID, "matricula").send_keys("t07692665176")

    driver.find_element(By.ID, "data_inicio").send_keys("10/06/2025")

    driver.find_element(By.ID, "data_fim").send_keys("20/06/2025")

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    time.sleep(2)  # Aguarda o logoff ser processado

def acessar_monitoramento(driver):
    
    driver.find_element(By.ID, "monitoramentoDropdown").click()

    driver.find_element(By.CSS_SELECTOR, 'a[href="monitoramento\\ incidentes.php"]').click()

fazer_login(driver)
acessar_logoff(driver)
acessar_monitoramento(driver)

# Encerra o navegador
