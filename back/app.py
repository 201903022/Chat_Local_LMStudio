from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import re
app = Flask(__name__)
CORS(app)  # Permitir acceso desde el frontend local

# Conexión con LM Studio local
client = OpenAI(
    base_url="http://localhost:1234/v1",  # Puerto de LM Studio
    api_key="lm-studio"  # Valor cualquiera, no se valida
)

# Historial de conversación (persistente mientras el servidor esté activo)
messages = [{
    "role": "user",
    "content": "Responde directamente a las preguntas en español, sin explicar lo que estás haciendo internamente. No describas tu razonamiento, solo responde como un chat normal."
}]

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "Mensaje vacío"}), 400

    # Agrega mensaje del usuario al historial
    messages.append({"role": "user", "content": user_input})

    # Llama al modelo a través de LM Studio
    response = client.chat.completions.create(
        model="deepseek-r1-distill-llama-8b",
        messages=messages
    )

    # Extrae la respuesta
    reply = response.choices[0].message.content.strip()
    reply = re.sub(r"<think>.*?</think>", "", reply, flags=re.DOTALL).strip()

    # Agrega respuesta al historial
    messages.append({"role": "assistant", "content": reply})

    # Devuelve la respuesta al frontend
    return jsonify({"response": reply})


if __name__ == "__main__":
    app.run(port=5000)
