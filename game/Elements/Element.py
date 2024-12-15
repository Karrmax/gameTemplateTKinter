"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: Element
Description: Cette classe représente un élément de base dans le jeu. Elle gère les positions, les tailles, les sprites et les collisions des éléments.
TODO: Ajouter des comportements spécifiques pour les éléments, comme des animations, des interactions avec d'autres éléments ou des effets visuels.
Date de création: 2024-16-11
Date de modification: 2023-10-10
"""

from divers.vector import Vector, NULLVECTOR

class Element:
    """
    Classe représentant un élément de base.
    
    Attributs:
        board (Board): Le plateau de jeu.
        pos (Vector): La position de l'élément.
        size (Vector): La taille de l'élément.
        sprite (bool): Indique si l'élément a un sprite.
    """
    def __init__(self, board, pos: Vector, size: Vector):
        """
        Initialise un élément avec les paramètres donnés.
        
        Args:
            board (Board): Le plateau de jeu.
            pos (Vector): La position de l'élément.
            size (Vector): La taille de l'élément.
        """
        self.board = board
        self.pos = pos  # en (x, y)
        self.size = size  # en (x, y)
        self.sprite = False
        
    def hasSprite(self):
        """
        Vérifie si l'élément a un sprite.
        
        Returns:
            bool: True si l'élément a un sprite, False sinon.
        """
        return self.sprite != False
    
    def update(self):
        """
        Met à jour l'état de l'élément.
        """
        pass
    
    def changeState(self, input):
        """
        Change l'état de l'élément en fonction des entrées.
        
        Args:
            input: Les entrées pour changer l'état de l'élément.
        """
        pass
    
    def hit(self, proj):
        """
        Gère l'impact d'un projectile sur l'élément.
        
        Args:
            proj (Projectile): Le projectile qui touche l'élément.
        """
        pass
    
    @staticmethod
    def touched(e1, e2):
        """
        Vérifie si deux éléments se touchent.
        
        Args:
            e1 (Element): Le premier élément.
            e2 (Element): Le deuxième élément.
        
        Returns:
            bool: True si les éléments se touchent, False sinon.
        """
        return (e1.pointIn(e2.pos) or e1.pointIn(e2.pos + e2.size) or e1.pointIn(Vector(e2.pos.x + e2.size.x, e2.pos.y)) or e1.pointIn(Vector(e2.pos.x, e2.pos.y + e2.size.y)) or
                e2.pointIn(e1.pos) or e2.pointIn(e1.pos + e1.size) or e2.pointIn(Vector(e1.pos.x + e1.size.x, e1.pos.y)) or e2.pointIn(Vector(e1.pos.x, e1.pos.y + e1.size.y)))
        # regarde si les deux objets rectangulaires sont l'un dans l'autre (se touchent)
      
    def pointIn(self, point):
        """
        Vérifie si un point est à l'intérieur de l'élément.
        
        Args:
            point (Vector): Le point à vérifier.
        
        Returns:
            bool: True si le point est à l'intérieur de l'élément, False sinon.
        """
        return (point.x >= self.pos.x and point.x <= self.pos.x + self.size.x) and (point.y >= self.pos.y and point.y <= self.pos.y + self.size.y)
        
    def outOfBoard(self):
        """
        Vérifie si l'élément est en dehors du plateau de jeu.
        
        Returns:
            bool: True si l'élément est en dehors du plateau de jeu, False sinon.
        """
        return ((self.pos.x < 0 or self.pos.x + self.size.x > self.board.width) or
                (self.pos.y < 0 or self.pos.y + self.size.y > self.board.height))
    
    def outOfBoardLarge(self):
        """
        Vérifie si l'élément est largement en dehors du plateau de jeu.
        
        Returns:
            bool: True si l'élément est largement en dehors du plateau de jeu, False sinon.
        """
        return ((self.pos.x + self.size.x < 0 or self.pos.x - self.size.x > self.board.width) or
            (self.pos.y + self.size.y < 0 or self.pos.y - self.size.y > self.board.height))