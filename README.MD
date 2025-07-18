# 🚀 Selenium Functional Test con GitHub Actions

Este proyecto realiza pruebas funcionales automatizadas utilizando **Selenium WebDriver**, integradas con **GitHub Actions** para ejecución continua (CI).

---

## ✅ ¿Qué hace este proyecto?

- Realiza una búsqueda en [DuckDuckGo](https://duckduckgo.com)
- Verifica que se obtienen resultados
- Genera un **reporte HTML** con `pytest-html`
- Captura una imagen en caso de error
- Publica los resultados como **artifact** en GitHub Actions

---

## 📁 Estructura del Proyecto

```bash
selenium-ftest/
├── .github/workflows/selenium-test.yml      # Pipeline CI con GitHub Actions
├── assets/                                  # (Opcional) Carpeta para capturas de error
├── ci_smoke_test.py                         # Script principal para CI
├── smoke_test.py                            # Versión con pytest para generar reportes
├── requirements.txt                         # Dependencias del proyecto
├── .gitignore                               # Archivos ignorados por Git
└── README.md                                # Este archivo 😄

⚙️ Instalación

# Clona el repositorio
git clone https://github.com/tu-usuario/selenium-ftest.git
cd selenium-ftest

# Crea un entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows usa: .venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

🧪 Ejecutar Pruebas Localmente

Opción A – Script de prueba simple
python ci_smoke_test.py

Opción B – Usando Pytest con HTML Reporte
pytest smoke_test.py --html=report.html

🖥️ Ver Reporte HTML
Después de ejecutar pytest, abre el archivo report.html en tu navegador:
start report.html  # En Windows
open report.html   # En macOS

🔄 Integración Continua (GitHub Actions)
El archivo .github/workflows/selenium-test.yml configura una pipeline que:

Instala dependencias

Ejecuta el test

Publica report.html y screenshot_error.png (si falla)

📦 Artifacts

GitHub subirá como artifacts:

✅ report.html: Resultado de la prueba

📸 screenshot_error.png: Solo si la prueba falla

📌 Requisitos

Python 3.10+

Google Chrome (en local si no usas headless)

Git
