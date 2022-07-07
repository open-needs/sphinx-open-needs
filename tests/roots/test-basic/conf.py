# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os

# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "test basic"
copyright = "2022, team useblocks"
author = "team useblocks"
version = "0.1.1"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxcontrib.needs",
    "sphinx_open_needs",
]

needs_types = [
    {"directive": "req", "title": "Requirement", "prefix": "R_", "color": "#BFD8D2", "style": "node"},
    {"directive": "spec", "title": "Specification", "prefix": "SP_", "color": "#FEDCD2", "style": "node"},
    {"directive": "impl", "title": "Implementation", "prefix": "IM_", "color": "#DF744A", "style": "node"},
    {"directive": "task", "title": "Task", "prefix": "T_", "color": "#DCB239", "style": "node"},
]


needs_services = {
    "open-needs": {
        "url": "http://127.0.0.1:9595",
        "user": os.environ.get("ONS_USERNAME", ""),
        "password": os.environ.get("ONS_PASSWORD", ""),
        "id_prefix": "ONS_TEST_",
        "mappings": {
            "id": "{{key}}",
            "type": ["type"],
            "title": "{{title}}",
            "status": ["options", "status"],
            "links": ["references", "links"],
        },
        "extra_data": {
            "Priority": ["options", "priority"],
            "Approval": ["options", "approved"],
            "Cost": ["options", "costs"],
        },
    },
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]
