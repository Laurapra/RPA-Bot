from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#ruta de chromedriver.exe
service = Service("C:/Users/richa/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

#inicializo el navegador con Service
driver = webdriver.Chrome(service=service)

#abro google
driver.get("https://www.google.com")

#tiempo de espera (aqui pongo el timeer necesario)
time.sleep(2)

#busco algo (pongo a que ejecute la tarea)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("RPA con Python y Selenium")
search_box.submit()

#tiempo de espera de resultados de la tarea que le puse
time.sleep(3)

#cierro el navegador
driver.quit()
