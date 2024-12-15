"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: LobbyScreen
Description: Cette classe représente l'écran du lobby. Elle permet de naviguer vers le jeu ou le tableau des scores.
TODO: Ajouter des fonctionnalités spécifiques pour l'écran du lobby, comme des animations, des effets visuels ou des interactions avancées avec les éléments du jeu.
Date de création: 2024-18-11
Date de modification: 2024-10-12
"""

import tkinter as tk
from tkinter import messagebox

from screens.baseScreen import BaseScreen

class LobbyScreen(BaseScreen):
    """
    Classe représentant l'écran du lobby.
    
    Attributs:
        switchCallback (function): Fonction de rappel pour changer d'écran.
        loadManager (LoadManager): Gestionnaire de chargement des ressources.
        canvas (tk.Canvas): Canvas pour afficher le fond du lobby.
    """
    def __init__(self, root, switchCallback, loadManager):
        """
        Initialise l'écran du lobby.
        
        Args:
            root (tk.Tk): Fenêtre principale de l'application.
            switchCallback (function): Fonction de rappel pour changer d'écran.
            loadManager (LoadManager): Gestionnaire de chargement des ressources.
        """
        # 
        
        super().__init__(root, switchCallback, loadManager, canvas=True)

        #canvas = tk.Canvas(self, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        # self.canvas.pack(fill="both", expand=True)

        # Get the background image from LoadManager
        self.background_image = self.loadManager.getMainBG()
        if self.background_image:
            self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        # Titre du lobby
        self.canvas.create_text(root.winfo_screenwidth() // 2, 100, text="My Game", font=("Helvetica", 36), fill="yellow")

        # Bouton pour démarrer le jeu
        start_button = tk.Button(self.canvas, text="Start Game", font=("Helvetica", 24), fg="yellow", bg="black", command=lambda: self.switchCallback("gameScreen"))
        self.canvas.create_window(root.winfo_screenwidth() // 2, 200, window=start_button)

        # Bouton pour afficher le tableau des scores
        leaderboard_button = tk.Button(self.canvas, text="Leaderboard", font=("Helvetica", 18), fg="yellow", bg="black", command=lambda: self.switchCallback("leaderboardScreen"))
        self.canvas.create_window(root.winfo_screenwidth() // 2, 300, window=leaderboard_button)
        
        # bouton pour à propos et crédits
        about_button = tk.Button(self.canvas, text="À propos", font=("Helvetica", 18), fg="yellow", bg="black", command=self.show_about)
        self.canvas.create_window(root.winfo_screenwidth() // 2, 350, window=about_button)
        
        
        
        # Bouton pour Quitter le jeu
        quit_button = tk.Button(self.canvas, text="Quitter", font=("Helvetica", 18), fg="yellow", bg="black", command=lambda: self.quit())
        self.canvas.create_window(root.winfo_screenwidth() // 2, 400, window=quit_button)


        ####### Les lignes suivantes permettent d'afficher si besoin une barre de menue en haut de la page
        
        # Création de la barre de menu
        # self.menu_bar = tk.Menu(root)
        # root.config(menu=self.menu_bar)

        # # Ajout du menu "Aide"
        # help_menu = tk.Menu(self.menu_bar, tearoff=0)
        # self.menu_bar.add_cascade(label="Aide", menu=help_menu)
        # help_menu.add_command(label="À propos", command=self.show_about)
        
        # # Ajout du menu "Quitter"
        # self.menu_bar.add_command(label="Quitter", command=self.quit)
        
        # Ajout du boutton menu Lancer une partie
        # self.menu_bar.add_command(label="Lancer une partie", command=lambda: self.switchCallback("game"))

    def show_about(self):
        """
        Affiche une boîte de dialogue "À propos".
        """
        messagebox.showinfo("À propos", "MyGame \n Version 1.0 \n Auteurs: Jules GRIVOT PELISSON")