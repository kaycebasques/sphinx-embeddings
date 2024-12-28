from .models import Gemini


gemini = Gemini()


def on_doctree_resolved(app, doctree, docname):
    text = doctree.astext()
    gemini.embed(text, docname)


def setup(app):
    app.connect('doctree-resolved', on_doctree_resolved)
    gemini.configure(app.confdir, 'xyz123')
    return {
        'version': '0.0.8',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
