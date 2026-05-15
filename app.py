from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)

client = OpenAI()

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_input = request.form["prompt"]

        print("Recibido:", user_input)

        completion = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
Eres un experto en marketing digital especializado en redes sociales.

Tu trabajo es crear calendarios de contenido para Instagram que ayuden a negocios locales a atraer clientes y vender más.

Haz el contenido:
- Claro
- Ordenado
- Profesional
- Fácil de leer
- Separado por días
- Con emojis moderados

Para cada día incluye:
- Tipo de contenido
- Idea de contenido
- Hook (gancho)
- Guión corto
- CTA para vender
"""
                },
                {
                    "role": "user",
                    "content": f"""
Tengo este negocio:
{user_input}

Crea un calendario de contenido para 7 días (lunes a domingo).
"""
                }
            ]
        )

        response = completion.choices[0].message.content

        print("RESPUESTA IA:")
        print(response)

    return render_template("index.html", response=response)
