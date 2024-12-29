import json
import os


# Metadata
project = 'sphinx-embeddings'
copyright = '2024, Kayce Basques'
author = 'Kayce Basques'
release = '0.0.8'


# General
templates_path = ['_templates']
exclude_patterns = ['_build']


# Extensions
extensions = ['sphinx-embeddings']
sphinx_embeddings_models = {
    'gemini': {
        'models': ['text-embedding-004']
        'api_key': os.environ['GEMINI_API_KEY']
    }
}


# HTML theme
html_theme = 'alabaster'
