from docutils import nodes
from sphinx.writers.html import HTML5Translator

class CustomHTML5Translator(HTML5Translator):
    def visit_fontawesome(self, node):
        # Optionally, you can add HTML rendering logic here
        pass

    def depart_fontawesome(self, node):
        pass

def setup(app):
    app.set_translator('html', CustomHTML5Translator)
