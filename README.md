Help on module etoiles:

NAME
    etoiles

DESCRIPTION
    Exploitation du Catalogue of the Brightest Stars (Ochsenbein+ 1988).
    Les fichiers :
        catalog.dat
        names.dat
    doivent être téléchargés sur le site du catalogue et placés dans le dossier
    du module.
    Lien de téléchargement :
    ftp://cdsarc.u-strasbg.fr/cats/V/53A

CLASSES
    builtins.object
        Etoile
    
    class Etoile(builtins.object)
     |  Classe contentant pour une étoile donnée quelques attributs du
     |  catalogue.
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |  
     |  __repr__(self)
     |      Procédure d'affichage des attributs d'une étoile.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    catalogue_calc()
        Construction du catalogue.
    
    coordonnees(HR, J)
        Retourne les coordonnées d'une étoile en fonction de l'année julienne
        en tenant compte de la position 2000.0 et du mouvement propre.
        Entrée :
            HR numéro de l'étoile
            J année julienne
        Retour :
            coordonnées ........
    
    etoile_data(HR)
        Retourne les attributs d'une étoile repérée par son numéro HR.
        Entrée :
            HR numéro de l'étoile
        Retour :
            Attributs de l'étoile (objet Etoile)

DATA
    cat_file = 'catalog.dat'
    catalogue = {3: ------------------------
    HR : 3
    Name : ---
    HD : ...2
    D...
    names_file = 'names.dat'
    noms = {15: 'Alpheratz', 21: 'Caph', 39: 'Algenib', 168: 'Schedar', 33...

FILE
    c:\users\mc\mu_code\_mes_modules\etoilescat\etoiles.py


