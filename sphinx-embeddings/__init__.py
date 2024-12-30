import hashlib
import os

from .models import Gemini


gemini = Gemini()
data = {}


def cleanup(app, exception):
    embeddings_dir = app.config.sphinx_embeddings_dir
    for md5 in data:
        if data[md5]['stale'] == False:
            continue
        os.remove(f'{embeddings_dir}/{md5}.json')


def embed(app, doctree, docname):

    text = doctree.astext()
    md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
    if md5 in data:
        data[md5]['stale'] = False
        return
    gemini.embed(text, docname)


def setup(app):

    # User-configurable values
    app.add_config_value('sphinx_embeddings_models', None, 'html')
    default_dir = f'{app.confdir}/embeddings'
    app.add_config_value('sphinx_embeddings_dir', default_dir, 'html')
    embeddings_dir = app.config.sphinx_embeddings_dir

    # Directory setup
    if not os.path.exists(embeddings_dir):
        os.makedirs(embeddings_dir)

    # Build metadata
    for data_file in os.listdir(embeddings_dir):
        if not data_file.endswith('.json'):
            continue
        md5 = data_file.replace('.json', '')
        data[md5] = {'stale': True}

    # Model(s) initialization
    models = app.config.sphinx_embeddings_models
    if models is None:
        raise ValueError('sphinx_embeddings_models configuration is required')
    if 'gemini' in models:
        api_key = models['gemini']['api_key']
        gemini.configure(embeddings_dir, api_key)

    # Event handlers
    app.connect('doctree-resolved', embed)
    app.connect('build-finished', cleanup)

    # Metadata that Sphinx requires the extension to return
    return {
        'version': '0.0.8',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
