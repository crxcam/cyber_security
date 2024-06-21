from flask import Flask, render_template, abort
from flask import safe_join

# from werkzeug.utils import safe_join
# from werkzeug.security import safe_join

import markdown
import os

app = Flask(__name__)


@app.route("/")
def list_markdown_files():
    root_dir = os.path.abspath("../../../POE/")
    markdown_files = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                # Construction du chemin relatif sécurisé
                file_path = os.path.relpath(os.path.join(subdir, file), root_dir)
                markdown_files.append(file_path)
    return render_template("index.html", files=markdown_files)


@app.route("/files/<path:path>")
def file_display(path):
    root_dir = os.path.abspath("../../../POE/")

    # Utilisation de safe_join pour sécuriser le chemin du fichier
    md_path = safe_join(root_dir, path)

    if not os.path.exists(md_path) or not md_path.endswith(".md"):
        abort(404)

    with open(md_path, "r", encoding="utf-8") as f:
        #    content = markdown.markdown(f.read())
        content = markdown.markdown(f.read(), extensions=["nl2br"])

    return render_template("file.html", content=content)


if __name__ == "__main__":
    app.run(debug=True)
