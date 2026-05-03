from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)


import os
client = OpenAI()

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_input = request.form["content"]

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un experto en marketing digital que ayuda a negocios a crear contenido para redes sociales que atrae clientes, genera interés y convierte en ventas. Responde con ideas claras, gancho (hook), estructura del contenido y llamada a la acción."
                },
                {
                    "role": "user",
                    "content": user_input + " Dame: 1) Idea de contenido 2) Hook 3) Guión 4) CTA para vender"
                }
            ]
        )

        response = completion.choices[0].message.content

    return render_template("index.html", response=response)

if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
