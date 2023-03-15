"""
Sphinx extension for inserting a list of authors from Fatiando projects

Based on:

* sphinx-contributors (https://github.com/dgarcia360/sphinx-contributors) by
  David Garcia (@dgarcia360), distributed under the MIT license.
* sphinx-pannels (https://github.com/executablebooks/sphinx-panels) by
  Executable Books, distributed under the MIT license.
"""
import re
import json
from pathlib import Path

import requests
from docutils import nodes
from docutils.parsers.rst import Directive, directives

__version__ = "0.2.0"


def _parse_authors_file(package):
    """
    Returns a dict with information about the author of the package

    Parameters
    ----------
    package : str
        Name of the Fatiando a Terra package.

    Returns
    -------
    authors : list
        List of tuples. Each tuple contains the ``full_name`` and the
        ``github_handle`` of each user.
    """
    response = requests.get(
        f"https://raw.githubusercontent.com/fatiando/{package}/main/AUTHORS.md",
    )
    response.raise_for_status()
    markdown = response.text
    authors = re.findall(r"\[(.+?)\]\((?:https://github.com/)(.+?)/?\)", markdown)
    return {handle: name for name, handle in authors}


def _make_card_list(authors):
    """
    Create a list of cards for a particular package.
    """
    row_classes = "row g-1 mt-3 mb-4".split()
    col_classes = "col-6 col-sm-4 col-md-3 col-lg-2".split()
    # Use is_div=True in our containers to stop docutils inserting the
    # "container" class. Based on code from sphinx-panels.
    row = nodes.container(is_div=True, classes=row_classes)
    for handle in sorted(authors.keys(), key=str.lower):
        col = nodes.container(is_div=True, classes=col_classes)
        card = nodes.container(is_div=True, classes="card h-100 bg-ligh".split())
        card += nodes.image(
            uri=f"https://github.com/{handle}.png",
            alt=f"Profile picture of {authors[handle]}",
            classes=["card-img-top"],
        )
        card_body = nodes.container(
            is_div=True, classes="card-body text-center fs-6".split()
        )
        card_name = nodes.paragraph(classes=["card-text"])
        card_name += nodes.reference(
            text=authors[handle], refuri=f"https://github.com/{handle}"
        )
        card_body += card_name
        card += card_body
        col += card
        row += col
    return [row]


class AuthorsDirective(Directive):
    """
    The fatiando-authors directive.
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}

    def run(self):
        packages = self.arguments[0].split(",")
        authors = {}
        for package in packages:
            authors.update(_parse_authors_file(package))
        return _make_card_list(authors)


class GovernanceDirective(Directive):
    """
    The fatiando-governance directive.
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}

    def run(self):
        fname = Path(self.arguments[0])
        return _make_card_list(json.loads(fname.read_text()))


def setup(app):
    app.add_directive("fatiando-authors", AuthorsDirective)
    app.add_directive("fatiando-governance", GovernanceDirective)

    ###########################################################################
    # Hack from sphinx-panels to make docutils stop inserting the "container"
    # class into divs (which doesn't play nicely with bootstrap).

    def visit_container(self, node):
        classes = "docutils container"
        if node.get("is_div", False):
            # we don't want the CSS for container for these nodes
            classes = "docutils"
        self.body.append(self.starttag(node, "div", CLASS=classes))

    def depart_container(self, node):
        self.body.append("</div>\n")

    # we override container html visitors, to stop the default behaviour
    # of adding the `container` class to all nodes.container
    app.add_node(
        nodes.container, override=True, html=(visit_container, depart_container)
    )
    ###########################################################################

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
