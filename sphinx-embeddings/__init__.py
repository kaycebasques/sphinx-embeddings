import os

from .models import Gemini


gemini = Gemini()


def on_doctree_resolved(app, doctree, docname):

    text = doctree.astext()
    gemini.embed(text, docname)


def setup(app):

    # User-configurable values
    # TODO: Make this a single dict called sphinx_embeddings_models and
    # let each model have slightly different values as needed
    app.add_config_value(
        'sphinx_embeddings_model',
        'text-embedding-004',
        'html',
        [str],
        'The embeddings model to use. Valid values: text-embedding-004'
    )
    app.add_config_value(
        'sphinx_embeddings_api_key',
        None,
        'html',
        [str],
        'A valid API key for the embedding model.'
    )
    default_out_dir = f'{app.confdir}/embeddings'
    app.add_config_value(
        'sphinx_embeddings_out_dir',
        default_out_dir,
        'html',
        [str],
        (
            'The directory where embeddings will be saved.\n'
            'The directory will be created if it does not already exist.\n'
            f'Default value: {default_out_dir}\n'
        )
    )
    out_dir = app.config.sphinx_embeddings_out_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

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
