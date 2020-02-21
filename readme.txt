Help on module etoiles:

NAME
    etoiles

DESCRIPTION
    Exploitation du Catalogue of the Brightest Stars (Ochsenbein+ 1988).
    Les fichiers :
        catalog.dat
        names.dat
    doivent �tre t�l�charg�s sur le site du catalogue et plac�s dans le dossier
    du module.
    Lien de t�l�chargement :
    ftp://cdsarc.u-strasbg.fr/cats/V/53A

CLASSES
    builtins.object
        Etoile
    
    class Etoile(builtins.object)
     |  Classe contentant pour une �toile donn�e quelques attributs du
     |  catalogue.
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |  
     |  __repr__(self)
     |      Proc�dure d'affichage des attributs d'une �toile.
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
        Retourne les coordonn�es d'une �toile en fonction de l'ann�e julienne
        en tenant compte de la position 2000.0 et du mouvement propre.
        Entr�e :
            HR num�ro de l'�toile
            J ann�e julienne
        Retour :
            coordonn�es ........
    
    etoile_data(HR)
        Retourne les attributs d'une �toile rep�r�e par son num�ro HR.
        Entr�e :
            HR num�ro de l'�toile
        Retour :
            Attributs de l'�toile (objet Etoile)

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


