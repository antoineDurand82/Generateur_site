# Generateur_site

## Projet

Nous devions créer un programme capable de prendre un dossier possédant des fichiers en markdown et de les transformer en fichiers html dans un autre dossier pour les fichiers html.

### Le programme

Comme écrit dans le ![requirements](./requirements.txt) vous allez avoir besoin du package ![markdown2](https://github.com/trentm/python-markdown2)
Vous pouvez l'installer avec les commandes suivantes:

```
pip install -r requirement.txt
```

Pour utiliser le programme vous allez avoir besoin de la ligne de commande qui suit:

```
main.py -i markdown -o html
```

On appelle le programme avec `main.py`.
Voici les arguments que l'on peut passer dans notre commande:

-i, --input-directory | chemin du dossier des fichiers markdown (faite attention le premier fichier qui est traité sera renommé automatiquement index.html), les autres conserveront leur nom de base
-o, --output-directory | chemin du dossier de fichier ou seront mis les fichiers generes en html
-t, --template-directory | dossier pouvant contenir les modeles de pages web a completer
-a, --achtung | Aide les allemends a lire nos blogs francais


Ma commande achtung ne fonctionne pas mais vous pouvez voir mes tentatives dans le `main.py`.