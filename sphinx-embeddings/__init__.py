import hashlib
import json
import os
from typing import Dict, Union

from docutils.nodes import section
from sphinx.application import Sphinx
from sphinx.addnodes import document

import logging  # debug
log_id = 'sphinx-embeddings'  # debug
logger = logging.getLogger(log_id)  # debug
handler = logging.FileHandler(f'{log_id}.log')  # debug
logger.addHandler(handler)  # debug
logger.setLevel(logging.DEBUG)  # debug


def prune_data(docname, before, after):
    old_data = [hash for hash in before if hash not in after]
    for hash in old_data:
        del data[docname][hash]
    # TODO: Delete old docs?


def on_doctree_resolved(app: Sphinx, doctree: document, docname: str) -> None:
    """TODO: Description"""
    before = []
    after = []
    if docname not in data:
        data[docname] = {}
    else:
        before = data[docname].keys()
    for node in doctree.traverse(section):
        text = node.astext()
        hash = hashlib.md5(text.encode('utf-8')).hexdigest()
        after.append(hash)
        if hash in data[docname]:
            continue
        data[docname][hash] = {}
        data[docname][hash]['text'] = text[0:50]
        # TODO: Generate embedding
    prune_data(docname, before, after)
    

def on_build_finished(app: Sphinx, exception) -> None:
    with open(srcpath, 'w') as f:
        json.dump(data, f, indent=4)
    with open(outpath, 'w') as f:
        json.dump(data, f, indent=4)


def init_configs(app: Sphinx) -> None:
    # https://ai.google.dev/models/gemini#embedding
    app.add_config_value(f'sphinx_embeddings_model', 'gemini/embedding-001', 'html')
    app.add_config_value(f'sphinx_embeddings_api_key', None, 'html')


def init_globals(srcdir: str, outdir: str) -> None:
    global filename
    global srcpath
    global outpath
    global data
    filename = 'embeddings.json'  # TODO: Make configurable
    srcpath = f'{srcdir}/{filename}'  # TODO: Make configurable
    outpath = f'{outdir}/{filename}'  # TODO: Make configurable
    data = {}
    if os.path.exists(srcpath):
        with open(srcpath, 'r') as f:
            data = json.load(f)


def setup(app: Sphinx) -> Dict[str, Union[bool, str]]:
    """TODO: Description"""
    init_globals(app.srcdir, app.outdir)
    init_configs(app)
    # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events
    app.connect('doctree-resolved', on_doctree_resolved)
    app.connect('build-finished', on_build_finished)
    return {
        'version': '0.0.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
