 #ouverture md / creation fichier html
fichier_md = open("test1.md", "r")
fichier_html = open("index.html", "w")

'''for x in fichier_md:
    for y in x:
        print(y)'''
ligne = [] #tableau de lignes qui vont être lues
for x in fichier_md: #pour chaque ligne du md on les ajoutes les unes après les autres au tableau
    ligne.append(x)
compteur_croisillon = 0
for r in ligne[2]: #sur chaque ligne on compte de # qu'il y a
    if r == "#":
        compteur_croisillon += 1
        
c = ligne[2].replace("#", "") #je remplace les # par du vide pour les enlever
v = c.replace("\n", "") #je remplace les \n pour les retirer et mettre la fermeture de ma balise html


if compteur_croisillon == 3: #j'écris dans mon html la ligne que je viens de faire (pas du tout automatiser)
    fichier_html.write("<h3>")
    fichier_html.write(v + "</h3>" + "\n")


print(compteur_croisillon)
print(ligne)