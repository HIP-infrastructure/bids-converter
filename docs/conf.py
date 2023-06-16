# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import os
import sys

import mock

sys.path.append("../")  # noqa: 402

from datahipy.info import __version__
from datahipy.info import __release_date__

import time

from recommonmark.parser import CommonMarkParser


# Workaround: https://github.com/readthedocs/recommonmark/issues/177#issuecomment-555553053
class CustomCommonMarkParser(CommonMarkParser):
    def visit_document(self, node):
        pass


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("../datahipy"))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    # "sphinx.ext.viewcode",
    "sphinxarg.ext",
    "sphinx.ext.inheritance_diagram",
    "sphinxcontrib.apidoc",
    "sphinxemoji.sphinxemoji",
    "m2r2",
]

# autodoc_default_options = {
#    'autosummary': True,
# }

autodoc_mock_imports = [
    "bids-manager",
    "PyQt5",
    "pydicom",
    "paramiko",
    "bids_validator",
    "xlrd",
    "nibabel",
    "tkcalendar",
    "pysimplegui",
    "pandas",
    "bids",
]

# Make sure sphinx argparse considers the autodoc_mock_imports
for mod_name in autodoc_mock_imports:
    sys.modules[mod_name] = mock.Mock()

# Accept custom section names to be parsed for numpy-style docstrings
# of parameters.
# Requires pinning sphinxcontrib-napoleon to a specific commit while
# https://github.com/sphinx-contrib/napoleon/pull/10 is merged.
napoleon_use_param = False
napoleon_custom_sections = [
    ("Inputs", "Parameters"),
    ("Outputs", "Parameters"),
    ("Attributes", "Parameters"),
    ("Mandatory Inputs", "Parameters"),
    ("Optional Inputs", "Parameters"),
]


on_rtd = os.environ.get("READTHEDOCS") == "True"
if on_rtd:
    extensions.append("readthedocs_ext.readthedocs")

apidoc_module_dir = "../datahipy"
apidoc_output_dir = "api/generated"
# apidoc_excluded_paths = ['tests']
apidoc_separate_modules = True

# Allow errors in notebooks for doc
nbsphinx_allow_errors = True

# Consistent emoticon style
sphinxemoji_style = "twemoji"
sphinxemoji_source = 'https://unpkg.com/twemoji@latest/dist/twemoji.min.js'

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Use Markdown and reStructuredText in the same Sphinx project
# source_parsers = {
#     ".md": CustomCommonMarkParser,
# }
# The suffix of source filenames.
source_suffix = [".rst", ".md"]

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "DataHIPy: Data Manager of the Human Intra-cerebral EEG Platform"
copyright = "2022-{}, The HIP team, University Hospital of Lausanne (CHUV), Switzerland & Contributors".format(
    time.strftime("%Y")
)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

rst_prolog = """
.. |pypirelease| replace:: {}
.. |vrelease| replace:: {}
""".format(
    f"datahipy=={release}", f"v{release}"
)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%b %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]
default_role = "obj"

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

gettext_compact = False

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"  # 'sphinxdoc'
# html_theme = 'alabaster'#'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "logo_only": True,  # should be commented if html_theme = 'alabaster'
    "display_version": False,
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'DataHIPy: Data Manager of the Human Intracerebral Platform in Python'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "DataHIPy"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "logos/datahipy-logo-flower.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {'**': ['sidebar_version.html', 'localtoc.html','relations.html', 'sourcelink.html', 'searchbox.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "DataHIPydoc"

html_context = {"release_date": __release_date__}

# Activate autosectionlabel plugin
autosectionlabel_prefix_document = True

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    "papersize": "a4paper",
    # The font size ('10pt', '11pt' or '12pt').
    "pointsize": "10pt",
    # Additional package
    # 'extrapackages': r'',
    # Font settings
    #    'fontpkg': r'''
    # \setmainfont{DejaVu Serif}
    # \setsansfont{DejaVu Sans}
    # \setmonofont{DejaVu Sans Mono}
    # ''',
    # Additional stuff for the LaTeX preamble.
    "preamble": r"""
\usepackage{dejavu}
""",
    # Use Fancy chapter
    "fncychap": r"\usepackage[Bjornstrup]{fncychap}",
    # Adjust for the large character width of the monospace font, used in code-blocks
    # 'fvset': r'\\fvset{fontsize=\\footnotesize}', Seems not working!
    # Adjust size for long module name in generated index
    "printindex": r"""
\tiny\raggedright\printindex
""",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        "DataHIPy.tex",
        "DataHIPy Documentation",
        "The HIP team and Contributors",
        "manual",
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = "images/datahipy-logo.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# If true, show page references after internal links.
latex_show_pagerefs = True

# Specify Latex engine
# latex_engine = 'xelatex'

latex_show_urls = "footnote"

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        "index",
        "DataHIPy",
        "DataHIPy Documentation",
        ["The HIP team and Contributors"],
        1,
    )
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "DataHIPy",
        "DataHIPy Documentation",
        "The HIP team and Contributors",
        "datahipy",
        "Tools to manage BIDS datasets in the Human intracranial EEG platform.",
        "Science",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'
