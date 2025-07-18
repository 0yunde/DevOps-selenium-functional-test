def test_busqueda_en_duckduckgo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("🚀 Navegando a DuckDuckGo...")
        driver.get("https://duckduckgo.com/")

        print("⌨️ Buscando 'inmuebles en Bogotá'...")
        buscador = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        buscador.send_keys("inmuebles en Bogotá")
        buscador.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2 > a"))
        )

        resultados = driver.find_elements(By.CSS_SELECTOR, "h2 > a")
        print(f"🔎 Se encontraron {len(resultados)} resultados.")
        assert len(resultados) > 0, "No se encontraron resultados en la búsqueda"

    finally:
        driver.quit()
