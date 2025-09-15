from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Ruta al chromedriver
service = Service("C:/Users/richa/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

#abro google
driver.get("https://www.google.com")

#aqui doy la instrucción de que buscar en el buscador
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Articulos Flor del desierto")
search_box.submit()

#espero a que carguen los resultados (en este caso puse 10sg, pero es dependiendo)
results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "h3"))
)

#extraigo los textos
titulos = [r.text for r in results if r.text.strip() != ""]

#guardo en un excel
df = pd.DataFrame(titulos, columns=["Titulos"])
df.to_excel("outputs/resultados_google.xlsx", index=False)

print("Resultados guardados en outputs/resultados_google.xlsx")

driver.quit()
