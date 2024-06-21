from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse les paramètres de l'URL
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        # Commence à écrire la réponse
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        # Contenu HTML
        message_parts = [
            "<html><head><title>Requête Info</title></head>",
            "<body>",
            "<h1>En-têtes de la Requête</h1>",
            "<ul>",
        ]

        value: str
        for header, value in self.headers.items():
            message_parts.append(f"<li>{header}: {value}</li>")
        message_parts.append("</ul>")

        if query_params:
            message_parts.append("<h2>Paramètres de la Requête</h2>")
            message_parts.append("<ul>")
            for param, values in query_params.items():
                message_parts.append(f"<li>{param}: {values}</li>")
            message_parts.append("</ul>")

        message_parts.append("</body></html>")
        message = "\n".join(message_parts)

        # Envoie le contenu HTML
        _ = self.wfile.write(message.encode("utf-8"))


if __name__ == "__main__":
    server_address = ("", 8000)  # Port 8000
    httpd = HTTPServer(server_address, RequestHandler)
    print("Serveur démarré sur le port 8000...")
    httpd.serve_forever()
