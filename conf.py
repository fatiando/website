# -*- coding: utf-8 -*-
import sys
import os
import datetime
import sphinx_bootstrap_theme

# Sphinx needs to be able to import fatiando to use autodoc
sys.path.append(os.path.pardir)

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
]

# Sphinx project configuration
templates_path = ['_templates']
exclude_patterns = ['_build']
source_suffix = '.rst'
# The encoding of source files.
#source_encoding = 'utf-8-sig'
master_doc = 'index'

# General information about the project
year = datetime.date.today().year
project = 'Fatiando a Terra'
copyright = '2010-{:d}, Leonardo Uieda'.format(year)
version = ""

# These enable substitutions using |variable| in the rst files
rst_epilog = """
.. |year| replace:: {year}
""".format(year=year)

html_last_updated_fmt = '%b %d, %Y'
html_title = project
html_short_title = project
html_logo = '_static/fatiando-navbar-logo.png'
html_favicon = 'favicon.ico'
html_static_path = ['_static']
html_extra_path = ['.nojekyll', 'CNAME']
html_use_smartypants = True
pygments_style = 'default'
add_function_parentheses = False
# Custom sidebar templates, maps document names to template names.
html_sidebars = {}
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
html_show_sourcelink = True
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True
# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True
# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''
# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None
# Output file base name for HTML help builder.
htmlhelp_basename = 'FatiandoATerraDoc'

# Theme config
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    'bootswatch_theme': "flatly",
    'navbar_title': 'fatiando',
    'navbar_site_name': "Site",
    'navbar_links': [
        ("Install", "install"),
        ("Gallery", "gallery/index"),
        ("API", "api"),
        ("Docs", "docs"),
        ("Contribute", "develop"),
        ("Cite", "cite"),
        ('<i class="fa fa-github fa-lg" title="Source code on Github"></i>', "https://github.com/fatiando/fatiando", True),
    ],
    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,
    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,
    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "This page",
    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 1,
    # Include hidden TOCs in Site navbar?
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "false",
    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-default",
    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "false",
    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "footer",
    'bootstrap_version': "3",
}

# Load the custom CSS files (needs sphinx >= 1.6 for this to work)
def setup(app):
    app.add_stylesheet("style.css")
    app.add_stylesheet("font-awesome/css/font-awesome.css")
