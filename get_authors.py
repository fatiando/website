#!/usr/bin/env python
"""
Fetch the names, handles and avatars of the authors of each Fatiando project
"""
import re
from requests import get


GITHUB_API_BASE_URL = "https://api.github.com/users/"
AUTHORS_BASE_URL = "https://raw.githubusercontent.com/fatiando/{}/{}/AUTHORS.md"


def get_authors(project, main_branch="master"):
    """
    Returns a dict with information about the author of the project

    Parameters
    ----------
    project : str
        Name of the Fatiando a Terra project.
    master : str (optional)
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
    Get authors' name and GitHub handle from content of AUTHORS.md file
    """
    regex_pattern = r"\[(.+?)\]\((?:https://github.com/)(.+?)\)"
    _authors = re.findall(regex_pattern, authors_md)
    authors = []
    for author in _authors:
        full_name, gh_handle = author[:]
        avatar_url = _get_avatar(gh_handle)
        authors.append((full_name, gh_handle, avatar_url))
    return authors


def _get_avatar(gh_handle):
    """
    Return the url to user's GitHub avatar
    """
    github_json_data = get(GITHUB_API_BASE_URL.format(gh_handle)).json()
    avatar_url = github_json_data["avatar_url"]
    return avatar_url
