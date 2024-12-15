"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: GameScreen
Description: Cette classe représente l'écran de jeu. Elle gère l'affichage du jeu, les pauses, les scores et les interactions utilisateur.
TODO: Ajouter des fonctionnalités spécifiques pour l'écran de jeu, comme des animations de transition, des effets visuels ou des interactions avancées avec les éléments du jeu.
Date de création: 2024-18-11
Date de modification: 2024-10-12
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
    def __init__(self, root, switchCallback, loadManager, **kwargs):
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