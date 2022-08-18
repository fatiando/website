"""
Sphinx extension for inserting a link to the latest release on PyPI
"""
import re
import json
import requests
import packaging.version
from docutils import nodes

__version__ = "0.1.0"


def pypi_version(name, rawtext, text, lineno, inliner, options=None, content=None):
    """
    Create a link to the latest version of a package on PyPI.

    The text for the role should be "package" or "text <package>". The package
    name or "<package>" will be replaced by the latest version number.
    """
    arguments = re.findall(r"\<(.+?)\>", text)
    if len(arguments) > 1:
        raise ValueError("Invalid pypi_version role: rawtext")
    elif arguments:
        package = arguments[0]
        placeholder = f"<{package}>"
    else:
        package = text
        placeholder = package
    url = f"https://pypi.org/pypi/{package}/json"
    response = requests.get(url)
    response.raise_for_status()
    releases = [
        packaging.version.parse(v)
        for v in json.loads(response.text).get("releases", [])
    ]
    version = max(releases)
    node = nodes.reference(
        text=text.replace(placeholder, str(version)),
        refuri=f"https://pypi.org/project/{package}",
    )
    return [node], []


def setup(app):
    "Register the new role with sphinx"
    app.add_role("pypi_version", pypi_version)
    return {"version": __version__}
