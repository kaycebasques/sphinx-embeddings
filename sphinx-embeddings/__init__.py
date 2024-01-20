import logging  # debug
log_id = 'sphinx-embeddings'  # debug
logger = logging.getLogger(log_id)  # debug
handler = logging.FileHandler(f'{log_id}.log')  # debug
logger.addHandler(handler)  # debug
logger.setLevel(logging.DEBUG)  # debug


def on_doctree_resolved(app, doctree, docname):  # TODO: type hints
    """TODO: Description"""
    logger.info(docname)
    

def setup(app):  # TODO: type hints
    """TODO: Description"""
    # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events
    app.connect('doctree-resolved', on_doctree_resolved)
    return {
        'version': '0.0.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
