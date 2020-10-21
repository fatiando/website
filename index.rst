.. title:: Fatiando a Terra

.. _about:

About
=========================================

.. raw:: html

   <div class="row text-center">
      <div class="col-sm-4">
         <h2><i class="fas fa-toolbox fa-2x"></i></h2>
         <b>Open-source</b>
         <br>
         We develop Python packages for Geophysics data processing, modeling, and more.
      </div>
      <div class="col-sm-4">
         <h2><i class="fas fa-drafting-compass fa-2x"></i></h2>
         <b>Carefully designed and tested</b>
         <br>
         Our software strictly follows development best practices.
      </div>
      <div class="col-sm-4">
         <h2><i class="fas fa-copy fa-2x"></i></h2>
         <b>Comprehensive documentation</b>
         <br>
         Tutorials, examples, theory, and real data applications.
      </div>
   </div>

.. raw:: html

   <div class="gallery text-center">
      <div class="row">
         <div class="col-sm-6">
            <div class="row">
               <div class="col-xs-6 gallery-img">
                  <a target="_blank" href="https://www.fatiando.org/harmonica/latest/gallery/gravity_disturbance.html">
                  <img src="_static/gallery/gallery-disturbance.jpg">
                  </a>
               </div>
               <div class="col-xs-6 gallery-img">
                  <a target="_blank" href="https://www.fatiando.org/rockhound/latest/gallery/bedmap2.html">
                  <img src="_static/gallery/gallery-bedmap.jpg">
                  </a>
               </div>
            </div>
         </div>
         <div class="col-sm-6">
            <div class="row">
               <div class="col-xs-6 gallery-img">
                  <a target="_blank" href="https://www.fatiando.org/verde/latest/gallery/blockreduce.html">
                  <img src="_static/gallery/gallery-blockmean.jpg">
                  </a>
               </div>
               <div class="col-xs-6 gallery-img">
                  <a target="_blank" href="https://www.fatiando.org/rockhound/latest/gallery/seafloor_age.html">
                  <img src="_static/gallery/gallery-seafloorage.jpg">
                  </a>
               </div>
            </div>
         </div>
      </div>
   </div>

.. _projects:

The Tools
=============

We maintain several Python projects which are in various stages of development: from
early design to polished and published products. We'll also be adding new projects to
our toolkit in the future (see how you can :ref:`get involved <contribute>`).

.. raw:: html

   <div class="row">

      <div class="col-sm-6 project">

         <a href="http://www.fatiando.org/verde">
            <img class="project-logo center-block" src="_static/verde-logo.svg">
         </a>

         <p>
         Spatial data processing and interpolation (<b>gridding</b>) using
         Green's functions (or radial basis functions) with a
         machine learning inspired interface.
         </p>

         <a href="https://pypi.python.org/pypi/verde">
         <img src="https://img.shields.io/pypi/v/verde.svg?style=flat-square"
              alt="Latest release on PyPI">
         </a>
         <a href="https://pypi.python.org/pypi/verde">
         <img src="https://img.shields.io/pypi/pyversions/verde.svg?style=flat-square"
              alt="Compatible Python versions">
         </a>

         <ul class="fa-ul project-icons">
            <li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
               <a href="https://github.com/fatiando/verde">fatiando/verde</a>
            </li>
            <li><i class="fa-li fa fa-book fa-fw" title="Documentation"></i>
               <a href="http://www.fatiando.org/verde">www.fatiando.org/verde</a>
            </li>
            <li><i class="fa-li fas fa-bookmark fa-fw" title="Publication"></i>
               doi: <a href="https://doi.org/10.21105/joss.00957">10.21105/joss.00957</a>
            </li>
            <li><i class="fa-li fa fa-check fa-fw" style="color: green" title="Project status"></i>
               Stable and ready for use
            </li>
         </ul>

      </div>

      <div class="col-sm-6 project">

         <a href="http://www.fatiando.org/pooch">
            <img class="project-logo center-block" src="_static/pooch-logo.svg">
         </a>

         <p>
         Manages the <b>download of data</b> files from a server, storing them
         in a local directory, and handling updates if required. Used by our
         other libraries.
         </p>

         <a href="https://pypi.python.org/pypi/pooch">
         <img src="https://img.shields.io/pypi/v/pooch.svg?style=flat-square"
              alt="Latest release on PyPI">
         </a>
         <a href="https://pypi.python.org/pypi/pooch">
         <img src="https://img.shields.io/pypi/pyversions/pooch.svg?style=flat-square"
              alt="Compatible Python versions">
         </a>

         <ul class="fa-ul project-icons">
            <li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
               <a href="https://github.com/fatiando/pooch">fatiando/pooch</a>
            </li>
            <li><i class="fa-li fa fa-book fa-fw" title="Documentation"></i>
               <a href="http://www.fatiando.org/pooch">www.fatiando.org/pooch</a>
            </li>
            <li><i class="fa-li fas fa-bookmark fa-fw" title="Publication"></i>
               doi: <a href="https://doi.org/10.21105/joss.01943">10.21105/joss.01943</a>
            </li>
            <li><i class="fa-li fa fa-check fa-fw" style="color: green" title="Project status"></i>
               Stable and ready for use
            </li>
         </ul>

      </div>

   </div>

   <div class="row">

      <div class="col-sm-6 project">

         <a href="http://www.fatiando.org/harmonica">
            <img class="project-logo center-block" src="_static/harmonica-logo.svg">
         </a>

         <p>
         Processing and modeling <b>gravity</b> and <b>magnetic</b> data, like terrain
         correction, upward continuation, equivalent layers, 3D inversion, and more.
         </p>

         <a href="https://pypi.python.org/pypi/harmonica">
         <img src="https://img.shields.io/pypi/v/harmonica.svg?style=flat-square"
              alt="Latest release on PyPI">
         </a>
         <a href="https://pypi.python.org/pypi/harmonica">
         <img src="https://img.shields.io/pypi/pyversions/harmonica.svg?style=flat-square"
              alt="Compatible Python versions">
         </a>

         <ul class="fa-ul project-icons">
            <li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
               <a href="https://github.com/fatiando/harmonica">fatiando/harmonica</a>
            </li>
            <li><i class="fa-li fa fa-book fa-fw" title="Documentation"></i>
               <a href="http://www.fatiando.org/harmonica">www.fatiando.org/harmonica</a>
            </li>
            <li><i class="fa-li fa fa-sync-alt fa-fw" style="color: green" title="Project status"></i>
               Ready for use but still changing
            </li>
         </ul>

      </div>

      <div class="col-sm-6 project">

         <a href="http://www.fatiando.org/boule">
            <img class="project-logo center-block" src="_static/boule-logo.svg">
         </a>

         <p>
         Reference <b>ellipsoids</b> for geodesy and geophysics. Calculates
         <b>Normal gravity</b> and coordinate conversions for the Earth and
         other plantery bodies.
         </p>

         <a href="https://pypi.python.org/pypi/boule">
         <img src="https://img.shields.io/pypi/v/boule.svg?style=flat-square"
              alt="Latest release on PyPI">
         </a>
         <a href="https://pypi.python.org/pypi/boule">
         <img src="https://img.shields.io/pypi/pyversions/boule.svg?style=flat-square"
              alt="Compatible Python versions">
         </a>

         <ul class="fa-ul project-icons">
            <li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
               <a href="https://github.com/fatiando/boule">fatiando/boule</a>
            </li>
            <li><i class="fa-li fa fa-book fa-fw" title="Documentation"></i>
               <a href="http://www.fatiando.org/boule">www.fatiando.org/boule</a>
            </li>
            <li><i class="fa-li fa fa-sync-alt fa-fw" style="color: green" title="Project status"></i>
               Ready for use but still changing
            </li>
         </ul>

      </div>

  </div>

   <div class="row">

      <div class="col-sm-6 project">

         <a href="http://www.fatiando.org/rockhound">
            <img class="project-logo center-block" src="_static/rockhound-logo.svg">
         </a>

         <p>
         Download geophysical models and datasets (PREM, CRUST1.0, ETOPO1) and load them
         into Python. Relies on Pooch to manage the downloads.
         </p>

         <a href="https://pypi.python.org/pypi/rockhound">
         <img src="https://img.shields.io/pypi/v/rockhound.svg?style=flat-square"
              alt="Latest release on PyPI">
         </a>
         <a href="https://pypi.python.org/pypi/rockhound">
         <img src="https://img.shields.io/pypi/pyversions/rockhound.svg?style=flat-square"
              alt="Compatible Python versions">
         </a>

         <ul class="fa-ul project-icons">
            <li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
               <a href="https://github.com/fatiando/rockhound">fatiando/rockhound</a>
            </li>
            <li><i class="fa-li fa fa-book fa-fw" title="Documentation"></i>
               <a href="http://www.fatiando.org/rockhound">www.fatiando.org/rockhound</a>
            </li>
            <li><i class="fa-li fa fa-sync-alt fa-fw" style="color: green" title="Project status"></i>
               Ready for use but still changing
            </li>
         </ul>

      </div>

      <div class="col-sm-6 project">
      </div>

   </div>



.. _started:

Getting Started
===============


To use Fatiando tools, we recommend using the `Anaconda Python distribution <https://www.anaconda.com/products/individual>`__
to ensure you have all dependencies installed.
We recommend `Software Carpentry instructions <https://carpentries.github.io/workshop-template/#python>`__
for Anaconda installation.

So, you can install all the latest Fatiando tools with a single command:

.. raw:: html

   <code>
      conda install verde harmonica rockhound boule  --channel conda-forge
   </code>

Alternatively, you can also use the `pip package manager <https://pypi.org/project/pip/>`__:

.. raw:: html

   <code>
      pip install verde harmonica rockhound boule
   </code>

.. raw:: html

    <h2><i class="fas fa-rocket"></i> New to Python?</h2>

If you don't have so much experience with Python language, **don't worry!**.
We recommend you the `Software Carpentry lessons <https://software-carpentry.org/lessons/>`__.
These are a really great for starting to learn Python for scientific computation.

.. raw:: html

   <ul class="fa-ul icon-list-small">
      <li>
         <i class="fa-li fa fa-book fa-fw"></i>
         <a href="https://swcarpentry.github.io/python-novice-inflammation/">Programming with Python</a>
      </li>
      <li>
         <i class="fa-li fa fa-book fa-fw"></i>
         <a href="https://swcarpentry.github.io/python-novice-gapminder/">Plotting and Programming in Python</a>
      </li>
   </ul>



.. _support:

Support Fatiando
================


All Fatiando projects are **made by scientists and volunteers** who generously donate
their time and attention. Here are some of the ways in which you can help support the
project and give back to the community:

.. raw:: html

   <div class="row text-center">
      <div class="col-sm-4">
         <h2><i class="fas fa-users fa-2x"></i></h2>
         <b>Join the community</b>
         <br>
         Get involved in our projects and help shape their future. See below how you
         can <a href="#contact">participate in the conversation</a> and
         <a href="#contribute">make contributions</a>.
      </div>
      <div class="col-sm-4">
         <h2><i class="fas fa-share-alt fa-2x"></i></h2>
         <b>Spread the word</b>
         <br>
         Share links in social media, publish your analysis
         code that uses Fatiando, include our logo in talks and posters (sources in
         <a href="https://github.com/fatiando/logo"><i class="fab fa-github"></i>
         fatiando/logo</a>), etc.
      </div>
      <div class="col-sm-4">
         <h2><i class="fas fa-bookmark fa-2x"></i></h2>
         <b>Cite the projects</b>
         <br>
         Citations help us justify the effort that goes into building and maintaining
         this project.
         There are
         <a href="https://github.com/fatiando/verde/blob/master/CITATION.rst">CITATION.rst</a>
         files in each project explaining how to cite it (and also a page in the
         documentation).
      </div>
   </div>



.. _contact:

Contacting Us
=============

.. raw:: html

   <div class="row text-center">
      <div class="col-sm-4">
         <h2><i class="fab fa-github fa-2x"></i></h2>
         Most discussions happen on <a href="https://github.com/fatiando">Github</a>.
         <a href="https://github.com/fatiando/contributing/blob/master/CONTRIBUTING.md#reporting-a-bug">Open
         an issue</a> to <strong>report bugs</strong> and <strong>request features</strong>.
         Leave a comment on any open issue or pull request to join the
         conversation.
      </div>
      <div class="col-sm-4">
         <h2><i class="fab fa-slack fa-2x"></i></h2>
         Hop on to our <a href="http://contact.fatiando.org">chat room on Slack</a>
         where you can <strong>ask questions</strong>, leave comments, and
         reach out to users and developers.
      </div>
      <div class="col-sm-4">
         <h2><i class="fab fa-twitter fa-2x"></i></h2>
         Follow us on Twitter <a href="https://twitter.com/fatiandoaterra">@fatiandoaterra</a>
         where we post occasional <strong>updates</strong> about the project.
      </div>
   </div>


.. _contribute:

Getting Involved
================

**We want your help!**
Fatiando is a **community-developed** project, so it's people like you that
make it useful and successful.

.. raw:: html

    <h2><i class="fa fa-comments"></i> Participate in the community</h2>

**Open-source is more than just code, it's about the people involved**.
The most important thing you can do for any project is participate in the
community: ask and answer questions, share your experience, help guide the
development, and make friends along the way.


**IMPORTANT:** Everyone is expected to abide by our
`Code of Conduct <https://github.com/fatiando/contributing/blob/master/CODE_OF_CONDUCT.md>`__
when participating in the Fatiando community. Please review it carefully.

The Fatiando community gathers in a few different places, **all of which are
completely open to everyone**. So come along and join the conversation:

.. raw:: html

   <ul class="fa-ul icon-list-small">
      <li>
      <i class="fa-li fab fa-slack fa-fw"></i> <a href="http://contact.fatiando.org/">Slack</a>:
      where most conversation happens about meetings, events, questions, etc.
      </li>
      <li>
      <i class="fa-li fab fa-github fa-fw"></i> <a href="https://github.com/fatiando/">GitHub</a>:
      where we discuss development details, review code, etc.
      </li>
      <li>
      <i class="fa-li fa fa-microphone-alt fa-fw"></i> <a href="https://github.com/fatiando/meeting-notes">Community Calls</a>:
      regular video calls to discuss the latest developments, project
      directions, and have a little social interaction. <strong>We welcome everyone
      interested in Fatiando to take part!</strong> Calls happen once a month (check
      <a href="http://calendar.fatiando.org">our calendar</a> for the next one)
      and are live-streamed to
      <a href="https://www.youtube.com/FatiandoOrg">our YouTube channel</a>.
      Check the <a href="https://github.com/fatiando/meeting-notes">meeting notes</a>
      for more information.
      <br>
      <div class="embed-responsive embed-responsive-16by9 youtube">
      <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/videoseries?list=PLPA_RM8wsOqIEBLICo3v7f_A1WnLcwJld" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
      </li>
   </ul>

.. raw:: html

    <h2><i class="fa fa-cog"></i> Join the development</h2>

There may be a little voice inside your head that is telling you that you're
not ready; that your skills aren't nearly good
enough to contribute.
What could you possibly offer?
We assure you that the little voice in your head is wrong.

**Being a contributor doesn't just mean writing code**.
There are many ways to contribute:

.. raw:: html

   <ul class="fa-ul icon-list-small">
      <li><i class="fa-li fa fa-bug fa-fw"></i> Submitting bug reports and feature requests</li>
      <li><i class="fa-li fa fa-book fa-fw"></i> Writing tutorials or examples</li>
      <li><i class="fa-li fa fa-hammer fa-fw"></i> Fixing typos and improving to the documentation</li>
      <li><i class="fa-li fa fa-terminal fa-fw"></i> Writing code for everyone to use</li>
   </ul>

.. raw:: html

   Have a look at our
   <a href="https://github.com/fatiando/contributing/blob/master/CONTRIBUTING.md">Contributing Guide</a>
   to see how you can get involved.
   This and other guides (for project maintenance, etc.) can be found in the
   <a href="https://github.com/fatiando/contributing"><i class="fab fa-github"></i> fatiando/contributing</a> repository.



Looking for the ``fatiando`` package?
=====================================

**It still exists!**
While development of the ``fatiando`` library has stopped (in favor of
:ref:`our new libraries <projects>`),
you can still view the
`documentation for the last release (v0.5) <https://www.fatiando.org/v0.5/>`__
and the `source code archive on Github <https://github.com/fatiando/fatiando>`__.
The library will remain archived and usable for the foreseeable future.
To get a sense for the reasoning behind the choice to abandon ``fatiando``, please read
`this blog post <http://www.leouieda.com/blog/future-of-fatiando.html>`__.
