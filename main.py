import os
import markdown2
import re
import argparse
 
#préparation pour les liens
lien = [(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'), r'\1')]

#toutes nos commandes

parser = argparse.ArgumentParser(description="Transposition de fichier markdown dans un dossier vers des fichiers html dans un nouveau dossier.")
parser.add_argument('-i', '--input-directory', type=str, metavar='', required=True, help="chemin du dossier de fichiers source(contenant les fichiers markdown)")
parser.add_argument('-o', '--output-directory', type=str, metavar='', required=True, help="chemin du dossier de fichier ou seront mis les fichiers generes pour le site statique")
parser.add_argument('-t', '--template-directory', type=str, metavar='', help="dossier pouvant contenir les modeles de pages web a completer")
parser.add_argument('-k', '--kikoulol', type=str, metavar='', help="Rajout de kikoulol,mdr,lol dans le texte aleatoirement")
parser.add_argument('-a', '--achtung', type=str, metavar='', help="Aide les allemends a lire nos blogs francais")
args = parser.parse_args()



dossier_md = args.input_directory
dossier_html = args.output_directory
dossier_temp = args.template_directory
# utilise le package markdown2 et traduit en html




def conv(dossier_md,dossier_html):
    nbr_html = 0
 # créer une liste de tous les fichiers présent dans dossier md# 
    liste = os.listdir(dossier_md)
    for files in liste:
        # prend chaque ligne dans les fichiers et les lis
        with open(f'{dossier_md}/{files}', "r") as text:
            transf = markdown2.markdown(text.read(), extras = ["lien"], link_patterns = lien)
            fichier_html = open(f'{dossier_html}/index{nbr_html}.html',"w")
            fichier_html.write(transf)
            fichier_html.close()
            nbr_html += 1

conv(dossier_md, dossier_html)