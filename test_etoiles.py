#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: test_etoiles.py
# Auteur: Marc COATANHAY

"""
    Tests pour le module etoiles.
"""

# Import des modules
from etoiles import *
import unittest

# Définitions constantes et variables globales

# Définitions fonctions et classes
class MeeusTest(unittest.TestCase):
    def test_HR3982(self):
        dat = etoile_data(3982)
        self.assertEqual(dat.pmRA, "-249")
        self.assertEqual(dat.pmDE, "4")

if (__name__ == "__main__"):
    unittest.main()