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
import sys

# from docutils.parsers.rst import directives

from sphinx_open_needs.version import VERSION

sys.path.insert(0, os.path.abspath("../sphinx_open_needs"))

# -- Project information -----------------------------------------------------

project = 'Sphinx-Open-Needs'
copyright = '2022, team useblocks'
author = 'team useblocks'

# The full version, including alpha/beta/rc tags
version = VERSION

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.ifconfig",
    "sphinxcontrib.needs",
    "sphinx_needs_enterprise",
    "sphinx_design",
    "sphinxcontrib.programoutput",
    "sphinx_copybutton",
    "sphinx_immaterial",

]

intersphinx_mapping = {"needs": ("https://sphinxcontrib-needs.readthedocs.io/en/latest/", None)}

ons_server = "http://127.0.0.1:9595"

ons_content = """
{{data.description}}"""

needs_extra_options = ["author"]

needs_types = [
    dict(directive="req", title="Requirement", prefix="R_", color="#BFD8D2", style="node"),
    dict(directive="spec", title="Specification", prefix="S_", color="#FEDCD2", style="node"),
    dict(directive="impl", title="Implementation", prefix="I_", color="#DF744A", style="node"),
    dict(directive="test", title="Test Case", prefix="T_", color="#DCB239", style="node"),
    dict(directive="task", title="Task", prefix="T_", color="#DCB239", style="node"),
    # Kept for backwards compatibility
    dict(directive="need", title="Need", prefix="N_", color="#9856a5", style="node"),
]


def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != "html" and app.builder.name != "linkcheck":
        return
    src = source[0]
    from jinja2 import Template

    template = Template(src, autoescape=True)
    rendered = template.render(**app.config.html_context)
    source[0] = rendered


# Check, if docs get built on ci.
# If this is the case, external services like Code-beamer are not available and
# docs will show images instead of getting real data.
on_ci = os.environ.get("ON_CI", "False").upper() == "TRUE"


def setup(app):
    print(f"---> ON_CI is: {on_ci}")
    app.connect("source-read", rstjinja)


html_context = {"on_ci": on_ci}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = os.environ.get("THEME", "sphinx_immaterial")

# Set link name generated in the top bar.
html_title = "Sphinx-Open-Needs"

# html_favicon = "./_static/sphinx-needs-logo-favicon.png"
# html_logo = "./_static/sphinx-needs-logo-white.png"
# material theme options (see theme.conf for more information)
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "site_url": "https://useblocks.com/sphinx-needs-enterprise/",
    "repo_url": "https://github.com/open-needs/sphinx-open-needs",
    "repo_name": "Sphinx-Open-Needs",
    "repo_type": "github",
    "edit_uri": "blob/master/docs",
    "globaltoc_collapse": True,
    "features": [
        "navigation.sections",
        "navigation.top",
        "search.share",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "blue",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "blue",
            "accent": "yellow",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
    "toc_title_is_page_title": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css"]

if html_theme == "sphinx_immaterial":
    html_sidebars = {"**": ["logo-text.html", "globaltoc.html", "navigation.html",
                            "localtoc.html", "searchbox.html"]}


rst_epilog = """
.. |ex| replace:: **Code** 

.. |out| replace:: **Output** 

.. |br| raw:: html 

   <br>

"""