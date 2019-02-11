import os
import markdown2
import re
import argparse

# extra markdown2

lien = [(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'), r'\1')]

# toutes nos commandes

parser = argparse.ArgumentParser(
    description="Transposition de fichier markdown dans un dossier vers des fichiers html dans un nouveau dossier.")
parser.add_argument('-i', '--input-directory', type=str, metavar='', required=True,
                    help="chemin du dossier des fichiers markdown (faite attention le premier fichier qui est traité sera renommé automatiquement index.html, les autres conserveront leur nom de base")
parser.add_argument('-o', '--output-directory', type=str, metavar='', required=True,
                    help="chemin du dossier de fichier ou seront mis les fichiers generes en html")
parser.add_argument('-t', '--template-directory', type=str, metavar='',
                    help="dossier pouvant contenir les modeles de pages web a completer")
parser.add_argument('-k', '--kikoulol', type=str, metavar='',
                    help="Rajout de kikoulol,mdr,lol dans le texte aleatoirement")
parser.add_argument('-a', '--achtung', type=str, metavar='',
                    help="Aide les allemends a lire nos blogs francais")
args = parser.parse_args()


dossier_md = args.input_directory
dossier_html = args.output_directory
dossier_temp = args.template_directory
achtung = args.achtung


# utilise le package markdown2 et traduit en html
def conv(dossier_md, dossier_html):
    nbr_html = 0
 # créer une liste de tous les fichiers présent dans dossier md#
    liste = os.listdir(dossier_md)
    for x_files in liste:
        # prend chaque ligne dans les fichiers et les lis
        with open(f'{dossier_md}/{x_files}', "r") as text:
            transf = markdown2.markdown(
                text.read(), extras=["link-patterns", "cuddled-lists"], link_patterns=lien)
            if nbr_html < 1:
                fichier_html = open(f'{dossier_html}/index.html', "w")
            else:
                file = x_files[:-3]
                fichier_html = open(f'{dossier_html}/{file}.html', "w")
            fichier_html.write(transf)
            fichier_html.close()
            nbr_html += 1


conv(dossier_md, dossier_html)


# J'ai pas réussi à faire le achtung, je suis triste
# def aide_a():
#     liste_md = os.listdir(dossier_md)
#     ligne = []
#     for file in liste_md:
#         with open(f'{file}', "r+") as fichier:
#             test = fichier.read()
#             test = fichier.replace('a', 'tg')
#             fichier.write(test)

# if achtung:
#     aide_a()
# else:
#     pass
