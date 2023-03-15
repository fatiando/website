"""
Sphinx extension for inserting listing users in Fatiando governance roles

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

__version__ = "0.1.0"


def _get_user_info(handle):
    """
    Returns a dict with information of a GitHub user
    """
    response = requests.get(f"https://api.github.com/users/{handle}")
    response.raise_for_status()
    data = json.loads(response.text)
    return data


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
    return [handle for _, handle in authors]


def _make_card_list(group):
    col_classes = "col-4 col-sm-3 col-md-2 d-flex align-items-stretch".split()
    row_classes = "row gy-3 gx-2".split()
    # Use is_div=True in our containers to stop docutils inserting the
    # "container" class. Based on code from sphinx-panels.
    row = nodes.container(is_div=True, classes=row_classes)
    for user in group:
        col = nodes.container(is_div=True, classes=col_classes)
        card = nodes.container(is_div=True, classes=["card"])
        card += nodes.image(
            uri=user["avatar_url"],
            alt=f"Profile picture of {user['name']}",
            classes=["card-img-top"],
        )
        card_body = nodes.container(
            is_div=True, classes=["card-body", "text-center"]
        )
        card_title = nodes.paragraph(classes="card-title fs-6 fw-bold".split())
        card_title += nodes.Text(user["name"])
        card_title += nodes.Text()
        card_body += card_title
        card_text = nodes.paragraph(classes="card-text text-muted fs-6".split())
        card_text += nodes.reference(
            text=f"@{handle}", refuri=f"https://github.com/{handle}"
        )
        card_body += card_text
        card += card_body
        col += card
        row += col
    return row


def _make_authors_tabs(authors_per_package):
    index = nodes.bullet_list(classes="nav nav-pills mb-3".split(), ids=["authors-tab"], roles=["tablist"])
    return index


"""
<ul class="nav nav-pills mb-3" id="authors-tab" role="tablist">
  <li class="nav-item" role="presentation">
    <button
        class="nav-link active"
        id="authors-harmonica-tab"
        data-bs-toggle="pill"
        data-bs-target="#authors-harmonica"
        type="button"
        role="tab"
        aria-controls="authors-harmonica"
        aria-selected="true"
        aria-label="Harmonica"
    >
    <i class="fa fa-users"></i>
    Harmonica
    </button>
  </li>
</ul>
<div class="tab-content" id="authors-tabContent">
  <div
      class="tab-pane fade show active"
      id="authors-harmonica"
      role="tabpanel"
      aria-labelledby="authors-harmonica-tab"
  >

```{fatiando-authors} harmonica
```

  </div>
</div>
"""



class AuthorsDirective(Directive):
    """
    The fatiando-authors directive.
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "exclude": directives.unchanged,
        "branch": directives.unchanged,
    }

    def run(self):
        packages = self.arguments[0].split(",")
        authors_info = {}
        authors_per_package = {}
        for package in packages:
            handles = _parse_authors_file(package)
            authors_per_package[package] = []
            for handle in handles:
                if handle not in authors_info:

                    authors_info[handle] = _get_user_info(handle)
                authors_per_package[package].append(authors_info[handle])
        tabs = _make_authors_tabs(authors_per_package)
        return [tabs]


def setup(app):
    app.add_directive("fatiando-authors", AuthorsDirective)

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
