# 🔐 Simulación Máquina Enigma

Este proyecto es una **simulación de la máquina Enigma**, el famoso dispositivo de cifrado utilizado por Alemania durante la Segunda Guerra Mundial.  
El objetivo es recrear su funcionamiento básico en Python, permitiendo al usuario **cifrar y descifrar mensajes** mediante la configuración de rotores y reflectores.

---

## 📂 Estructura del repositorio

- `.gitignore` → Archivos y carpetas ignorados por Git.  
- `LICENSE` → Licencia MIT, que permite usar y modificar libremente el código.  
- `README.md` → Documento de presentación del proyecto.  
- `rotors/` → Archivos .txt de los rotores usados en el proyecto. Por defecto vienen los rotores típicos de la máquina real.
- - `output/` → Contiene los archivos de output generados por el programa: cifrado.txt y desencriptado.txt.

---

## 🚀 Características principales

- Simulación del **cifrado y descifrado** de mensajes.  
- Configuración de **rotores** para personalizar la máquina.  
- Código abierto bajo licencia **MIT**.

---

## 🛠️ Requisitos

- Python 3.8 o superior  
- Las librerias importadas han sido time y re.

---

## ▶️ Uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/songorren02/AA1.2_enigma.git
   cd AA1.2_enigma
2. Ejecuta el programa main.py:
   python enigma/main.py
3. Primero cifra el mensaje para poder descifrarlo.
   Si hay un mensaje previamente cifrado se va a sobreescribir y perderás el mensaje.
