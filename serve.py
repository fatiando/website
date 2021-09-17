"""
Use livereload to serve, build, and reload the website when files change.
"""
from livereload import Server, shell

FATIANDO_PROJECTS = "pooch verde harmonica boule".split()


def ignore_authors_files(filepath):
    for project in FATIANDO_PROJECTS:
        if f"{project}-authors.md" in filepath:
            return True
    return False


server = Server()
files = ["**/**.rst", "**/**.md", "conf.py", "_static/", "_templates/", "theme/"]
for filename in files:
    server.watch(filename, "make clean html", ignore=ignore_authors_files)
server.serve(root="_build/html", host="localhost", open_url_delay=1)
