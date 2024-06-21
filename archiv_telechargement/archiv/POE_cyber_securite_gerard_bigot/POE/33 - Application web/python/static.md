#sudo apt install python3-flask python3-markdown
#pip install flask markdown

Exécutez votre application en lançant `app.py` :

```bash
python app.py
```

Ouvrez un navigateur et allez à l'adresse `http://127.0.0.1:5000/`. Vous devriez voir la liste des fichiers Markdown dans le répertoire spécifié, et vous pourrez cliquer sur chaque lien pour voir son contenu formaté en HTML.

### Conclusion

Cette application simple vous permet d'afficher le contenu des fichiers Markdown stockés dans un répertoire et ses sous-répertoires. Elle utilise Flask pour le serveur web et Python-Markdown pour le rendu des fichiers Markdown en HTML. Vous pouvez étendre cette application de base de plusieurs façons, comme en ajoutant des styles CSS pour améliorer la mise en page ou en implémentant des fonctionnalités supplémentaires selon vos besoins.
