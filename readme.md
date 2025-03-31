# 🟢 Manual del Proyecto "Chatsito" con DeepSeek R1 + LM Studio

Este proyecto implementa una interfaz estilo WhatsApp que permite interactuar con el modelo de lenguaje **DeepSeek R1 (distill-llama-8b)** corriendo localmente a través de **LM Studio**, utilizando un backend en **Flask** y frontend en HTML/CSS/JS.

---

## 📁 Estructura del Proyecto

```
CHATSITO/
├── back/                 ← Backend en Python (Flask + LM Studio)
│   ├── app.py           ← Servidor Flask
│   ├── venv/            ← Entorno virtual Python
│   └── requirements.txt
│
├── front/                ← Interfaz estilo WhatsApp
│   ├── index.html       ← HTML principal
│   ├── styles.css       ← Estilo del chat
│   └── script.js         ← Lógica JS para enviar mensajes
```

---

## 🔧 Requisitos

- Python 3.10+
- [LM Studio](https://lmstudio.ai) instalado con modelo `deepseek-r1-distill-llama-8b`
- Flask y dependencias (ver instalación)

---

## ⚙️ Instalación del Backend (carpeta `back/`)

```bash
cd back
python -m venv venv
venv\Scripts\activate  # En Windows
pip install flask flask-cors openai
pip freeze > requirements.txt
```

---

## 🚀 Ejecutar el Servidor

1. Abre LM Studio y carga el modelo `deepseek-r1-distill-llama-8b`.
2. Asegúrate de que el servidor esté activo en `http://localhost:1234`.
3. Desde la carpeta `back/`, ejecuta:

```bash
python app.py
```

> El backend estará escuchando en `http://localhost:5000/chat`

---

## 🖼 Interfaz de Usuario (carpeta `front/`)

Abre `index.html` en tu navegador. La interfaz permite:
- Escribir mensajes al estilo WhatsApp
- Enviar mensajes al backend
- Recibir respuestas del modelo

---

## 🔁 Funcionamiento Interno

1. JS capta el mensaje del usuario y hace `POST` a `http://localhost:5000/chat`
2. Flask recibe el mensaje, lo agrega al historial y consulta a LM Studio (vía API OpenAI-compatible).
3. El modelo responde y el backend filtra bloques `<think>...</think>`
4. El frontend muestra la respuesta tipo burbuja de chat

---

## 🧠 Personalización del Asistente

Puedes modificar el `system prompt` en `app.py`:
```python
messages = [{
    "role": "system",
    "content": (
        "Eres un asistente que responde en español, sin mostrar razonamientos internos ni usar etiquetas <think>."
    )
}]
```

---

## 🧽 Mejoras Posibles

- Guardar historial en un archivo `.txt`
- Implementar reinicio de conversación desde el frontend
- Agregar soporte para markdown o código con resaltado
- Convertir en app de escritorio (Tkinter o Electron)

---

## 🧪 Ejemplo de mensaje

Usuario:
```
como hacer un hola mundo en python?
```
Respuesta:
```
Claro, aquí tienes:
```python
print("Hola Mundo")
```
```

---

## 🔐 100% Offline

Este proyecto es **100% local y privado**:
- El modelo corre offline en tu PC
- Flask y JS solo usan `localhost`
- No se envía información a internet

---

## 📄 Licencia

Uso personal o educativo. Puedes modificarlo libremente.

---

_Desarrollado por: Jonathan A. Sanchez y DeepSeek + Flask + HTML/CSS/JS_

