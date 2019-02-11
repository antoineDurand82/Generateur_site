# Generateur_site

## Projet

Nous devions créer un programme capable de prendre un dossier possédant des fichiers en markdown et de les transformer en fichiers html dans un autre dossier pour les fichiers html.

### Le programme

Comme écrit dans le [requirements](./requirements.txt) vous allez avoir besoin du package [markdown2](https://github.com/trentm/python-markdown2)
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

-i, --input-directory | chemin du dossier des fichiers markdown (faite attention le premier fichier qui est traité sera renommé automatiquement index.html), les autres conserveront leur nom de base<br>
-o, --output-directory | chemin du dossier de fichier où seront mis les fichiers générés en html<br>
-t, --template-directory | dossier pouvant contenir les modèles de pages web à completer<br>
-a, --achtung | Aide les allemends à lire nos blogs francais<br>
-k, --kikoulol | Aide les kikou à comprendre nos blogs (un peu trop même avec le mien)


N'oubliez pas de rajouter un argument après les commandes (un lien vers un dossier pour -i et -o et n'importe quoi après -a et -k)

Projet réalisé en collaboration avec Théo Delas et Alex Boisseau.