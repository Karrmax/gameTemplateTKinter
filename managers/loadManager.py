"""
Auteur: Jules GRIVOT PELISSON, Raphael Dziopa
Classe: LoadManager
Description: Cette classe gère le chargement des ressources pour le jeu, y compris les images, les sons et les arrière-plans.
TODO: Ajouter des fonctionnalités spécifiques pour le gestionnaire de chargement, comme la gestion des ressources audio ou le préchargement des ressources pour améliorer les performances.
Date de création: 2024-16-11
Date de modification: 2024-10-12
"""

from PIL import Image, ImageTk

class LoadManager:
    """
    Classe représentant le gestionnaire de chargement des ressources.
    
    Attributs:
        resources (dict): Dictionnaire des ressources chargées.
        enemyRessources (dict): Dictionnaire des ressources ennemies chargées.
        backgroundRessources (list): Liste des ressources d'arrière-plan.
    """
    def __init__(self):
        """
        Initialise le gestionnaire de chargement des ressources.
        """
        self.resources = {}
        self.enemyRessources = {}
        self.backgroundRessources = []

    def load_resources(self):
        """
        Charge les ressources nécessaires pour le jeu.
        """
        # loading images, sounds, etc...
        print("Loading resources...")
        # self.resources["ship"] = ImageTk.PhotoImage(Image.open("ressources/images/pngegg.png").resize((60, 60)))
        # self.resources["fire"] = ImageTk.PhotoImage(Image.open("ressources/images/fire.png").resize((10, 58)))
        # self.resources["wall"] = ImageTk.PhotoImage(Image.open("ressources/images/sci-fiwall8bit.png").resize((150, 42)))
        
        # self.enemyRessources["enemy1"] = ImageTk.PhotoImage(Image.open("ressources/images/alien1.png").resize((40, 40)))
        # self.enemyRessources["enemy2"] = ImageTk.PhotoImage(Image.open("ressources/images/alien2.png").resize((40, 40)))
        # self.enemyRessources["enemy3full"] = ImageTk.PhotoImage(Image.open("ressources/images/alien3_FULL.png").resize((40, 40)))
        # self.enemyRessources["enemy3mid"] = ImageTk.PhotoImage(Image.open("ressources/images/alien3MID.png").resize((40, 40)))
        # self.enemyRessources["enemy3low"] = ImageTk.PhotoImage(Image.open("ressources/images/alien3LOW.png").resize((40, 40)))
        # self.enemyRessources["fireDown"] = ImageTk.PhotoImage(Image.open("ressources/images/fireDown.png").resize((10, 58)))
        
        
        # self.backgroundRessources.append(LoadManager.center_zoom_and_resize(Image.open("ressources/images/background.jpg")))
        # self.backgroundRessources.append(LoadManager.center_zoom_and_resize(Image.open("ressources/images/zvenus8bit.png"))) 
        # self.backgroundRessources.append(LoadManager.center_zoom_and_resize(Image.open("ressources/images/zearth8bit.jpg")))
        # self.backgroundRessources.append(LoadManager.center_zoom_and_resize(Image.open("ressources/images/zsaturn8bit.png")))
        # self.backgroundRessources.append(LoadManager.center_zoom_and_resize(Image.open("ressources/images/zjupiter8bit.png")))
        # self.backgroundRessources.append(LoadManager.center_zoom_and_resize(Image.open("ressources/images/zsun8bit.png")))
        
        print("Resources loaded.")
        
    def get_resource(self, name):
        """
        Retourne une ressource spécifique par son nom.
        
        Args:
            name (str): Le nom de la ressource.
        
        Returns:
            object: La ressource demandée.
        """
        return self.resources.get(name)
    
    def resizeAllBackgrounds(self, width, height):
        """
        Redimensionne toutes les ressources d'arrière-plan aux dimensions spécifiées.
        
        Args:
            width (int): La largeur cible.
            height (int): La hauteur cible.
        """
        for i in self.backgroundRessources:
            i = i.resize((width, height))
            
    def getBackgrounds(self):
        """
        Retourne une liste des arrière-plans redimensionnés sous forme d'objets ImageTk.PhotoImage.
        
        Returns:
            list: Liste des arrière-plans redimensionnés.
        """
        a = []
        for i in self.backgroundRessources:
            a.append(ImageTk.PhotoImage(i))
        return a
    
    def getMainBG(self):
        """
        Retourne l'arrière-plan principal sous forme d'objet ImageTk.PhotoImage.
        
        Returns:
            ImageTk.PhotoImage: L'arrière-plan principal.
        """
        
        return ImageTk.PhotoImage(self.backgroundRessources[0]) if len(self.backgroundRessources)>0 else None
            
    from PIL import Image
    
    @staticmethod
    def center_zoom_and_resize(image, output_size = (1920, 1080), zoom_factor = 1):
        """
        Zoom into the center of an image and resize it to the desired dimensions.

        Args:
            image_path (str): Path to the input image file.
            output_size (tuple): The desired output size as (width, height).
            zoom_factor (float): The factor by which to zoom in (e.g., 2.0 for 2x zoom).

        Returns:
            Image: The processed image.
        """
        # Open the image
        # image = Image.open(image_path)

        # Get original dimensions
        width, height = image.size

        # Calculate the dimensions of the zoomed area
        zoom_width = int(width / zoom_factor)
        zoom_height = int(height / zoom_factor)

        # Calculate the coordinates to center the zoomed area
        center_x, center_y = width // 2, height // 2
        left = max(center_x - zoom_width // 2, 0)
        top = max(center_y - zoom_height // 2, 0)
        right = min(center_x + zoom_width // 2, width)
        bottom = min(center_y + zoom_height // 2, height)

        # Crop the image to the zoomed area
        cropped_image = image.crop((left, top, right, bottom))

        # Resize the cropped image to the desired output size
        resized_image = cropped_image.resize(output_size, Image.LANCZOS)

        return resized_image


    def __del__(self):
        """
        Détruit le gestionnaire de chargement des ressources et libère les ressources.
        """
        del self.resources
