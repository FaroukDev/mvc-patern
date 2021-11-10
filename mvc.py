import sys

# La vue se charge de récupérer l'action utilisateur qui est de taper une ligne de texte sur l'entrée standard
class Vue:
    def entree(self):
        return sys.stdin.readline()

# Le controleur fait le lien entre la vue et le modèle en effectuant des traitements sur la donnée
class Controleur:
    # Le controleur demande à la vue de récupérer une chaine de caractères sur l'entrée standard, et ensuite demande au modèle 
    # de le stocker
    def stockEntree(self):
        chaine = vue.entree()
        modele.ajouter(chaine.upper())

    # Le controleur récupère les chaînes du modèle et va écrire dans un fichier
    def sauvegardeChaines(self):
        chaines = modele.recupererChaines()
        with open('test.txt', 'w') as f:
            for chaine in chaines:
                f.write(chaine)

class Modele: 
    def __init__(self):
        self.chaines = []

    # Ajoute une chaine dans la liste
    def ajouter(self, chaine):
        self.chaines.append(chaine)

    # Retourne le liste de chaînes.
    def recupererChaines(self):
        return self.chaines

# Les acteurs MVC sont globaux dans cet exemple 
vue = Vue()
controleur = Controleur()
modele = Modele()
# on veut récupérer 2 lignes sur l'entrée standard.
# _ est utilisé pour ignorer l'index: https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc
for _ in range(2):
    controleur.stockEntree()
# Puis on sauvegarde dans un fichier
controleur.sauvegardeChaines()

