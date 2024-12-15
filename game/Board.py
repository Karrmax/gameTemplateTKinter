"""
Auteur: Jules GRIVOT PELISSON
Classe: Board
Description: Cette classe représente le plateau de jeu. Elle gère les dimensions du plateau, les ennemis, le vaisseau principal, les projectiles, les murs et les collisions.
TODO: Ajouter des comportements spécifiques pour le plateau de jeu, comme des niveaux différents, des obstacles dynamiques ou des effets visuels.
Date de création: 2024-20-11
Date de modification: 2024-04-12
"""


class Board:
    """
    Classe représentant le plateau de jeu.
    
    Attributs:
        width (int): La largeur du plateau de jeu.
        height (int): La hauteur du plateau de jeu.
        ennemiesMatrix (list): La matrice des ennemis sur le plateau.
        mainShip (Element): Le vaisseau principal.
        fire (dict): Les projectiles tirés par les ennemis et le vaisseau principal.
        walls (list): Les murs sur le plateau.
        col (list): Les colonnes sur le plateau.
        load_manager (LoadManager): Le gestionnaire de chargement des ressources.
        points (int): Les points du joueur.
        allayZone (int): La zone d'allée sur le plateau.
    """
    def __init__(self, width, height, loadManager):
        """
        Initialise un plateau de jeu avec les dimensions données et le gestionnaire de chargement.
        
        Args:
            width (int): La largeur du plateau de jeu.
            height (int): La hauteur du plateau de jeu.
            loadManager (LoadManager): Le gestionnaire de chargement des ressources.
        """
        self.width = width
        self.height = height
        
        
        # creation de tous les emements du jeu
        
        self.load_manager = loadManager
        self.points = 0
        
        self.allayZone = height - 175
    
    
    def getEntities(self):
        """
        Retourne la liste de toutes les entités sur le plateau.
        
        Returns:
            list: La liste de toutes les entités sur le plateau.
        """
        return # liste de toutes les entités sur le plateau
    
    def remove(self, entity):
        """
        Supprime une entité du plateau.
        
        Args:
            entity (Element): L'entité à supprimer.
        """
        #supprime l'entité du plateau
    
            
    def reset(self):
        """
        Réinitialise le plateau de jeu.
        """
        #remet le plateau de jeu à zéro
       
    def isGameFinished(self):
        """
        Vérifie si le jeu est terminé.
        
        Returns:
            bool: True si le jeu est terminé, False sinon.
        """
        # finish condition