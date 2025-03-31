# Manual del Proyecto: Chatsito

Este proyecto simula un sistema de chat estilo WhatsApp entre el usuario y un modelo de lenguaje local (LLM) usando **DeepSeek R1** cargado desde **LM Studio**. Se comunica con un backend en Python usando Flask y una interfaz frontend responsiva en HTML, CSS y JavaScript.

---

## ✅ Tecnologías Utilizadas

| Componente | Tecnología |
|------------|-------------|
| Modelo LLM | DeepSeek R1 (vía LM Studio) |
| Backend    | Python + Flask |
| Frontend   | HTML, CSS, JavaScript |
| Markdown y Código | marked.js + highlight.js |

---

## 📁 Estructura del Proyecto

```
Chatsito/
├── back/                 # Backend Flask + venv
│   └── app.py           # API que se comunica con LM Studio
├── front/                # Interfaz web tipo WhatsApp
│   ├── index.html       # Estructura HTML
│   ├── styles.css       # Estilos personalizados
│   └── script.js        # Lógica JS + animaciones
└── README.md             # Este manual
```

---

## 🚀 Configuración y Ejecución

### 1. Requisitos previos
- Tener Python 3.10+
- Tener instalado LM Studio con un modelo cargado (ej. `deepseek-r1-distill-llama-8b`)
- LM Studio debe estar corriendo en `http://localhost:1234`

### 2. Requisitos mínimos del sistema para DeepSeek R1 (local)

| Componente      | Recomendado                    |
|------------------|-------------------------------|
| CPU              | Intel i5 o superior (6 núcleos) |
| RAM              | **16 GB mínimo**               |
| GPU (opcional)   | **NVIDIA RTX 3060 o mejor** (12 GB VRAM) |
| Almacenamiento   | 8-10 GB disponibles para el modelo |
| SO               | Windows, macOS o Linux         |

> También puede funcionar en CPU, pero será más lento.

### 3. Configurar entorno virtual en `back/`
```bash
cd back
python -m venv venv
venv\Scripts\activate      # en Windows
pip install flask flask-cors requests
```

### 4. Ejecutar backend
```bash
python app.py
# Corre en http://localhost:5000
```

### 5. Abrir frontend
Solo abre `front/index.html` con tu navegador (doble clic o VS Code Live Server).

---

## 🤖 Comportamiento del Chat
- Muestra el mensaje del usuario
- Luego simula "DeepSeek está escribiendo..." con animación
- Renderiza la respuesta con Markdown y resaltado de código

---

## 📊 Características Especiales

### 🌟 Formateo enriquecido
- Se usa `marked.js` para convertir Markdown en HTML
- Se usa `highlight.js` para mostrar código colorido (Python, JS, etc.)

### ⏳ Indicador de escritura
- Se muestra un texto animado tipo WhatsApp: `DeepSeek está escribiendo...`
- Al llegar la respuesta real, se reemplaza por el mensaje

---

## 🎓 Aprendizajes y extensiones posibles
- Se pueden agregar respuestas por voz (TTS)
- O guardar el historial del chat en localStorage o SQLite
- Puedes cambiar el modelo usado en LM Studio

---

## 👍 Crédito

Desarrollado por: **Jonathan Alexander Sánchez Barrios**  
IA Local: **DeepSeek R1 con LM Studio**  
Frontend inspirado en **WhatsApp Web**

---

© 2025 - Proyecto educativo y experimental con LLMs locales.