#pip install Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulons une base de données simple avec un dictionnaire
data = {
    "items": [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"}
    ]
}

# Route pour obtenir tous les items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# Route pour obtenir un item par son ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data['items'] if item['id'] == item_id), None)
    if item is not None:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Route pour ajouter un nouvel item
@app.route('/items', methods=['POST'])
def add_item():
    if request.is_json:
        item = request.get_json()
        data['items'].append(item)
        return jsonify(item), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)