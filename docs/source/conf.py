# Configuration file for the Sphinx documentation builder.

# -- Project information
project = 'EnergySystemModels'
copyright = '2024, Zoheir HADID'
author = 'Zoheir HADID'
release = '0.1.17'
version = '0.1.17-63'

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.i18n',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
language = None  # Default language is English
locale_dirs = ['locale/']
gettext_compact = False

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
