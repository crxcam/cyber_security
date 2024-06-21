from flask import Flask, request, render_template_string
import ssl
import socket
from datetime import datetime

app = Flask(__name__)


def get_cert_details(hostname):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
    # 443 est le port standard pour HTTPS
    conn.connect((hostname, 443))
    cert = conn.getpeercert()

    issuer = dict(x[0] for x in cert["issuer"])
    issuer_common_name = issuer["commonName"]
    valid_from = datetime.strptime(cert["notBefore"], "%b %d %H:%M:%S %Y %Z").strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    valid_to = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z").strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return {
        "issuer_common_name": issuer_common_name,
        "valid_from": valid_from,
        "valid_to": valid_to,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        hostname = request.form["url"]
        try:
            # Extraire le nom d'hôte sans les parties de protocole/chemin
            if hostname.startswith("http://") or hostname.startswith("https://"):
                from urllib.parse import urlparse

                hostname = urlparse(hostname).hostname
            cert_details = get_cert_details(hostname)
            return render_template_string(
                """
                <h2>Détails du Certificat</h2>
                <ul>
                    <li>Émetteur: {{ cert_details['issuer_common_name'] }}</li>
                    <li>Valide à partir de: {{ cert_details['valid_from'] }}</li>
                    <li>Valide jusqu'à: {{ cert_details['valid_to'] }}</li>
                </ul>
                <a href="/">Nouvelle recherche</a>
            """,
                cert_details=cert_details,
            )
        except Exception as e:
            return f"Erreur lors de la récupération du certificat: {e}"
    return """
        <form method="post">
            URL: <input type="text" name="url"><br>
            <input type="submit" value="Envoyer">
        </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
