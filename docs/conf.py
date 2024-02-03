import dotenv

env = dotenv.dotenv_values('.env')

project = 'sphinx-embeddings'
copyright = '2024, Kayce Basques'
author = 'Kayce Basques'
release = '0.0.2'
extensions = ['sphinx-embeddings']
templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'build.sh',
    'venv', 
]
html_theme = 'alabaster'

sphinx_embeddings_function = lambda text: text[::-1]  # reverse the string
