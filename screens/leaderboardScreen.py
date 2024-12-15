"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: LeaderboardScreen
Description: Cette classe représente l'écran du tableau des scores. Elle affiche les meilleurs scores des joueurs et permet de revenir au lobby.
TODO: Ajouter des fonctionnalités spécifiques pour le tableau des scores, comme la possibilité de filtrer les scores, de rechercher des joueurs ou d'afficher des statistiques avancées.
Date de création: 2024-18-11
Date de modification: 2024-01-12
"""

import tkinter as tk
# from managers.scoreManager import ScoreManager

class LeaderboardScreen(tk.Frame):
    """
    Classe représentant l'écran du tableau des scores.
    
    Attributs:
        switch_callback (function): Fonction de rappel pour changer d'écran.
        loadManager (LoadManager): Gestionnaire de chargement des ressources.
        scoreManager (ScoreManager): Gestionnaire des scores.
    """
    def __init__(self, root, switch_callback, loadManager):
        """
        Initialise l'écran du tableau des scores.
        
        Args:
            root (tk.Tk): Fenêtre principale de l'application.
            switch_callback (function): Fonction de rappel pour changer d'écran.
            loadManager (LoadManager): Gestionnaire de chargement des ressources.
        """
        super().__init__(root)
        self.switch_callback = switch_callback
        self.loadManager = loadManager

        # root.bind("<KeyRelease-Escape>", self.return_to_lobby)
        # root.bind("<Visibility>", lambda event: self.reload())
        self.reload()
        
    def return_to_lobby(self, event=None):
        """
        Retourne au lobby.
        
        Args:
            event (tk.Event, optional): L'événement de la touche Esc. Par défaut, None.
        """
        self.switch_callback("lobby")
        
    def reload(self):
        """
        Recharge le tableau des scores.
        """
        SM = ScoreManager()
        data = SM.get_score()
        sorted_list = sorted(data, key=lambda d: (list(d.values())[1], list(d.values())[2]))[::-1]
        keyless_list = [list(d.values()) for d in sorted_list]
        print_list = keyless_list[0:10]  # Max 10 profiles

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(len(print_list) + 3, weight=1)
        
        # Titre du tableau
        tk.Label(self, text="Leaderboard top 10 players", font=("Arial", 24)).grid(row=0, column=0, columnspan=3, pady=20)

        # En-têtes du tableau
        tk.Label(self, text="Username", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self, text="Score", font=("Arial", 12)).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self, text="Stage", font=("Arial", 12)).grid(row=1, column=2, padx=5, pady=5)

        # Affichage des scores
        for i, val in enumerate(print_list):
            bg_color = "#f0f0f0" if i % 2 == 0 else "#d0d0d0"
            tk.Label(self, text=val[0], font=("Arial", 12), bg=bg_color).grid(row=i+2, column=0, padx=5, pady=5, sticky="ew")
            tk.Label(self, text=val[1], font=("Arial", 12), bg=bg_color).grid(row=i+2, column=1, padx=5, pady=5, sticky="ew")
            tk.Label(self, text=val[2], font=("Arial", 12), bg=bg_color).grid(row=i+2, column=2, padx=5, pady=5, sticky="ew")

        # Bouton pour retourner au lobby
        tk.Button(self, text="Back to Lobby", command=lambda: self.switch_callback("lobby")).grid(row=len(print_list)+2, column=0, columnspan=3, pady=20)