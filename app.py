from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)

client = OpenAI()

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_input = request.form["prompt"]

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un experto en marketing digital especializado en redes sociales. Creas contenido atractivo, claro y enfocado en generar clientes reales para negocios. Respondes con estructuras claras, prácticas y listas para usar."
                },
                {
                    "role": "user",
                    "content": f"""
                    Tengo este negocio: {user_input}

                    Crea un calendario de contenido para 7 días (lunes a domingo).

                    Para cada día incluye:
                    - Tipo de contenido (reel, historia, post, etc.)
                    - Idea de contenido
                    - Hook (gancho)
                    - Guión corto
                    - CTA para vender

                    Hazlo claro, ordenado y separado por días.
                    """
                }
            ]
        )

        response = completion.choices[0].message.content

    return render_template("index.html", response=response)

# NO usar app.run()
