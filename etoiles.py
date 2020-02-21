#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: etoiles.py
# Auteur: Marc COATANHAY

"""
    Exploitation du Catalogue of the Brightest Stars (Ochsenbein+ 1988).
    Les fichiers :
        catalog.dat
        names.dat
    doivent être téléchargés sur le site du catalogue et placés dans le dossier
    du module.
    Lien de téléchargement :
    ftp://cdsarc.u-strasbg.fr/cats/V/53A
"""

# Import des modules
try:
    import mes_modules_path
    from etoilescat.repertoire import filerep
    filerep()
    names_file = 'names.dat'
    cat_file = 'catalog.dat'
except:
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    # Définitions constantes et variables globales
    root = Tk()
    names_file = askopenfilename(
            parent=root,
            filetypes=( ("Tous les fichiers", "*.*"),
                        ("Fichier Texte", "*.txt")
                            ),
            title="Indiquer le chemin du fichier 'names.dat'")
    cat_file = askopenfilename(
            parent=root,
            filetypes=( ("Tous les fichiers", "*.*"),
                        ("Fichier Texte", "*.txt")
                            ),
            title="Indiquer le chemin du fichier 'catalog.dat'")
    root.destroy()

# Définitions fonctions et classes
class Etoile():
    """
        Classe contentant pour une étoile donnée quelques attributs du
        catalogue.
    """
    def __init__(self):
        pass

    def __repr__(self):
        """
            Procédure d'affichage des attributs d'une étoile.
        """
        chaine = "------------------------" + "\n"
        chaine +=  "HR : " + str(self.HR) + "\n"
        chaine += "Name : " + self.Name + "\n"
        chaine += "HD : " + str(self.HD) + "\n"
        chaine += "Flamsteed : " + self.Flamsteed + "\n"
        chaine += "Bayer : " + self.Bayer + "\n"
        chaine += "Const : " + self.Const + "\n"
        chaine += "VarName : " + self.VarName + "\n"
        chaine += "RAh (h): " + self.RAh + "\n"
        chaine += "RAm (min): " + self.RAm + "\n"
        chaine += "RAs (s): " + self.RAs + "\n"
        chaine += "DEsgn : " + self.DEsgn + "\n"
        chaine += "DEd (°): " + self.DEd + "\n"
        chaine += "DEm ('): " + self.DEm + "\n"
        chaine += "DEs (\"): " + self.DEs + "\n"
        chaine += "pmRA (mas/yr): " + self.pmRA + "\n"
        chaine += "pmDE (mas/yr): " + self.pmDE
        return chaine

def catalogue_calc():
    """
        Construction du catalogue.
    """
    try:
        # Exploitation de names_file
        # --------------------------
        file = open(names_file, "r")
        lignes = file.readlines()
        file.close()
        for ligne in lignes:
            HR = int(ligne[0:4])
            nom = ligne[6:18].strip()
            noms[HR] = nom

        # Exploitation de cat_file
        # ------------------------
        file = open(cat_file, "r")
        lignes = file.readlines()
        file.close()
        for ligne in lignes:
            etoile = Etoile()
            # HR 1-4
            HR = int(ligne[0:4])
            etoile.HR = HR
            # Name
            if HR in noms:
                etoile.Name = noms[HR]
            else:
                etoile.Name = "---"
            # HD 6-11
            etoile.HD = int(ligne[5:11])
            # Flamsteed 13-15
            etoile.Flamsteed = ligne[12:15].strip()
            # Bayer 18-21
            etoile.Bayer = ligne[17:21].strip()
            # Const 23-25
            etoile.Const = ligne[22:25].strip()
            # VarName 28-37
            etoile.VarName = ligne[27:37].strip()
            # RAh 39-40
            etoile.RAh = ligne[38:40].strip()
            # RAm 42-43
            etoile.RAm = ligne[41:43].strip()
            # RAs 45-48
            etoile.RAs = ligne[44:48].strip()
            # DEsgn 50-50
            etoile.DEsgn = ligne[49:50].strip()
            # DEd 51-52
            etoile.DEd = ligne[50:52].strip()
            # DEm 54-55
            etoile.DEm = ligne[53:55].strip()
            # DEs 57-58
            etoile.DEs = ligne[56:58].strip()
            # pmRA 119-124
            etoile.pmRA = ligne[118:124].strip()
            # pmDE 126-131
            etoile.pmDE = ligne[125:131].strip()

            catalogue[HR] = etoile
    except:
        print("Fichiers non accessibles.")

def coordonnees(HR, J):
    """
        Retourne les coordonnées d'une étoile en fonction de l'année julienne
        en tenant compte de la position 2000.0 et du mouvement propre.
        Entrée :
            HR numéro de l'étoile
            J année julienne
        Retour :
            coordonnées ........
    """
    cat = etoile_data(HR)
    # A finir ...

def etoile_data(HR):
    """
        Retourne les attributs d'une étoile repérée par son numéro HR.
        Entrée :
            HR numéro de l'étoile
        Retour :
            Attributs de l'étoile (objet Etoile)
    """
    return catalogue[HR]

"""
    Construction du catalogue d'étoiles.
        nom = dictionnaire contenant les noms d'étoiles
        catalogue = dictionnaire contenant les attributs des étoiles
"""
noms = {}
catalogue = {}
catalogue_calc()
