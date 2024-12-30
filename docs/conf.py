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
        'text-embedding-004': {
            'task_types': [
                'CLASSIFICATION',
                'CLUSTERING',
                # 'FACT_VERIFICATION',  # not supported?
                # 'QUESTION_ANSWERING',  # not supported?
                'RETRIEVAL_DOCUMENT',
                'RETRIEVAL_QUERY',
                'SEMANTIC_SIMILARITY',
                # 'TASK_TYPE_UNSPECIFIED'  # supported but not necessary
            ]
        },
        'api_key': os.environ['GEMINI_API_KEY']
    },
    'voyage': {
        'voyage-3': {
            'task_types': [
                'SEMANTIC_SIMILARITY'
            ]
        },
        'api_key': '...'
    }
}


# HTML theme
html_theme = 'alabaster'
