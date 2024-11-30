#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import sys
sys.setrecursionlimit(1500)  # Augmentez cette valeur si nécessaire

def main():
    """
    Point d'entrée principal pour les tâches administratives Django.
    - Définit les paramètres par défaut du projet Django.
    - Charge le gestionnaire de commandes pour exécuter des tâches (e.g., runserver, migrate).
    """
    # Définit le fichier de configuration par défaut pour le projet
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppBudget.settings')

    try:
        # Importe et exécute la commande Django appropriée
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Gère l'erreur si Django n'est pas correctement installé ou configuré
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Exécute la commande passée en ligne de commande (e.g., `python manage.py runserver`)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Appelle la fonction principale
    main()
