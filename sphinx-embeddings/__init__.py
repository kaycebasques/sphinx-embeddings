import os

from .models import Gemini


gemini = Gemini()


def on_doctree_resolved(app, doctree, docname):

    text = doctree.astext()
    gemini.embed(text, docname)


def setup(app):

    # User-configurable values
    app.add_config_value('sphinx_embeddings_models', None, 'html')
    default_dir = f'{app.confdir}/embeddings'
    app.add_config_value('sphinx_embeddings_dir', default_dir, 'html')
    embeddings_dir = app.config.sphinx_embeddings_dir
    if not os.path.exists(embeddings_dir):
        os.makedirs(embeddings_dir)

    # Model initialization
    models = app.config.sphinx_embeddings_models
    if models is None:
        raise ValueError('sphinx_embeddings_models configuration is required')
    if 'gemini' in models:
        api_key = models['gemini']['api_key']
        gemini.configure(embeddings_dir, api_key)

    # Event handlers
    app.connect('doctree-resolved', on_doctree_resolved)

    # Metadata that Sphinx requires the extension to return
    return {
        'version': '0.0.8',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
