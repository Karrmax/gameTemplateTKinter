"""
Auteur: Jules GRIVOT PELISSON
Classe: Main
Description: Ce fichier contient le point d'entrée principal de l'application. Il initialise et démarre l'application.
TODO: Ajouter des fonctionnalités spécifiques pour le point d'entrée principal, comme la gestion des arguments de ligne de commande ou des configurations de démarrage.
Date de création: 16/12/2024
Date de modification: 16/12/2024
"""

from screens.mainRoot import MainRoot

def main():
    """
    Point d'entrée principal de l'application.
    Initialise et démarre l'application.
    """
    app = MainRoot()
    app.start()

if __name__ == "__main__":
    main()