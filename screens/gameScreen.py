"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: GameScreen
Description: Cette classe représente l'écran de jeu. Elle gère l'affichage du jeu, les pauses, les scores et les interactions utilisateur.
TODO: Ajouter des fonctionnalités spécifiques pour l'écran de jeu, comme des animations de transition, des effets visuels ou des interactions avancées avec les éléments du jeu.
Date de création: 16/12/2024
Date de modification: 16/12/2024
"""

import tkinter as tk
from screens.baseScreen import BaseScreen
from game.GameLogic import GameLogic

class GameScreen(BaseScreen):
    """
    Classe représentant l'écran de jeu.
    
    Attributs:
        switch_callback (function): Fonction de rappel pour changer d'écran.
        load_manager (LoadManager): Gestionnaire de chargement des ressources.
        canvas (tk.Canvas): Canvas pour afficher le jeu.
        gameLogic (GameLogic): Logique du jeu.
        paused (bool): Indique si le jeu est en pause.
        pause_menu_buttons (list): Liste des boutons du menu de pause.
        scoreManager (ScoreManager): Gestionnaire des scores.
    """
    def __init__(self, root, switch_callback, load_manager, inputManager):
        """
        Initialise l'écran de jeu.
        
        Args:
            root (tk.Tk): Fenêtre principale de l'application.
            switch_callback (function): Fonction de rappel pour changer d'écran.
            load_manager (LoadManager): Gestionnaire de chargement des ressources.
        """
        super().__init__(root, switch_callback, load_manager, inputManager, canvas=True)
        
        # Initialisation de la logique du jeu avec une cible de 60 FPS
        self.gameLogic = GameLogic(self.canvas, self.loadManager, self.inputManager, self.callback_endSequence, target_fps=60)

        # Bind the Esc key to pause the game
        # root.bind("<KeyRelease-Escape>", self.toggle_pause)

        self.paused = False
        self.pause_menu_buttons = []
        
        # self.scoreManager = ScoreManager()

    def onActivateFunction(self):
        """
        Fonction appelée lors de l'activation de l'écran.
        """
        self.start_game_loop()
        
    def goLobby(self):
        """
        Change l'écran pour le lobby et réinitialise la logique du jeu.
        """
        self.switch_callback("lobbyScreen")
        self.gameLogic = GameLogic(self.canvas, self.loadManager, self.inputManager, self.callback_endSequence, target_fps=60)
        
    def start_game_loop(self):
        """
        Démarre la boucle de jeu.
        """
        self.gameLogic.start()

    def callback_endSequence(self, points):
        """
        Affiche l'écran de fin de jeu avec les points et les options pour sauvegarder le score ou rejouer.
        
        Args:
            points (int): Les points obtenus par le joueur.
        """
        self.paused = True
        self.gameLogic.pause()

        # Griser l'arrière-plan
        self.canvas.create_rectangle(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height(), fill="gray", stipple="gray50")

        # Afficher le texte "GAME OVER"
        self.canvas.create_text(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2 - 200, text="GAME OVER", font=("Arial", 36), fill="white")

        # Afficher les points
        self.canvas.create_text(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2 - 100, text=f"Points: {points}", font=("Arial", 24), fill="white")

        # Créer le champ de saisie pour le nom d'utilisateur
        self.username_entry = tk.Entry(self.canvas, font=("Arial", 24))
        username_entry_window = self.canvas.create_window(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2, window=self.username_entry)
        self.pause_menu_buttons.append(username_entry_window)

        # Créer le bouton "Save"
        save_button = tk.Button(self.canvas, text="Save", command=self.save_score, bg="black", fg="white", font=("Arial", 24), padx=20, pady=10)
        save_button_window = self.canvas.create_window(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2 + 100, window=save_button)
        self.pause_menu_buttons.append(save_button_window)

        # Créer le bouton "Play Again"
        play_again_button = tk.Button(self.canvas, text="Play Again", command=self.play_again, bg="black", fg="white", font=("Arial", 24), padx=20, pady=10)
        play_again_button_window = self.canvas.create_window(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2 + 200, window=play_again_button)
        self.pause_menu_buttons.append(play_again_button_window)

    def play_again(self):
        """
        Redémarre le jeu.
        """
        self.gameLogic = GameLogic(self.canvas, self.loadManager, self.inputManager, self.callback_endSequence, target_fps=60)
        self.resume_game()
        self.start_game_loop()