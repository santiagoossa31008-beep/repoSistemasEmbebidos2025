# 🐍 Laboratorio de Sistemas Embebidos con Raspberry Pi

Este repositorio contiene los ejercicios y proyectos desarrollados para la clase de **Sistemas Embebidos**, utilizando la plataforma **Raspberry Pi** y programación en **Python**.

El objetivo principal es aplicar conceptos de computación embebida, interacción con hardware (GPIO) y comunicación a través de protocolos como SSH.

---

## 💻 Configuración y Herramientas

Para trabajar con este repositorio, se utiliza la siguiente configuración y herramientas principales:

* **Plataforma Embebida:** Raspberry Pi (modelo específico, si se conoce, se puede añadir).
* **Sistema Operativo:** Raspberry Pi OS (anteriormente Raspbian).
* **Acceso Remoto:** **SSH** mediante clientes como **PuTTY**.
* **Lenguaje de Programación:** **Python 3**.
* **Entorno de Desarrollo:** Se recomienda el uso de **nano** o **vim** directamente en la Raspberry Pi, o un editor con conexión SSH/SFTP.

---

## 📂 Estructura del Repositorio

Los códigos están organizados por temas o números de práctica:
. ├── 📂 practica_01_introduccion/ │ ├── 📄 ejemplo_hola_mundo.py │ └── 📄 ... ├── 📂 practica_02_gpio_basico/ │ ├── 📄 led_blink.py │ └── 📄 ... ├── 📄 README.md ├── 📄 requirements.tx

Cada carpeta de práctica (`practica_XX_nombre`) contendrá los archivos `.py` relevantes y, si es necesario, un `README.md` específico con instrucciones detalladas o diagramas de conexión.

---

## 🚀 Uso de los Scripts de Python

1.  **Conexión:** Accede a tu Raspberry Pi vía **SSH** (ej. usando PuTTY).
2.  **Clonar:** Clona este repositorio en tu Raspberry Pi:
    ```bash
    git clone [URL-DE-TU-REPOSITORIO]
    cd [NOMBRE-DEL-REPOSITORIO]
    ```
3.  **Ejecución:** Navega a la carpeta de la práctica deseada y ejecuta el script con Python 3:
    ```bash
    cd practica_01_introduccion
    python3 ejemplo_hola_mundo.py
    ```

> ⚠️ **Nota Importante:** Algunos scripts requieren permisos de superusuario para acceder al hardware GPIO. En esos casos, se debe usar `sudo`:
> `sudo python3 script_de_gpio.py`

---

## 🛠️ Dependencias de Python

Si los scripts requieren librerías de Python adicionales a las estándar, estas se listarán en el archivo `requirements.txt`. Puedes instalarlas usando:

```bash
pip3 install -r requirements.txt
