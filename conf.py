"""
Configuration for building the website with Sphinx.
"""
import sys
import os
import datetime

extensions = []

# Sphinx project configuration
exclude_patterns = ["_build"]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

# General information about the project
year = datetime.date.today().year
project = "Fatiando a Terra"
copyright = "2010-{:d}, The Fatiando a Terra Developers".format(year)
version = ""

html_title = project
html_short_title = ""
html_logo = "_static/fatiando-logo-background.png"
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_extra_path = []
html_use_smartypants = True
pygments_style = "default"
# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True
# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# Theme configuration.
html_theme = "basic"
html_context = {
    "menu_items": [
        ("About", "#about", True),
        ("Projects", "#projects", True),
        ("Getting Started", "#getting-started", True),
        ("Support", "#support", True),
        ("Contact", "#contact", True),
        ("Contribute", "#contribute", True),
    ],
    "social_links": [
        (
            '<i class="fab fa-github fa-lg"></i>',
            "Github",
            "https://github.com/fatiando",
        ),
        (
            '<i class="fab fa-slack fa-lg"></i>',
            "Slack chat group",
            "http://contact.fatiando.org",
        ),
        (
            '<i class="fab fa-twitter fa-lg"></i>',
            "Twitter",
            "https://twitter.com/fatiandoaterra",
        ),
        (
            '<i class="fab fa-youtube fa-lg"></i>',
            "YouTube channel",
            "https://www.youtube.com/fatiandoorg",
        ),
    ]
}
html_css_files = [
    "css/bootstrap/bootstrap.min.css",
    "css/fontawesome/css/all.css",
    "css/style.css",
]
