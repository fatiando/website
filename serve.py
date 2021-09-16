"""
Use livereload to serve, build, and reload the website when files change.
"""
from livereload import Server, shell


def ignore_authors(filepath):
    projects = "pooch verde harmonica boule".split()
    for project in projects:
        if f"{project}-authors.md" in filepath:
            return True
    return False


server = Server()
files = [
    "**/**.rst",
    "**/**.md",
    "conf.py",
    "get_authors.py",
    "_static/",
    "_templates/",
    "theme/",
]
for filename in files:
    server.watch(filename, "make clean html", ignore=ignore_authors)
server.serve(root="_build/html", host="localhost", open_url_delay=1)
