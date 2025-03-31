let dots = 0;

// Animación de escritura con puntos
function animateTyping() {
  const typingEl = document.getElementById("typing-indicator");
  if (!typingEl) return;

  dots = (dots + 1) % 4;
  typingEl.textContent = "DeepSeek está pensando" + ".".repeat(dots);
  setTimeout(animateTyping, 500);
}

async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const userMsg = input.value.trim();
  if (!userMsg) return;

  // Mostrar mensaje del usuario
  chatBox.innerHTML += `<div class="message user">${userMsg}</div>`;
  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;

  // Mostrar mensaje de "escribiendo"
  const writing = document.createElement("div");
  writing.className = "message bot typing";
  writing.id = "typing-indicator";
  writing.textContent = "DeepSeek está escribiendo";
  chatBox.appendChild(writing);
  chatBox.scrollTop = chatBox.scrollHeight;

  animateTyping(); // inicia la animación

  try {
    const res = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userMsg })
    });

    const data = await res.json();
    const botMsg = data.response;

    // Eliminar indicador
    document.getElementById("typing-indicator")?.remove();

    // Convertir Markdown a HTML
    const html = marked.parse(botMsg);
    chatBox.innerHTML += `<div class="message bot">${html}</div>`;

    // Resaltar código
    document.querySelectorAll('pre code').forEach(block => {
      hljs.highlightElement(block);
    });

    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("typing-indicator")?.remove();
    chatBox.innerHTML += `<div class="message bot">❌ Error al obtener respuesta.</div>`;
  }
}
