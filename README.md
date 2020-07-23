# Sphinx sources for fatiando.org

[![build-html](https://github.com/fatiando/website/workflows/build-html/badge.svg?event=push)](https://github.com/fatiando/website/actions?query=workflow%3Abuild-html)

## Compiling the site

Run:

    make

Pushing changes to
[fatiando/website](https://github.com/fatiando/website)
triggers a build on GitHub Actions.
The build will check if the site compiles and also checks for broken links.
When changes are pushed to the `master` branch (directly or by merging a Pull
Request), Actions will push the compiled site to the
[fatiando/fatiando.github.io](https://github.com/fatiando/fatiando.github.io)
repository.
GitHub serves this repository under
[http://fatiando.github.io](http://fatiando.github.io/).
See `.github/workflows/build.yml`.

## Logo fonts

The font used in the front page banner is EB Garamond.

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).
