# Sphinx sources for fatiando.org

[![TravisCI status](http://img.shields.io/travis/fatiando/website.svg?style=flat)](https://travis-ci.org/fatiando/website)

## Compiling the site

Run:

    make

Pushing changes to
[fatiando/website](https://github.com/fatiando/website)
triggers a build on [TravisCI](https://travis-ci.org/fatiando/website).
The build will check if the site compiles and also checks for broken links.
When changes are pushed to the `master` branch (directly or by merging a Pull
Request), Travis will push the compiled site to the
[fatiando/fatiando.github.io](https://github.com/fatiando/fatiando.github.io)
repository.
Github serves this repo under
[http://fatiando.github.io](http://fatiando.github.io/).

Pushing the changes from Travis is handled by the scripts in the `ci` folder.

## Logo fonts

The font used in the front page banner is El Messiri and the one in the navbar is
ABeeZee.

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).
