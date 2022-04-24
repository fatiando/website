"""
Configuration for building the website with Sphinx.
"""
import sys
import re
import datetime
import subprocess
from requests import get
from pathlib import Path


# Need this so the authors extension can be imported
sys.path.append(".")

extensions = [
    "myst_parser",
    "sphinx_extensions.authors",
]

# Sphinx project configuration
exclude_patterns = ["_build", "README.md", "LICENSE.md"]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

# General information about the project
current_date = datetime.date.today()
project = "Fatiando a Terra"
copyright = f"{current_date.year:d} The Fatiando a Terra Developers"
version = ""

html_title = project
html_short_title = ""
html_logo = "_static/fatiando-logo-background.png"
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_extra_path = ["forward"]
html_use_smartypants = True
html_permalinks = False
pygments_style = "default"

# Ignore the default theme and define everything through our own template.
# These variables are passed to the templates in _templates/
html_context = {
    "menu_items": [
        ("About", "about", True),
        ("Install", "install", True),
        ("Learn", "learn", True),
        ("Contact", "contact", True),
        ("Community", "community", True),
        ("Cite", "cite", True),
        ("Support", "support", True),
    ],
    "social_links": [
        (
            "fab fa-github",
            "GitHub",
            "https://github.com/fatiando",
        ),
        (
            "fab fa-slack",
            "Slack",
            "/slack",
        ),
        (
            "fab fa-twitter",
            "Twitter",
            "https://twitter.com/fatiandoaterra",
        ),
        (
            "fab fa-linkedin",
            "LinkedIn",
            "https://www.linkedin.com/company/fatiando",
        ),
        (
            "fab fa-youtube",
            "YouTube",
            "https://www.youtube.com/fatiandoorg",
        ),
    ],
    "base_url": "https://www.fatiando.org",
    "twitter": "fatiandoaterra",
    "description": "Open-source Python tools for geophysics",
    "commit": subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        capture_output=True,
        text=True,
    ).stdout.strip(),
    "repository": "fatiando/website",
    "last_updated": str(current_date),
    "navbar_brand": "_static/fatiando-logo.svg",
    "stylesheet": "css/style.css",
}
