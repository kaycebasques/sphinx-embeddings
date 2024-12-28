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
sphinx_embeddings_model = 'text-embedding-004'
sphinx_embeddings_api_key = '...'


# HTML theme
html_theme = 'alabaster'
