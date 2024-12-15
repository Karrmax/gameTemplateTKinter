"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: RenderManager
Description: Cette classe gère le rendu des entités et des arrière-plans sur le canvas du jeu.
TODO: Ajouter des fonctionnalités spécifiques pour le gestionnaire de rendu, comme des effets visuels avancés, des animations ou des transitions.
Date de création: 16/12/2024
Date de modification: 16/12/2024
"""

from tkinter import NW
from PIL import ImageTk
from managers.loadManager import LoadManager
 
class RenderManager:
    """
    Classe représentant le gestionnaire de rendu.
    
    Attributs:
        canvas (tk.Canvas): Le canvas pour le rendu du jeu.
        background_image (ImageTk.PhotoImage): L'image de fond actuelle.
        background_images (list): Liste des images de fond pour les différents niveaux.
    """
    def __init__(self, canvas, background_images):
        """
        Initialise le gestionnaire de rendu avec le canvas et les images de fond.
        
        Args:
            canvas (tk.Canvas): Le canvas pour le rendu du jeu.
            background_images (list): Liste des images de fond pour les différents niveaux.
        """
        self.canvas = canvas
        # self.background_image = background_images[1]
        # self.background_images = background_images

    def render(self, entities, board, stage):
        """
        Rend les entités et l'arrière-plan sur le canvas.
        
        Args:
            entities (list): Liste des entités à rendre.
            board (Board): Le plateau de jeu.
            stage (int): Le numéro du niveau actuel.
        """
        # if stage >= len(self.background_images):
        # stage = len(self.background_images) - 1
        stage = stage % (len(self.background_images)) - 1   
        self.background_image = self.background_images[1:][stage]
        
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        
        # délimitation de la zone de jeu
        self.canvas.create_line(0, board.allayZone, board.width, board.allayZone, fill="white", width=1)
        
        for entity in entities:
            if entity.hasSprite():
                self.canvas.create_image(entity.pos.x, entity.pos.y, image=entity.sprite, anchor="nw")
                
                #################   SHOW HIT BOX   ##############
                # self.canvas.create_rectangle(entity.pos.x, entity.pos.y, entity.pos.x + entity.size.x , entity.pos.y + entity.size.y, outline='red')
            else:
                print("has not sprite")
                self.canvas.create_rectangle(entity.pos.x, entity.pos.y, entity.pos.x + 20, entity.pos.y + 20, fill="white")
        
    def renderInfos(self, points, stage, HP):
        """
        Affiche les informations de jeu en haut à droite de l'écran.
        
        Args:
            points (int): Le nombre de points du joueur.
            stage (int): Le niveau actuel du jeu.
            HP (int): Les points de vie du joueur.
        """
        info_text = f"HP: {HP}\nPoints: {points}\nStage: {stage}"
        self.canvas.create_text(self.canvas.winfo_width() - 10, 10, text=info_text, anchor="ne", font=("Arial", 16), fill="white")
        
    def __del__(self):
        """
        Détruit le gestionnaire de rendu et libère les ressources.
        """
        del self.canvas