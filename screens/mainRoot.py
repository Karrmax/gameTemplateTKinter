"""
Auteur: Jules GRIVOT PELISSON
Classe: MainRoot
Description: Cette classe représente la fenêtre principale de l'application et gère la navigation entre les différents écrans.
TODO: Ajouter des fonctionnalités spécifiques pour la fenêtre principale, comme des animations de transition, des effets visuels ou des interactions avancées avec les éléments de l'interface utilisateur.
Date de création: 16/12/2024
Date de modification: 16/12/2024
"""

import tkinter as tk
import os
import importlib
from managers.loadManager import LoadManager
from managers.inputManager import InputManager

class MainRoot:
    """
    Classe représentant la fenêtre principale de l'application.
    
    Attributs:
        root (tk.Tk): La fenêtre principale de l'application.
        loadManager (LoadManager): Le gestionnaire de chargement des ressources.
        screens (dict): Dictionnaire des écrans de l'application.
        currentScreen (tk.Frame): L'écran actuellement affiché.
    """
    def __init__(self):
        """
        Initialise la fenêtre principale de l'application.
        """
        self.root = tk.Tk()
        self.root.title("Tkinter Game")
        self.root.state('zoomed') # fullscreen windowed

        self.loadManager = LoadManager()
        self.loadManager.load_resources()
        
        self.inputManager = InputManager()
        self.inputManager.bindAll(self.root)
        
        self.screens = {}
        self.currentScreen = None
        self.ignoredScreens = ["mainRoot", "leaderboardScreen"]
        self.init_screens()

    def init_screens(self):
        """
        Initialise les écrans de l'application dynamiquement en fonction du contenu de screens.
        """
        screens_folder = os.path.dirname(__file__)
        for filename in os.listdir(screens_folder):
            if filename.endswith(".py") and not ( filename.split(".py")[0] in self.ignoredScreens): #get all .py files except ingored ones
                module_name = filename[:-3] # remove .py extension
                module = importlib.import_module(f".{module_name}", package="screens") # import module dynamically
                class_name = ''.join([part[0].capitalize()+part[1::] for part in module_name.split('_')]) # works for My_Class_Name and MyClassName
                screen_class = getattr(module, class_name) # get class from module
                self.screens[module_name] = screen_class(self.root, self.switch_screen, self.loadManager, self.inputManager) # create instance of screen class and store it in screens dict
                
        self.switch_screen("lobbyScreen") # start with the lobby screen by default

    def switch_screen(self, screen_name):
        """
        Change l'écran actuellement affiché.
        
        Args:
            screen_name (str): Le nom de l'écran à afficher.
        """
        if not screen_name in self.screens:
            print(f"Screen {screen_name} not found.")
            return
        
        if self.currentScreen:
            self.currentScreen.pack_forget()
        self.currentScreen = self.screens[screen_name]
        
        self.currentScreen.pack(fill=tk.BOTH, expand=True)
        self.currentScreen.onActivateFunction()

    def start(self):
        """
        Démarre la boucle principale de l'application.
        """
        self.root.mainloop()



        
def resize(event):
    """
    Gère l'événement de redimensionnement de la fenêtre.
    
    Args:
        event (tk.Event): L'événement de redimensionnement.
    """
    print("New size is: {}x{}".format(event.width, event.height))
