🚀 selenium-ptest
Ejemplo de proyecto con pruebas funcionales en CI/Cd usando Selenium, pytest y GitHub Actions.

📁 Estructura del proyecto
bash
Copiar
Editar
selenium-ptest/
│
├── .github/workflows/selenium-test.yml   # Configuración del workflow CI con Actions
├── assets/                                # Capturas, configuraciones, etc. (opcional)
├── ci_smoke_test.py                       # Script principal para tests en CI
├── smoke_test.py                          # Versión con pytest para reportes HTML
├── requirements.txt                       # Dependencias del proyecto
└── README.md                              # Este archivo
🧪 Requisitos
Python 3.7+

Chrome instalado en runner (CI) o local

Dependencias definidas en requirements.txt:

text
Copiar
Editar
pytest
pytest-html
selenium
webdriver-manager
Instalación local:

bash
Copiar
Editar
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
🔄 Cómo ejecutar tests
🏠 En tu entorno local
Prueba manual:

bash
Copiar
Editar
python ci_smoke_test.py
Con pytest y reporte:

bash
Copiar
Editar
pytest smoke_test.py --html=report.html
Luego abre report.html en cualquier navegador para ver logs, pasos y capturas.

🔧 En CI (GitHub Actions)
Definimos el archivo .github/workflows/selenium-test.yml con estos pasos:

Checkout del repositorio

Instalación de Python y dependencias

Ejecución de ci_smoke_test.py en modo headless

Subida de captura de error (screenshot_error.png) como artifact

✅ Flujo del smoke test (ci_smoke_test.py)
Inicia Chrome en modo headless con webdriver-manager

Abre DuckDuckGo

Busca “inmuebles en Bogotá”

Valida que aparezcan resultados (h2 > a)

Si falla, captura screenshot

Cierra el navegador y retorna error si algo falló

📊 Reportes con pytest
El archivo smoke_test.py está preparado para usar pytest, genera un informe HTML con:

Resultado PASS/FAIL

Capturas automáticas al fallar

Logs detallados de cada paso

Ejemplo:

bash
Copiar
Editar
pytest smoke_test.py --html=report.html --self-contained-html
☁️ Artifacts en CI
GitHub Actions compila un artifact que incluye:

report.html (resultado de pytest)

screenshot_error.png si hay error

Puedes descargarlo desde la pestaña Artifacts del pipeline.

📝 Recomendaciones y mejoras
Agregar pytest fixtures para el setup/teardown del navegador

Usar pytest.ini para configurar filtros y logs

Extender tests a otros escenarios: login, formulario, navegación, etc.

Incluir análisis de cobertura o reportes de visualización

🎯 Objetivo del proyecto
Demostrar cómo integrar pruebas funcionales de interfaz con Selenium dentro de un pipeline CI moderno, generando reportes ricos y capturando errores automáticamente para facilitar el análisis y la mejora continua.
