"""
Configuration for building the website with Sphinx.
"""
import re
import datetime
import subprocess
from requests import get
from pathlib import Path


AUTHORS_BASE_URL = "https://raw.githubusercontent.com/fatiando/{}/{}/AUTHORS.md"
AUTHOR_HTML_CARD = """
<div class="col-6 col-md-3 col-sm-4">
  <div class="card">
    <img
        class="card-img-top"
        src="{avatar_url}"
        alt="Profile picture of {full_name}"
    >
    <div class="card-body">
      <h4 class="card-title fs-5">
          {full_name}
      </h4>
      <p class="card-text text-muted fs-6">
        <a href="https://github.com/{gh_handle}">@{gh_handle}</a>
        on <i class="fab fa-github" title="GitHub"></i>
      </p>
    </div>
  </div>
</div>
"""


def authors_cards(package, main_branch="master"):
    """
    Generate the html snippet for the authors cards of each package

    Parameters
    ----------
    package : str
        Name of the Fatiando a Terra package.
    main_branch : str (optional)
        Name of the main branch of the package. Default to ``"master"``.

    Returns
    -------
    html_snippet : string
        HTML snippet for generating the authors cards of the selected package.
    """
    authors = get_authors(package, main_branch=main_branch)
    html_snippet = '<div class="row gy-3">\n'
    for author in authors:
        full_name, gh_handle = author[:]
        avatar_url = get_avatar(gh_handle)
        html_snippet += AUTHOR_HTML_CARD.format(
            gh_handle=gh_handle, full_name=full_name, avatar_url=avatar_url
        )
    html_snippet += "</div>"
    return html_snippet


def get_avatar(gh_handle):
    """
    Returns url avatar picture of GitHub user

    If the picture is not availabe, returns url to a placeholder.
    """
    gh_avatar_url = f"https://github.com/{gh_handle}.png"
    status_code = get(gh_avatar_url).status_code
    if status_code == 404:
        return "/_static/avatar-placeholder.jpg"
    return gh_avatar_url


def get_authors(package, main_branch="master"):
    """
    Returns a dict with information about the author of the package

    Parameters
    ----------
    package : str
        Name of the Fatiando a Terra package.
    main_branch : str (optional)
        Name of the main branch of the package. Default to ``"master"``.

    Returns
    -------
    authors : list
        List of tuples. Each tuple contains the ``full_name`` and the
        ``github_handle`` of each user.
    """
    authors_md_url = AUTHORS_BASE_URL.format(package, main_branch)
    markdown = get(authors_md_url).text
    authors = _get_authors(markdown)
    return authors


def _get_authors(authors_md):
    """
    Get authors' name and GitHub handle from AUTHORS.md content
    """
    regex_pattern = r"\[(.+?)\]\((?:https://github.com/)(.+?)\)"
    _authors = re.findall(regex_pattern, authors_md)
    authors = []
    for author in _authors:
        full_name, gh_handle = author[:]
        authors.append((full_name, gh_handle))
    return authors


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

# Generate cards with the authors of each project
FATIANDO_PACKAGES = "pooch verde harmonica boule".split()
for package in FATIANDO_PACKAGES:
    html_snippet = authors_cards(package)
    authors_file = Path("about") / f"{package}-authors.md"
    with open(authors_file, "w") as f:
        f.write(html_snippet)

# Ignore the default theme and define everything through our own template.
# These variables are passed to the templates in _templates/
html_context = {
    "menu_items": [
        ("Install", "install", True),
        ("Learn", "learn", True),
        ("Contact", "contact", True),
        ("About Us", "about", True),
        ("Community", "community", True),
        ("Cite", "cite", True),
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
            "http://contact.fatiando.org",
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
