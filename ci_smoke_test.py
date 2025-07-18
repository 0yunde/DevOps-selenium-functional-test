from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://duckduckgo.com/")

    buscador = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    buscador.send_keys("inmuebles en Bogotá")
    buscador.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='result-title-a']"))
    )

    resultados = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    print(f"🔎 Se encontraron {len(resultados)} resultados.")
    assert len(resultados) > 0, "No se encontraron resultados."

    print("✅ CI test completado con éxito")

except Exception as e:
    print(f"❌ Error en el test de CI: {e}")

finally:
    driver.quit()
