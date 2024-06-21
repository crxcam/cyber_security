XML (eXtensible Markup Language) est un langage de balisage qui permet de décrire des données de manière structurée. 

Comme son nom l'indique, il est extensible, ce qui signifie que les développeurs peuvent définir leurs propres éléments de balisage pour répondre aux besoins spécifiques de leurs applications. 

XML est largement utilisé pour le stockage, la transmission et la description de données structurées sur Internet et dans de nombreux autres contextes.

### Structure de XML

La structure de XML est hiérarchique et commence avec un élément racine unique sous lequel tous les autres éléments sont imbriqués. Voici les composants clés de XML :

- **Éléments** : Les éléments sont les composants de base de XML et sont définis par des balises qui peuvent contenir du texte, d'autres balises, ou être vides. Les balises sont toujours entourées de chevrons, par exemple `<nom>` et `</nom>` pour une balise ouvrante et une balise fermante.
- **Attributs** : Les attributs fournissent des informations supplémentaires sur les éléments. Ils sont toujours situés dans la balise ouvrante d'un élément et se présentent sous la forme de paires clé/valeur, comme `type="texte"`.
- **Déclaration XML** : Les documents XML peuvent commencer par une déclaration qui spécifie la version XML et l'encodage du texte, par exemple `<?xml version="1.0" encoding="UTF-8"?>`.
- **Espaces de noms** : XML permet d'utiliser des espaces de noms pour éviter les conflits entre éléments qui ont le même nom mais des significations différentes.

### Exemple de XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<utilisateur>
  <nom>Jean Dupont</nom>
  <email>jean.dupont@example.com</email>
  <adresse>
    <rue>123 rue de Paris</rue>
    <ville>Paris</ville>
    <codePostal>75001</codePostal>
  </adresse>
</utilisateur>
```

### Caractéristiques de XML

- **Extensibilité** : Les utilisateurs peuvent créer leurs propres balises et structures adaptées à leurs besoins spécifiques.
- **Interopérabilité** : XML facilite l'échange de données entre systèmes hétérogènes.
- **Validation** : XML peut être validé contre des schémas XML (XSD) pour s'assurer que les données respectent un format prédéfini et des règles spécifiques.
- **Transformabilité** : Avec des outils comme XSLT (eXtensible Stylesheet Language Transformations), XML peut être transformé en d'autres formats de données ou en documents pour l'affichage, comme HTML.

### Utilisation de XML

XML est utilisé dans une grande variété d'applications, notamment :

- **Web Services** : De nombreux services web utilisent XML pour l'échange de messages, comme SOAP (Simple Object Access Protocol).
- **Configuration et spécifications** : De nombreux logiciels utilisent XML pour configurer des applications ou décrire des interfaces de programmation.
- **Interopérabilité entre les entreprises** : XML est fréquemment utilisé pour l'échange de données d'affaires, notamment dans les domaines de la finance, de l'assurance, et de la logistique.

XML offre une grande flexibilité et est une pierre angulaire de nombreux systèmes d'échange de données, même si dans certains contextes, comme les services web, il a été partiellement supplanté par des formats plus légers tels que JSON.