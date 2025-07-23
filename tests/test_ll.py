from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicia o navegador
driver = webdriver.Chrome()

# Abre a página
driver.get("https://ll.ipea.gov.br/")

# Interação de exemplo
driver.find_element(By.CSS_SELECTOR, "submit").click()

# Encerra o navegador
driver.quit()
