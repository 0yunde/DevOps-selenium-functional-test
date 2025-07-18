# 🧪 Selenium Functional Test Automation 🚀

Este proyecto contiene una prueba funcional automatizada con **Selenium** que se ejecuta en un entorno de **CI usando GitHub Actions**, y genera un **reporte HTML** y capturas de pantalla como artefactos.

---

## 📁 Estructura del Proyecto

selenium-ftest/
├── .github/workflows/selenium-test.yml # Pipeline CI con GitHub Actions
├── assets/ # (opcional) Carpeta para capturas de error
├── ci_smoke_test.py # Script principal para CI
├── smoke_test.py # Versión con pytest para generar reportes
├── requirements.txt # Dependencias del proyecto
├── README.md # Este archivo 🙂
└── .gitignore # Archivos ignorados por Git

---

## ✅ ¿Qué hace este proyecto?

- Abre DuckDuckGo en modo `headless`
- Realiza una búsqueda automatizada
- Valida que existan resultados
- Genera captura en caso de fallo
- Produce reporte `HTML` con `pytest-html`
- Sube artefactos (screenshot + report) al pipeline

---

## 🔧 Tecnologías usadas

- [Selenium WebDriver](https://www.selenium.dev/)
- [Python 3.10+](https://www.python.org/)
- [pytest](https://docs.pytest.org/)
- [pytest-html](https://pypi.org/project/pytest-html/)
- [GitHub Actions](https://github.com/features/actions)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)

---

## 🚀 ¿Cómo correrlo localmente?

1. Clona el repositorio:
   ```bash
   git clone https://github.com/0yunde/DevOps-selenium-functional-test.git
   cd selenium-ftest

pip install -r requirements.txt

pytest smoke_test.py --html=report.html

🤖 CI con GitHub Actions
Cada vez que haces push o pull_request sobre main, GitHub Actions:

Instala dependencias en Ubuntu

Ejecuta el test funcional (ci_smoke_test.py)

Guarda los artefactos:

screenshot_error.png si falla

report.html como reporte HTMLZ