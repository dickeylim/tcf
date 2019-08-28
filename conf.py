# -*- coding: utf-8 -*-
#
# timo documentation build configuration file, created by
# sphinx-quickstart on Wed Mar 25 09:00:21 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
# These are needed when we are building files in ./
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./ttbd'))
for path in os.environ.get("SPHINX_PATHS_EXTRA", "").split():
    sys.path.append(os.path.abspath(path))

# -- General configuration --------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo', 'sphinx.ext.autodoc', 'sphinx.ext.coverage',
    'sphinx.ext.intersphinx'
]
autodoc_default_flags = [ 'members', 'undoc-members' ]
autoclass_content = 'both'
autodoc_member_order = 'bysource'
# some imports can't be put in the build slaves without major effort
# and in any case, they are unneeed to build docs.
autodoc_mock_imports = [
    "prctl",
    "raritan",
    "requests_ntlm",
]

# Bring in documentation from other packages
intersphinx_mapping = {
    'jinja2': ('http://jinja.pocoo.org/docs/dev', None),
    'pexpect': ('http://pexpect.readthedocs.io/en/stable', None ),
    'pymongo': ('http://api.mongodb.com/python/current/', None ),
    'python': ( 'https://docs.python.org/2.7', None ),
    'requests': ( 'http://docs.python-requests.org/en/master/', None ),
    'serial': ('http://pythonhosted.org/pyserial/', None ),
}

# workaround:
#
## SOMEFILE.py:docstring of CLASS:: WARNING: py:class reference target not found: list
#
# Apaprently a backport bug to Python 2.7
#
# description: https://bugs.python.org/issue31117
# workaround: https://stackoverflow.com/questions/11417221/sphinx-autodoc-gives-warning-pyclass-reference-target-not-found-type-warning
nitpick_ignore = [('py:class', 'list')]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Test Case Framework'
copyright = u'2015, Author'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.11'
# The full version, including alpha/beta/rc tags.
release = '0.11'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    # Workaround to avoid this warning:
    #
    # WARNING: duplicate label XYZ, other instance in
    # ABSPATH/doc/02-guide-app-builder.rst
    #
    # which happens when including these files inside a bigger
    # one. Seems a bug in Sphinx that might have be fixed in newer
    # releases.
    # Individual files we have included 
    "doc/02-guide-contributing.rst",
    "doc/02-guide-tcf.rst",
    "doc/02-guide-tests.rst",
    "doc/02-guide-test-training.rst",
    "doc/02-guide-report-drivers.rst",
    "doc/02-guide-tcf-run.rst",
    "doc/02-guide-app-builder.rst",
    # these are the files we always include, so let's have them
    # excluded from being autoadded to avoid duplicates
    "doc/*-LL-*.rst",
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ------------------------------------------------
# import alabaster
#
# html_theme_path = [alabaster.get_path()]
# extensions.append('alabaster')
# html_theme = 'alabaster'
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',
#         'searchbox.html',
#         'donate.html',
#     ]
# }

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'tcfdoc'


# -- Options for LaTeX output -----------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples (source
# start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ('index', 'tcf.tex', u'Test Case Framework',
     u'Author', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output -----------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'tcf', u'Test Case Framework Documentation',
     [u'Author'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ---------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'tcf', u'Test case Framework Documentation',
     u'Author', 'tcf', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# -- Options for Epub output ------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'tcf'
epub_author = u'Author'
epub_publisher = u'Author'
epub_copyright = u'2015, Author'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True
