"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: GameLogic
Description: Cette classe gère la logique du jeu, y compris les entrées utilisateur, le rendu, les mises à jour du jeu et la gestion des niveaux.
TODO: Ajouter des comportements spécifiques pour la logique du jeu, comme des animations de fin de niveau, des effets visuels ou des interactions avancées avec les éléments du jeu.
Date de création: 2024-16-11
Date de modification: 2024-04-12
"""

# from managers.inputManager import InputManager
from managers.renderManager import RenderManager
from divers.vector import Vector
from game.Board import Board
import time

class GameLogic:
    """
    Classe représentant la logique du jeu.
    
    Attributs:
        canvas (tk.Canvas): Le canvas pour le rendu du jeu.
        callback_endSequence (function): Fonction de rappel pour la fin de la séquence de jeu.
        loadManager (LoadManager): Le gestionnaire de chargement des ressources.
        inputManager (InputManager): Le gestionnaire des entrées utilisateur.
        renderManager (RenderManager): Le gestionnaire du rendu.
        board (Board): Le plateau de jeu.
        stage_manager (StageManager): Le gestionnaire des niveaux.
        running (bool): Indique si le jeu est en cours d'exécution.
        points (int): Les points du joueur.
        target_fps (int): Le nombre d'images par seconde cible.
    """
    def __init__(self, canvas, loadManager, inputManager, callback_endSequence, target_fps=60):
        """
        Initialise la logique du jeu avec les paramètres donnés.
        
        Args:
            screen (tk.Frame): L'écran de jeu.
            loadManager (LoadManager): Le gestionnaire de chargement des ressources.
            callback_endSequence (function): Fonction de rappel pour la fin de la séquence de jeu.
            target_fps (int, optional): Le nombre d'images par seconde cible. Par défaut, 60.
        """
        self.canvas = canvas
        self.callback_endSequence = callback_endSequence
        self.loadManager = loadManager
        self.inputManager = inputManager
        
        loadManager.resizeAllBackgrounds(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight())
        bgs = self.loadManager.getBackgrounds()
        
        self.renderManager = RenderManager(self.canvas, bgs)
        
        self.board = Board(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), self.loadManager)
        
        self.running = False
        self.points = 0
        
        self.target_fps = target_fps
        self.frame_time = 1 / self.target_fps

        # Bind input events
        canvas.focus_set()
        
    
    
    def start(self):
        """
        Démarre la boucle de jeu.
        """
        self.running = True
        
        # Ajout du vaisseau principal
        # self.loadShip()
        # self.loadWals()
        # self.stage_manager.generateStage()
        
        
        self.game_loop()
        
    def stop(self):
        """
        Arrête la boucle de jeu.
        """
        self.running = False

    def game_loop(self):
        """
        Boucle principale du jeu.
        """
        start_time = time.time()

        if self.running:
            self.changeState()
            self.update()
            self.render()
            
            # if not self.board.noEnemies() and self.board.isGameFinished():
            #     self.endSequence()


        # tick at the end of the loop
        elapsed_time = time.time() - start_time
        sleep_time = max(0, self.frame_time - elapsed_time)

        self.canvas.after(int(sleep_time * 1000), self.game_loop)
            
    def changeState(self):
        """
        Change l'état du jeu en fonction des entrées utilisateur.
        """
        inputs = self.inputManager.get_inputs()
        # print(inputs)
        # self.stage_manager.changeStates()
        # for entity in self.board.getEntities():
        #     entity.changeState(inputs)
            
    def update(self):
        """
        Met à jour la logique du jeu.
        """
        # self.board.manageCollisions()
        # for entity in self.board.getEntities():
        #     entity.update()

    def render(self):
        """
        Rend l'état actuel du jeu.
        """
        # self.renderManager.render(self.board.getEntities(), self.board, self.stage_manager.numStage)
        # self.renderManager.renderInfos(self.board.points, self.stage_manager.numStage, self.board.mainShip.HP)

    
    def reset(self):
        """
        Réinitialise le plateau de jeu et le gestionnaire de niveaux.
        """
        self.board.reset()
        self.running = False
        
        
    def pause(self):
        """
        Met le jeu en pause.
        """
        self.running = False
        
    def unPause(self):
        """
        Reprend le jeu après une pause.
        """
        self.running = True
        
    def endSequence(self):
        """
        Termine la séquence de jeu et appelle la fonction de rappel de fin de séquence.
        """
        self.callback_endSequence(self.board.points)
        
    def get_points(self):
        """
        Retourne les points du joueur.
        
        Returns:
            int: Les points du joueur.
        """
        return self.board.points
