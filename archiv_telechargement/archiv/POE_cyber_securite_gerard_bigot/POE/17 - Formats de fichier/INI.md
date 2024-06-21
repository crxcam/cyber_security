Le format INI (Initialization File) est un format de fichier simple utilisé pour les fichiers de configuration. 

Ces fichiers sont généralement utilisés pour stocker des paramètres et des options pour des logiciels sous Windows et divers systèmes d'exploitation. 

Ils ont été largement utilisés dans les premières versions de Windows et sont encore utilisés aujourd'hui pour des applications spécifiques, bien que d'autres formats tels que XML, JSON, ou YAML soient souvent préférés pour leur flexibilité et leur robustesse.

### Structure d'un fichier INI

Un fichier INI est structuré en sections, chaque section contenant une ou plusieurs clés (ou propriétés) et leurs valeurs associées. Voici les éléments principaux d'un fichier INI :

- **Sections** : Elles regroupent des configurations liées et sont indiquées par un titre entre crochets `[]`.
- **Paires clé-valeur** : À l'intérieur des sections, les configurations spécifiques sont définies par des paires clé-valeur, où la clé et la valeur sont séparées par un signe égal `=`. Les espaces autour du signe égal sont généralement ignorés.
- **Commentaires** : Les commentaires peuvent être ajoutés en préfixant une ligne avec un point-virgule `;` ou parfois un dièse `#`.

### Exemple de fichier INI

```ini
; Ceci est un commentaire
[General]
username = user
password = pass123
level = admin

[Database]
server = localhost
port = 3306
db = mydatabase
timeout = 30
```

Dans cet exemple, il y a deux sections : `[General]` et `[Database]`. Chaque section contient plusieurs paramètres configurés via des paires clé-valeur.

### Caractéristiques du format INI

- **Simplicité** : La syntaxe des fichiers INI est très simple et facile à comprendre, ce qui rend les fichiers INI très accessibles pour les modifications manuelles par les utilisateurs ou les administrateurs.
- **Lisibilité** : Grâce à leur structure claire, les fichiers INI sont lisibles aussi bien par des humains que par des machines.
- **Portabilité** : Les fichiers INI ne dépendent pas d'un système d'exploitation ou d'un langage de programmation spécifique, bien qu'ils soient plus traditionnellement utilisés dans les environnements Windows.

### Utilisations du format INI

Bien que plus ancien et moins flexible que des formats modernes comme JSON ou YAML, le format INI est encore utilisé pour des applications qui nécessitent une configuration simple sans dépendances supplémentaires. Il est également couramment utilisé dans des contextes où la légèreté et la facilité de modification sont prioritaires.

### Limitations

- **Absence de types de données** : Tout est stocké comme des chaînes de caractères, ce qui peut nécessiter des conversions de type dans les applications.
- **Non hiérarchique** : Contrairement à JSON ou XML, les fichiers INI ne supportent pas une structure de données hiérarchique naturelle, ce qui limite leur utilité pour des configurations plus complexes.

En conclusion, le format INI offre une méthode éprouvée pour gérer des configurations de manière simple et directe, bien que ses limitations le rendent moins idéal pour des applications plus avancées ou des données structurées de manière complexe.