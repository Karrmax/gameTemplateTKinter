"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: InputManager
Description: Cette classe gère les entrées utilisateur pour le jeu. Elle permet de suivre les touches pressées et relâchées.
TODO: Ajouter des fonctionnalités spécifiques pour la gestion des entrées, comme la prise en charge des manettes de jeu ou des gestes tactiles.
Date de création: 16/12/2024
Date de modification: 16/12/2024
"""

class InputManager:
    """
    Classe représentant le gestionnaire des entrées utilisateur.
    
    Attributs:
        keys (dict): Dictionnaire des touches actuellement pressées.
    """
    def __init__(self):
        """
        Initialise le gestionnaire des entrées utilisateur.
        """
        self.keys = {}

    def bindAll(self, screen):
        """
        Lie les événements d'entrée utilisateur au gestionnaire d'entrées.
        
        Args:
            screen (tk.Frame): L'écran de jeu.
        """
        screen.bind("<KeyPress>", self.key_pressed)
        screen.bind("<KeyRelease>", self.key_released)
        
    def key_pressed(self, event):
        """
        Gère l'événement de pression d'une touche.
        
        Args:
            event (tk.Event): L'événement de pression de touche.
        """
        # print(event.keysym)
        if event.keysym == "Caps_Lock" or event.keysym == "Alt_L" or event.keysym == "Alt_R" or event.keysym == "Shift_R" or event.keysym == "Shift_L":
            self.keys = {}    
        self.keys[event.keysym] = True

    def key_released(self, event):
        """
        Gère l'événement de relâchement d'une touche.
        
        Args:
            event (tk.Event): L'événement de relâchement de touche.
        """
        if event.keysym in self.keys:
            del self.keys[event.keysym]

    def get_inputs(self):
        """
        Retourne les touches actuellement pressées.
        
        Returns:
            dict: Dictionnaire des touches actuellement pressées.
        """
        return self.keys
