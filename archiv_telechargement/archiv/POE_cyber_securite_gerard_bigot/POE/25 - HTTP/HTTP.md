[HTTP](https://developer.mozilla.org/fr/docs/Web/HTTP/Overview) (HyperText Transfer Protocol) est le protocole de base utilisé par le World Wide Web. 

Développé par Tim Berners-Lee en 1989, il définit les règles de transmission des fichiers (texte, images graphiques, son, vidéo et autres fichiers multimédias) sur le web.

 En conséquence, chaque transaction sur le web implique HTTP, ce qui en fait l'un des protocoles les plus utilisés sur Internet.

### Comment fonctionne HTTP

HTTP est un protocole de requête-réponse dans le modèle de calcul client-serveur. Un client, généralement un navigateur web, ouvre une connexion et demande des données à un serveur ; le serveur traite ensuite la demande et renvoie une réponse au client. Les étapes de base d'une transaction HTTP sont :

1. **Ouvrir une connexion TCP** : HTTP utilise TCP/IP pour garantir que les données sont livrées de bout en bout entre le client et le serveur.
2. **Envoyer une requête HTTP** : Le client envoie un message de requête au serveur. Cette requête comprend une méthode (comme GET, POST, etc.), l'URI (Uniform Resource Identifier), la version du protocole, suivie d'en-têtes de requête optionnels et du contenu du corps.
3. **Recevoir la réponse HTTP** : Le serveur traite la demande et renvoie une réponse au client. Cette réponse contient un code d'état (comme 200 pour succès ou 404 pour non trouvé), la version du protocole, suivie des en-têtes de réponse et du corps du message.
4. **Fermer la connexion ou la garder ouverte pour d'autres requêtes** : Par défaut, HTTP 1.1 maintient la connexion ouverte pour d'éventuelles autres requêtes mais peut être instruit de la fermer après l'achèvement de la réponse.

### Composants clés de HTTP

- **Méthodes** : HTTP définit un ensemble de méthodes de requête pour indiquer l'action souhaitée à effectuer. Les exemples incluent :
  - `GET` : Récupérer des informations de la source spécifiée.
  - `POST` : Soumettre des données à traiter à la ressource spécifiée.
  - `PUT` : Mettre à jour des données à la ressource spécifiée.
  - `DELETE` : Supprimer la ressource spécifiée.

- **Codes d'état** : Ces codes indiquent au client le statut de la requête.
  - `200 OK` : La requête a réussi.
  - `404 Not Found` : La ressource demandée n'est pas disponible.
  - `500 Internal Server Error` : Le serveur a rencontré une condition inattendue.

- **En-têtes** : Les en-têtes HTTP permettent au client et au serveur de transmettre des informations supplémentaires avec la requête ou la réponse. Les exemples incluent :
  - `Content-Type` : Spécifie le type de média de la ressource.
  - `Content-Length` : La longueur du corps de la réponse en octets.
  - `Authorization` : Contient les informations d'identification pour authentifier le client auprès du serveur.

- **Version** : Indique la version de HTTP, par exemple, HTTP/1.1.

### Sécurité et HTTP

Étant donné que HTTP lui-même n'est pas sécurisé, HTTPS (HTTP Secure) a été développé pour permettre l'autorisation et les transactions sécurisées. En utilisant HTTPS, les données envoyées et reçues sont chiffrées, ce qui empêche les transactions d'être interceptées par toute personne qui pourrait écouter.

Dans les applications web modernes, HTTP est omniprésent, servant de pilier pour la communication de données. Comprendre HTTP est crucial pour le développement web, car cela influence de nombreux aspects de la conception et de l'interaction avec les applications web.