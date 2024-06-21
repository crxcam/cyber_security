Le format JSON (JavaScript Object Notation) est un format de données léger destiné à l'échange de données entre serveurs et clients ou entre différents programmes informatiques. 

Basé sur la syntaxe des objets JavaScript, JSON est cependant indépendant du langage de programmation, ce qui le rend largement utilisé dans de nombreux langages de développement grâce à sa simplicité et sa facilité de mise en œuvre.

### Structure de JSON

Le format JSON est construit à partir de deux structures de base :

1. **Des paires clé/valeur** : JSON est composé de paires clé/valeur, où la clé est toujours une chaîne de caractères, et la valeur peut être une chaîne de caractères, un nombre, un objet JSON, un tableau JSON, un booléen (true ou false) ou null.
2. **Des listes ordonnées de valeurs** : Connu sous le nom de tableau JSON, il s'agit d'une liste ordonnée de valeurs (qui peuvent être de n'importe quel type de données JSON).

### Exemple de JSON

Voici un exemple simple de données structurées en JSON :

```json
{
  "nom": "Dupont",
  "age": 25,
  "estEtudiant": false,
  "cours": [
    "Informatique",
    "Mathématiques",
    "Physique"
  ],
  "adresse": {
    "rue": "123 rue de Paris",
    "ville": "Paris",
    "codePostal": 75000
  }
}
```

### Caractéristiques de JSON

- **Lisibilité humaine** : Les données JSON sont faciles à lire et à comprendre pour les humains.
- **Facilité de parsing** : JSON est facile à analyser en objets natifs dans la plupart des langages de programmation, ce qui le rend idéal pour les API de services web.
- **Légèreté** : Par rapport à d'autres formats de données comme XML, JSON est moins verbeux et plus compact, ce qui réduit la quantité de bande passante utilisée lors du transfert de données.

### Utilisation de JSON

JSON est utilisé dans de nombreuses applications web et mobiles pour transférer des données entre le client et le serveur. Il est également utilisé pour la configuration et le stockage de données en raison de sa structure claire et de sa facilité d'accès aux données.

En résumé, JSON est un format de données universellement reconnu pour sa simplicité, sa légèreté et sa capacité à s'intégrer facilement dans des applications de toutes sortes.