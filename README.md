# 🤖 RPA Bot con Selenium y Python

Este proyecto es un **Robot de Automatización de Procesos (RPA)** desarrollado en Python con **Selenium**.  
El bot abre Google, busca un término definido, extrae los títulos de los resultados y los guarda en un archivo Excel.  

---

## 🚀 Tecnologías utilizadas
- [Python 3.10+](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)
- [ChromeDriver](https://chromedriver.chromium.org/)

---

## 📂 Estructura del proyecto
rpa-bot/
│── bot_excel.py # Script principal del bot
│── requirements.txt # Dependencias del proyecto
│── outputs/ # Carpeta donde se guardan los resultados
│ └── resultados_google.xlsx

yaml
Copiar código

---

## ⚙️ Instalación y configuración

1. **Clonar el repositorio**  
```bash
git clone https://github.com/tu-usuario/rpa-bot.git
cd rpa-bot
Crear entorno virtual (opcional pero recomendado)

bash
Copiar código
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
Instalar dependencias

bash
Copiar código
pip install -r requirements.txt
Descargar ChromeDriver

Descarga la versión de ChromeDriver compatible con tu navegador.

Actualiza en bot_excel.py la ruta al ejecutable de ChromeDriver:

python
Copiar código
service = Service("C:/ruta/a/chromedriver.exe")
▶️ Ejecución del bot
Ejecuta el script con:

bash
Copiar código
python bot_excel.py
El bot hará lo siguiente:

Abrirá Google.

Buscará la frase "Articulos Flor del desierto".

Extraerá los títulos de los resultados de búsqueda.

Guardará los resultados en outputs/resultados_google.xlsx.
```
📊 Ejemplo de salida
Archivo Excel generado (resultados_google.xlsx):

Titulos
Artículos Flor del Desierto - Tienda
Catálogo Flor del Desierto 2025
Comprar accesorios Flor del Desierto

🚧 Posibles mejoras
Permitir que el usuario ingrese el término de búsqueda desde consola.

Manejo de captchas y detección de bloqueos de Google.

Exportación adicional a CSV o base de datos.

Integración con APIs externas para automatizar más procesos.

👩‍💻 Autor
Laura Patricia Rodriguez Angulo
💡 Proyecto de práctica para aprender RPA con Python y Selenium.
