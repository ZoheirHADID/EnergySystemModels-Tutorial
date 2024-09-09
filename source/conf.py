import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'EnergySystemModels'
author = 'Zoheir HADID'
version = '0.1'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []
html_static_path = ['_static']
html_theme = 'alabaster'

# Configuration pour les langues
language = None  # Utilisez None pour l'anglais
locale_dirs = ['locale/']  # Répertoire pour les fichiers de traduction

# Configuration des langues pour le build
gettext_compact = False
