"""
Auteur: Jules GRIVOT PELISSON
Classe: BaseScreen
Description: Cette classe est la classe dont chaque fenetre de jeu hérite. Elle contient les fonctions de base pour chaque fenetre de jeu.
Date de création: 16/12/2024
Date de modification: 16/12/2024
"""

import tkinter as tk

class BaseScreen(tk.Frame):
    """
    Classe représentant l'écran de jeu.
    
    Attributs:
        switchCallback (function): Fonction de rappel pour changer d'écran.
        loadManager (LoadManager): Gestionnaire de chargement des ressources.
        canvas (tk.Canvas): Canvas pour afficher le jeu.
    """
    def __init__(self, root, switchCallback, loadManager, inputManager, **kwargs):
        """
        Initialise l'écran de jeu.
        
        Args:
            root (tk.Tk): Fenêtre principale de l'application.
            switchCallback (function): Fonction de rappel pour changer d'écran.
            loadManager (LoadManager): Gestionnaire de chargement des ressources.
        """
        super().__init__(root)
        

        self.switchCallback = switchCallback
        self.loadManager = loadManager
        self.inputManager = inputManager
        self.canvas = None
        
        if "canvas" in kwargs and kwargs["canvas"]:
            self.canvas = tk.Canvas(self, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="black")
            self.canvas.pack(fill="both", expand=True)
        # Création du canvas avec la largeur et la hauteur de l'écran, fond noir

        
    def onActivateFunction(self):
        """
        Fonction appelée lors de l'activation de l'écran.
        """
        pass