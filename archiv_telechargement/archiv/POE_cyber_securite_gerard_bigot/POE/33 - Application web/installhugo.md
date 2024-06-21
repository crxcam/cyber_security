Hugo est un générateur de sites statiques très populaire écrit en golang. 

Voici un résumé des étapes pour ceux qui veulent créer rapidement leur propre site avec Hugo :

1. **Installer Hugo** :
   - **macOS** : Utiliser Homebrew avec la commande `brew install hugo`.
   - **Windows** : Utiliser Chocolatey avec la commande `choco install hugo -confirm`.
   - **Linux** (exemple pour Ubuntu) : Utiliser APT avec `sudo apt-get install hugo`.

2. **Créer un nouveau site Hugo** :
   - Exécuter `hugo new site my-hugo-site` dans le terminal pour créer un nouveau dossier nommé `my-hugo-site` qui contient la structure de base d'un site Hugo.

3. **Naviguer dans le répertoire du site** :
   - Changer de répertoire avec `cd my-hugo-site`.

4. **Ajouter un thème** :
   - Utiliser Git pour ajouter un thème, par exemple "Ananke", avec `git init` et `git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke`.
   - Ajouter le thème à la configuration du site, soit en TOML (`theme = "ananke"`) dans `config.toml`, soit en YAML (`theme: "ananke"`) dans `config.yaml`.

5. **Ajouter du contenu** :
   - Créer un nouveau post avec `hugo new posts/my-first-post.md` et éditer ce fichier dans un éditeur de texte pour y ajouter du contenu. Hugo utilise Markdown pour la création de contenu.

6. **Démarrer le serveur Hugo** :
   - Lancer le serveur local intégré à Hugo avec `hugo server` pour voir le site en action. Par défaut, le site sera accessible à `http://localhost:1313/`.

7. **Construire le site** :
   - Lorsque prêt, utiliser `hugo` pour générer les pages statiques qui seront placées dans le répertoire `public/`. Ces fichiers sont ceux qui seront déployés sur un serveur web.

Tu as maintenant une base solide pour personnaliser ton thème, ajouter plus de contenu et, éventuellement, déployer ton site sur un serveur en direct. La documentation complète de Hugo peut t'aider à traverser des configurations et des utilisations plus avancées. Si tu as d'autres questions ou besoin d'assistance supplémentaire, n'hésite pas à demander !