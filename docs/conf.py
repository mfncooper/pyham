# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'PyHam'
copyright = '2024-2025, Martin F N Cooper'
author = 'Martin F N Cooper'


# -- General configuration ---------------------------------------------------

templates_path = ['_templates']

rst_prolog = """
.. meta::
   :author: Martin F N Cooper
   :description: PyHam - Python Software for Ham Radio
"""


# -- Options for HTML output -------------------------------------------------

html_theme = 'bizstyle'
html_static_path = ['_static']
html_css_files = [ 'css/pyham.css' ]
html_sidebars = { '**': ['localtoc.html'] }
html_use_index = False
html_show_sourcelink = False
