# pip install flask
# sudo apt install python3-flask

from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        try:
            response = requests.get(url)
            headers = response.headers
            request_headers = response.request.headers
            status_code = response.status_code
            return render_template_string(
                """
                <h2>Réponse</h2>
                <p>Status Code: {{status_code}}</p>
                <h3>En-têtes de la requête:</h3>
                <ul>{% for header, value in request_headers.items() %}
                    <li>{{ header }}: {{ value }}</li>
                {% endfor %}</ul>
                <h3>En-têtes de la réponse:</h3>
                <ul>{% for header, value in headers.items() %}
                    <li>{{ header }}: {{ value }}</li>
                {% endfor %}</ul>
                <a href="/">Nouvelle recherche</a>
            """,
                headers=headers,
                request_headers=request_headers,
                status_code=status_code,
            )
        except requests.exceptions.RequestException as e:
            return f"Erreur lors de la requête: {e}"
    return """
        <form method="post">
            URL: <input type="text" name="url"><br>
            <input type="submit" value="Envoyer">
        </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
