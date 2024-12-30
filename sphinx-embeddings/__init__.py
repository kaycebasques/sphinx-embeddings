import hashlib
import json
import os

from .models import Gemini, Voyage


gemini = Gemini()
voyage = Voyage()
metadata = {}


def cleanup(app, exception):
    embeddings_dir = app.config.sphinx_embeddings_dir
    for md5 in metadata:
        if metadata[md5]['stale'] == False:
            continue
        os.remove(f'{embeddings_dir}/{md5}.json')


def embed(app, doc_tree, doc_name):

    text = doc_tree.astext()
    md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
    if md5 in metadata:
        metadata[md5]['stale'] = False
        return
    data = {
        'doc_name': doc_name,
        'text': text,
        'md5': md5
    }
    models = app.config.sphinx_embeddings_models
    if 'gemini' in models:
        data['gemini'] = {}
        for name in models['gemini']['models']:
            model = models['gemini']['models'][name]
            data['gemini'][name] = {}
            for task_type in model['task_types']:
                embedding = gemini.embed(text, name, task_type)
                data['gemini'][name][task_type] = embedding
    embeddings_dir = app.config.sphinx_embeddings_dir
    output_path = f'{embeddings_dir}/{md5}.json'
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)


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
        metadata[md5] = {'stale': True}

    # Model(s) initialization
    models = app.config.sphinx_embeddings_models
    if models is None:
        raise ValueError('sphinx_embeddings_models configuration is required')
    if 'gemini' in models:
        api_key = models['gemini']['api_key']
        gemini.configure(api_key)
    if 'voyage' in models:
        api_key = models['voyage']['api_key']
        voyage.configure(api_key)

    # Event handlers
    app.connect('doctree-resolved', embed)
    app.connect('build-finished', cleanup)

    # Metadata that Sphinx requires the extension to return
    return {
        'version': '0.0.8',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
