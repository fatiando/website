# Sphinx sources for fatiando.org

[![TravisCI status](http://img.shields.io/travis/fatiando/website.svg?style=flat)](https://travis-ci.org/fatiando/website)

## Requirements

* Sphinx
* matplotlib

To install using pip:

    pip install sphinx matplotlib

If you have [Anaconda](http://docs.continuum.io/anaconda/index.html), both
packages should already be installed.

## Compiling the site

Just run:

    make

To preview the site, run:

    make serve

This will start a local server on port 8005.
Point your web browser to [http://127.0.0.1:8005/](http://127.0.0.1:8005/) to
view the site.
Use `Ctrl+C` to shut down the server.

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

Pushing the changes from Travis is handled by the `.update-website.sh` script.
See the posts by
[Sleepy Coders](http://sleepycoders.blogspot.com.au/2013/03/sharing-travis-ci-generated-files.html)
and
[Mathieu Leplatre](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html)
for details on how this works.

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).
