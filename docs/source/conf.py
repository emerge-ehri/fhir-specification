# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import subprocess
#import sys
#sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
from sphinx.highlighting import lexers
from pygments.lexers.data import JsonLexer

lexers['json'] = JsonLexer(startinline=False)

def _get_git_tag():
    # To also capture stderr...
    res = subprocess.run("git describe --tags --always".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #res = subprocess.run("git describe --tags --always".split(), capture_output=True)
    tag = res.stdout.decode().strip()
    return tag

def _parse_release_as_version(rls):
    m = re.match("^(\d+\.\d+(\.\d+)*)", rls)
    if m:
        return m.group(1)
    return "unknown"

# -- Project information -----------------------------------------------------

project = u'emerge-fhir-spec'
copyright = u'2020, eMERGE Network'
author = u'Committers'
master_doc = 'index'
# N.B. RTD ignores these values. :-/
release = _get_git_tag()
version = _parse_release_as_version(release)

# -- Schema doc paths --------------------------------------------------------

rst_epilog_fn = os.path.join(os.path.dirname(__file__), 'rst_epilog')
rst_epilog = open(rst_epilog_fn).read().format(release=release)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinxcontrib.excel_table',
    'sphinxcontrib.imagesvg',
    'sphinxcontrib.images'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# TODO directive output
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo = '_images/logo_emerge6_03.png'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['custom.css']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }
