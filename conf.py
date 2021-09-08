"""
Configuration for building the website with Sphinx.
"""
import sys
import os
import datetime
import subprocess

extensions = ["myst_parser"]

# Sphinx project configuration
exclude_patterns = ["_build", "README.md"]
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
html_extra_path = []
html_use_smartypants = True
html_permalinks = False
pygments_style = "default"

# Ignore the default theme and define everything through our own template.
# These variables are passed to the templates in _templates/
html_context = {
    "menu_items": [
        ("About", "/about", True),
        ("Install", "/install", True),
        ("Learn", "/learn", True),
        ("Community", "/community", True),
        ("Contact", "/contact", True),
    ],
    "social_links": [
        (
            '<i class="fab fa-github fa-lg"></i>',
            "Our GitHub organization",
            "https://github.com/fatiando",
        ),
        (
            '<i class="fab fa-slack fa-lg"></i>',
            "Join our Slack chat",
            "http://contact.fatiando.org",
        ),
        (
            '<i class="fab fa-twitter fa-lg"></i>',
            "Our Twitter profile",
            "https://twitter.com/fatiandoaterra",
        ),
        (
            '<i class="fab fa-linkedin fa-lg"></i>',
            "Our LinkedIn profile",
            "https://www.linkedin.com/company/fatiando",
        ),
        (
            '<i class="fab fa-youtube fa-lg"></i>',
            "Our YouTube channel",
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
    "home_background": "_static/background.svg",
    "navbar_brand": "_static/fatiando-logo.svg",
    "stylesheet": "css/style.css",
}
