from sphinx.application import Sphinx


import logging  # debug
log_id = 'sphinx-embeddings'
logger = logging.getLogger(log_id)  # debug
handler = logging.FileHandler(f'{log_id}.log')  # debug
logger.addHandler(handler)  # debug
logger.setLevel(logging.DEBUG)  # debug


def on_doctree_resolved(app, doctree, docname):  # TODO: type hints
    """TODO"""
    logger.info(docname)
    

def setup(app: Sphinx) -> Dict[str, bool]:
    """TODO"""
    # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events
    app.connect('doctree-resolved', on_doctree_resolved)
    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
