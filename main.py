import os
import markdown2
import re
import argparse
import random

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
kikoulol = args.kikoulol


def allemand():
    liste_md = os.listdir(dossier_md)
    for x_files in liste_md:
        with open(f'{dossier_md}/{x_files}', "r+") as text:
            lecture = text.read()
            v_allemand = open(f'{dossier_md}/allemand-{x_files}', "w")
            ecriture_s = lecture.replace("s", "z")
            ecriture_c = lecture.replace("c", "z")
            ecriture_q = lecture.replace("q", "k")
            ecriture_ph = lecture.replace("ph", "f")
            ecriture_b = lecture.replace("b", "p")
            ecriture_v = lecture.replace("v", "f")
            v_allemand.write(ecriture_s)
            v_allemand.write(ecriture_c)
            v_allemand.write(ecriture_q)
            v_allemand.write(ecriture_ph)
            v_allemand.write(ecriture_b)
            v_allemand.write(ecriture_v)
    return v_allemand


def kikou():
    liste_md = os.listdir(dossier_md)
    liste_kikou = [" kikou ", " lol ", " ptdr ", " mdr ", " trololo "]
    for x_files in liste_md:
        with open(f'{dossier_md}/{x_files}', "r+") as text:
            lecture = text.read()
            v_kikou = open(f'{dossier_md}/kikou-{x_files}', "w")
            compteur_espace = 0
            for espace in lecture:
                if espace == " ":
                    if compteur_espace == 30:
                        rand = random.choice(liste_kikou)
                        ajout_r = lecture.replace(" ", rand)
                        compteur_espace = 0
                        v_kikou.write(ajout_r)
                    else:
                        compteur_espace += 1
    return v_kikou


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


if achtung:
    allemand()
if kikoulol:
    kikou()

conv(dossier_md, dossier_html)
