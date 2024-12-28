import hashlib
import json
import os

from .models import Gemini


gemini = Gemini()


# def on_build_finished(app, exception):
#     with open(srcpath, 'w') as f:
#         json.dump(data, f, indent=4)


def on_doctree_resolved(app, doctree, docname):
    text = doctree.astext()
    md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
    embedding = gemini.embed(text)
    data = {
        'docname': docname,
        'md5': md5,
        'embedding': embedding
    }
    path = f'{app.outdir}/{md5}.json'
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    # write embedding to tmp dir
    # provide tmp dir to model so that it can write itself
    # when done which will enable multithreading


def setup(app):
    # create tmp dir in app.outdir
    app.connect('doctree-resolved', on_doctree_resolved)
    gemini.configure(api_key='xyz123')
    # app.connect('build-finished', on_build_finished)
    return {
        'version': '0.0.8',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
