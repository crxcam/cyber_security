Créer une API REST simple avec Flask est un excellent moyen de comprendre comment les applications web modernes peuvent gérer des données via HTTP. 

Voici un exemple de base pour démarrer avec une API REST en utilisant Flask qui gère des données en mémoire sans utiliser de base de données.

### Prérequis

Assurez-vous d'avoir Python installé sur votre machine. Vous aurez également besoin de Flask. Si Flask n'est pas installé, vous pouvez l'installer via pip :

```bash
pip install Flask
```

### Création de l'Application Flask

Voici les étapes pour créer une petite API REST qui permet de récupérer et d'ajouter des données.

1. **Initialisation de l'Application** :
   Créez un fichier nommé `app.py`.

2. **Écrire le Code de l'Application** :
   Voici le contenu pour `app.py` qui crée une API avec Flask.

```python
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
```

### Explication du Code

- **`/items` GET** : Renvoie la liste de tous les items.
- **`/items/<int:item_id>` GET** : Renvoie un item spécifique par son ID.
- **`/items` POST** : Ajoute un nouvel item à la liste. Attend des données en format JSON.

### Test de l'API

Pour tester votre API, vous pouvez utiliser des outils comme [Postman](https://www.postman.com/) ou [curl](https://curl.se/) dans votre terminal. Voici comment vous pourriez tester les endpoints avec curl :

- **GET tous les items** :
  ```bash
  curl -X GET http://localhost:5000/items
  ```

- **GET un item par ID** :
  ```bash
  curl -X GET http://localhost:5000/items/1
  ```

- **POST ajouter un nouvel item** :
  ```bash
  curl -X POST http://localhost:5000/items -H "Content-Type: application/json" -d '{"id": 3, "name": "Item 3"}'
  ```

Lorsque vous exécuterez `app.py` et utiliserez ces commandes curl ou Postman, vous devriez voir les réponses correspondantes basées sur les données gérées par votre API Flask.

### Conclusion

Cet exemple de base montre comment mettre en place une API REST simple avec Flask. C'est un bon point de départ pour développer des applications web plus complexes qui nécessitent des interactions backend via des API.