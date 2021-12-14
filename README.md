# Sphinx sources for fatiando.org

[![build-html](https://github.com/fatiando/website/workflows/build-html/badge.svg?event=push)](https://github.com/fatiando/website/actions?query=workflow%3Abuild-html)

## Dependencies

The website is build with [Sphinx](https://www.sphinx-doc.org/), the same tool
we use to generate our documentation. So if you know how to edit the docs, you
know how to contribute to this website as well.

To set up your development environment, create a conda environment from the
`environment.yml` file in this repository (assuming you have some version of
Anaconda/Miniconda/Miniforge installed):

```
conda env create
conda activate fatiando-website
```

The sources can be the standard reStructuredText (`.rst`) that Sphinx uses or
Markdown (`.md`) thanks to the [MyST](https://myst-parser.readthedocs.io)
parser.
We use Markdown most of the time because it simplifies adding HTML directly to
the source document, which we often do for styling and fancy layouts.

## Contributing

Run `make serve` to generate the HTML files, serve them, and open your default
browser. This command will keep serving the pages and re-building them
automatically any time a source file changes. You don't even have to refresh
your browser. To stop the server, type `Control + C`.

* If you add any new pages, make sure they are included in the `toctree` entry
  at the top of `index.md`.
* The preferred format for sources is Markdown but RST will be acceptable if
  you have a reason for it.
* Navigation bar (menu) items are defined in `conf.py`.
* The template is custom made and can be modified by editing
  `_templates/layout.html`.
* The main CSS stylesheet is `_static/css/style.css`.
* We use [Bootstrap 5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
  (just the CSS, not the Javascript components).

### Forwarding

We use the HTML files in the `forward` folder to redirect to other domains.
This is not ideal but our DNS-based forwarding doesn't work with HTTPS (if you
know a way around this, please let us know!).

The files are copied to the output folder (`forward/dev/ -> _build/html/dev`
which is served as `fatiando.org/dev`).
To add a forward, create a new folder with an `index.html` similar to the ones
we already include.

**Use only for long and difficult to type URLs.**

## Deployment

Pushing changes to [fatiando/website](https://github.com/fatiando/website)
triggers a build on GitHub Actions.
The build will check if the site compiles and also checks for broken links.
When changes are pushed to the `master` branch (directly or by merging a Pull
Request), Actions will push the compiled site to the
[fatiando/fatiando.github.io](https://github.com/fatiando/fatiando.github.io)
repository.
GitHub serves this repository under
[http://fatiando.github.io](http://fatiando.github.io/).
See `.github/workflows/build.yml`.

## License

[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
