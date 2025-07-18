from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

options = Options()
options.binary_location = brave_path

driver = webdriver.Chrome(options=options)
driver.get("https://duckduckgo.com/")

try:
    # Buscar campo de búsqueda
    buscador = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    buscador.send_keys("inmuebles en Bogotá")
    buscador.send_keys(Keys.RETURN)

    # Esperar resultados
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='result-title-a']"))
    )

    resultados = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    print(f"🔎 Se encontraron {len(resultados)} resultados.")
    assert len(resultados) > 0, "No se encontraron resultados."

    print("✅ Prueba funcional completada con éxito")

except Exception as e:
    print("❌ Error durante la prueba:")
    print(e)

finally:
    driver.quit()
