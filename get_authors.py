#!/usr/bin/env python
"""
Fetch the names, handles and avatars of the authors of each Fatiando project
"""
import re
from requests import get


AUTHORS_BASE_URL = "https://raw.githubusercontent.com/fatiando/{}/{}/AUTHORS.md"
AVATAR_BASE_URL = "https://github.com/{}.png"


def get_authors(project, main_branch="master"):
    """
    Returns a dict with information about the author of the project

    Parameters
    ----------
    project : str
        Name of the Fatiando a Terra project.
    main_branch : str (optional)
        Name of the main branch of the project. Default to ``"master"``.

    Returns
    -------
    authors : list
        List of tuples. Each tuple contains the ``full_name``, the
        ``github_handle`` and the ``avatar_url`` of each user.
    """
    authors_md_url = AUTHORS_BASE_URL.format(project, main_branch)
    markdown = get(authors_md_url).text
    authors = _get_authors(markdown)
    return authors


def _get_authors(authors_md):
    """
    Get authors' name, GitHub handle and url to avatar from AUTHORS.md
    """
    regex_pattern = r"\[(.+?)\]\((?:https://github.com/)(.+?)\)"
    _authors = re.findall(regex_pattern, authors_md)
    authors = []
    for author in _authors:
        full_name, gh_handle = author[:]
        avatar_url = AVATAR_BASE_URL.format(gh_handle)
        authors.append((full_name, gh_handle, avatar_url))
    return authors
