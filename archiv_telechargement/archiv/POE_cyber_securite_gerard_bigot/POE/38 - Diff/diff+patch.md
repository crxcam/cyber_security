Installer le paquet path :  

```
sudo apt install patch
```

La commande `patch` sous Linux est utilisée pour appliquer des modifications encapsulées dans un fichier de différences (diff) à un ou plusieurs fichiers originaux. Elle est très utile pour intégrer des corrections ou des mises à jour à des fichiers de code source, des scripts ou tout document texte. Voici un exemple concret de la façon d'utiliser la commande `patch`.

### Création d'un fichier de différences

Imaginons que vous avez un fichier nommé `original.txt` contenant le texte suivant :

```
Bonjour,
Ceci est un fichier texte exemple.
Au revoir.
```

Vous modifiez ce fichier pour corriger une faute de frappe ou changer un peu le contenu, résultant en un nouveau fichier `modifie.txt` :

```
Bonjour,
Ceci est un fichier texte exemple modifié.
Au revoir et à bientôt.
```

Pour créer un fichier de différences, vous pouvez utiliser la commande `diff` :

```bash
diff -u original.txt modifie.txt > changes.diff
```

Le fichier `changes.diff` contiendra les différences entre les deux fichiers sous la forme suivante :

```diff
--- original.txt
+++ modifie.txt
@@ -1,3 +1,3 @@
 Bonjour,
-Ceci est un fichier texte exemple.
-Au revoir.
+Ceci est un fichier texte exemple modifié.
+Au revoir et à bientôt.
```

### Application du patch

Pour appliquer ces modifications au fichier `original.txt` en utilisant le fichier de différences `changes.diff`, tu utiliserais la commande `patch` comme suit :

```bash
patch original.txt changes.diff
```

Cette commande met à jour `original.txt` avec les modifications contenues dans `changes.diff`.

### Vérification

Après avoir appliqué le patch, `original.txt` contiendra :

```
Bonjour,
Ceci est un fichier texte exemple modifié.
Au revoir et à bientôt.
```

### Conseils supplémentaires

- Si vous recevez un message d'erreur indiquant que le patch ne peut pas trouver le fichier à patcher, vous pouvez utiliser l'option `-p` pour ignorer certains niveaux de répertoires dans les chemins spécifiés dans le fichier de diff.
- Utilise `patch --dry-run` pour simuler l'application du patch sans modifier les fichiers, ce qui permet de vérifier ce qui se passera.

Cet exemple montre comment créer et appliquer un fichier de différences, facilitant la distribution et l'application de modifications dans des environnements où plusieurs versions d'un fichier peuvent exister.