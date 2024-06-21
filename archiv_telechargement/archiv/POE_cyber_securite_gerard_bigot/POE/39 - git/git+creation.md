sudo apt intall git 

### 1. Création d'un nouveau répertoire pour votre dépôt

Ouvrir un terminal et créer un nouveau dossier qui servira de dépôt Git :

```bash
mkdir mon_projet
cd mon_projet
```

### 2. Initialisation du dépôt Git

Une fois dans le dossier de votre projet, initialiser le dépôt Git :

```bash
git init
```

Cette commande crée un nouveau sous-dossier `.git` dans votre dossier `mon_projet`, où toutes les données de suivi de Git sont stockées.

### 3. Création d'un fichier

Crée votre premier fichier dans ce dépôt. Par exemple, vous pouvez créer un fichier `README.md` qui contiendra des informations de base sur votre projet :

```bash
echo "# Mon Projet" > README.md
```

### 4. Suivi des fichiers avec Git

Pour commencer à suivre le fichier avec Git, vous devez l'ajouter à l'index (staging area) :

```bash
git add README.md
```

### 5. Enregistrement des modifications dans le dépôt

Enregistrez vos modifications dans l'historique du dépôt avec un commit :

```bash
git commit -m "Ajout du fichier README initial"
```

Le message du commit (après `-m`) est important car il explique ce que fait le commit. Il est une bonne pratique de rendre ce message aussi descriptif que possible pour chaque commit.

### 6. Vérification du statut

Vous pouvez vérifier le statut de ton dépôt à tout moment avec :

```bash
git status
```

Cette commande vous montrera les fichiers non suivis, modifiés, ou prêts à être commités.

### 7. Clonage d'un repos distant

Vous pouvez récupérer les contenu d'un repos distant en effectuant al commande suivante : 

```bash
git clone 'https://github.com/microsoft/vscode.git' vscode
```

Un répertoire vscode va apparaître contenant une copie des données distantes.

### 8. Voir l'historique des commits

Pour voir l'historique des modifications, utilise :

```bash
git log
```

Cette commande affiche la liste des commits, y compris l'auteur, la date et le message de chaque commit.

### 9. Mise à jour du repos local

La mise à jour du repos local avec le contenu distant, se fait avec la commande : 

```bash
git clean -fdx ; git checkout .
```

Les modifications locales (dûes ou pas à la compilation, par exemple) auront été rincées au préalable.

### Conseils supplémentaires

- **.gitignore :** Si vosu avez des fichiers ou dossiers que vous ne voulez pas suivre avec Git (par exemple, des fichiers binaires, des logs, ou des dossiers de dépendances comme `node_modules`), vous devez les lister dans un fichier nommé `.gitignore`.
- **Branches :** Pensez à utiliser des branches pour isoler le développement de différentes fonctionnalités.

Ces étapes de base vous permettront de démarrer avec Git pour un nouveau projet. Si vous souhaitez pousser votre dépôt local vers un dépôt distant (comme GitHub, GitLab, etc.), il y aura quelques étapes supplémentaires pour configurer cela.