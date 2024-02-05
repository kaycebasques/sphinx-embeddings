import json
import typing

import dotenv
import google.generativeai as gemini

with open('../sphinx-embeddings/version.json', 'r') as f:
    version = json.load(f)['version']

env = dotenv.dotenv_values('.env')
gemini.configure(api_key=env['GEMINI_API_KEY'])

project = 'sphinx-embeddings'
copyright = '2024, Kayce Basques'
author = 'Kayce Basques'
release = version
extensions = ['sphinx-embeddings']
templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'build.sh',
    'venv', 
]
html_theme = 'alabaster'

def embed(text: str) -> typing.Dict:
    response = gemini.embed_content(
        model='models/embedding-001',
        content=text,
        task_type='SEMANTIC_SIMILARITY'
    )
    return response['embedding'] if 'embedding' in response else None

sphinx_embeddings_function = embed
