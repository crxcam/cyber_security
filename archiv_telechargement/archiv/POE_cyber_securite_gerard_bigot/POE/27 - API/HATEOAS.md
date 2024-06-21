# **HATEOAS** (Hypermedia as the Engine of Application State) est un concept clé dans l'architecture REST (Representational State Transfer) pour les services web

Ce principe suggère que les interactions avec une API web doivent être pilotées par des hypermédias, c’est-à-dire par des liens fournis dynamiquement dans les réponses de l'API.

Voici quelques points essentiels à comprendre sur HATEOAS :

1. **Autonomie du Client** :  
   En utilisant HATEOAS, le client n'a pas besoin de connaître à l'avance comment interagir avec l'API. Au lieu de cela, il navigue à travers les liens fournis dynamiquement dans les réponses, ce qui lui permet de découvrir les actions possibles au fur et à mesure.

2. **Découverte de l'API** :  
   Les réponses de l'API incluent des liens vers d'autres actions ou ressources pertinentes. Cela signifie que le client peut découvrir les fonctionnalités de l'API en examinant les hyperliens fournis, sans référence à une documentation externe.

3. **Évolutivité** :  
   Grâce à HATEOAS, les développeurs peuvent modifier les URI des ressources sans casser les clients existants. Les clients découvrent les URI à travers les interactions plutôt que de les coder en dur.

4. **Exemple** :  
   Supposons une API pour un système de gestion de livres. Une réponse à une requête sur un livre spécifique pourrait inclure des liens pour "acheter le livre", "lire un résumé", "voir les critiques", etc. Ces liens guident le client sur les actions possibles sans nécessiter une connaissance préalable des URIs.

HATEOAS renforce l'indépendance entre le client et le serveur et encourage une plus grande flexibilité et maintenabilité dans le développement des applications web.
