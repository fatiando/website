"""
Use livereload to serve, build, and reload the website when files change.
"""
from livereload import Server, shell


server = Server()
files = ["**/**.rst", "**/**.md", "conf.py", "_static/", "_templates/", "theme/"]
for filename in files:
    server.watch(filename, "make html")
server.serve(root="_build/html", host="localhost", open_url_delay=1)
