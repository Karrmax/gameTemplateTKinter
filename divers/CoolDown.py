"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: CoolDown
Description: Cette classe gère le cooldown pour les actions dans le jeu. Elle permet de temporiser et d'activer une action uniquement après un certain délai.
TODO: Ajouter des fonctionnalités spécifiques pour le cooldown, comme des effets visuels ou des notifications lorsque le cooldown est terminé.
Date de création: 2023-10-10
Date de modification: 2023-10-10
"""

import time        
        
class CoolDown:
    """
    Classe représentant un cooldown.
    
    Attributs:
        CD (float): La durée du cooldown en secondes.
        lastTime (float): Le dernier moment où l'action a été effectuée.
    """
    def __init__(self, CD):
        """
        Initialise un cooldown avec la durée donnée.
        
        Args:
            CD (float): La durée du cooldown en secondes.
        """
        self.CD = CD
        self.lastTime = time.time()
        
        ## will time and enable the action only when lastTime = time 
        
    def isEnable(self):
        """
        Vérifie si le cooldown est terminé et si l'action peut être effectuée.
        
        Returns:
            bool: True si le cooldown est terminé, False sinon.
        """
        return (time.time() - self.lastTime) >= self.CD
    
    def set(self):
        """
        Définit le dernier moment où l'action a été effectuée à l'heure actuelle.
        """
        self.lastTime = time.time()
        
    def reset(self):
        """
        Réinitialise le cooldown.
        """
        self.lastTime = time.time(0)