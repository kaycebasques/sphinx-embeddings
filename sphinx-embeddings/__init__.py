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
    if not os.path.exists(app.config.sphinx_embeddings_dir):
        os.makedirs(app.config.sphinx_embeddings_dir)

    # Model initialization
    model = app.config.sphinx_embeddings_model
    api_key = app.config.sphinx_embeddings_api_key
    if model == 'text-embedding-004':
        gemini.configure(out_dir, api_key)
    else:
        raise ValueError(
            f'Invalid value provided for sphinx_embeddings_model: {model}\n'
            'Valid values: text-embedding-004'
        )

    # Event handlers
    app.connect('doctree-resolved', on_doctree_resolved)

    # Metadata that Sphinx requires the extension to return
    return {
        'version': '0.0.8',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
