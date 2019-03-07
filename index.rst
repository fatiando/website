.. title:: Fatiando a Terra

.. _about:

Python solutions for geophysical problems
=========================================

**Fatiando** is a collection of open-source `Python <https://www.python.org/>`__
packages for Geophysics.
Our toolkit includes code for processing geophysical data, forward and inverse
modeling, interpolation, and more.

We are committed to providing well crafted and trustworthy software. As such, all of our
core packages strictly follow **software development best practices:**

.. raw:: html

   <ul class="fa-ul icon-list">
      <li><i class="fa-li fas fa-vial fa-fw"></i>
         <b>Full suite of tests</b> for every part of the code base. Tests are run
         automatically every time a change is made and new features must include tests
         before being integrated.
      </li>

      <li><i class="fa-li fas fa-book fa-fw"></i>
         <b>Extensive documentation</b> including tutorials, example galleries, and
         reference documentation for functions and classes. As well as tests, we also
         require new features to be fully documented.
      </li>

      <li><i class="fa-li fas fa-search fa-fw"></i>
         <b>Carefully designed interfaces</b> for our functions and classes are debated
         and experimented on widely to make them as user-friendly as possible. We also
         focus on promoting best practices in geophysical data analysis through the
         design of our software.
      </li>

      <li><i class="fa-li fas fa-door-open fa-fw"></i>
         <b>Open development</b> through <a href="https://github.com/fatiando">Github</a>
         allows anyone to participate in our discussions, contribute their own ideas,
         and track changes made to the software since its inception.
      </li>
   </ul>


.. _projects:

The Libraries
=============

We maintain several Python libraries which are in various stages of development: from
early design to polished and published products. We'll also be adding new projects to
our toolkit in the future (see how you can :ref:`get involved <contribute>`).

.. raw:: html

   <div class="row">

      <div class="col-md-6 project">

         <img class="project-logo" src="_static/verde-logo.svg">

         <p>
         Spatial data processing and interpolation (<b>gridding</b>) using
         Green's functions (or radial basis functions) with a
         machine learning interface.
         </p>

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

      <div class="col-md-6 project">

         <img class="project-logo" src="_static/harmonica-logo.svg">

         <p>
         Processing and modeling <b>gravity</b> and <b>magnetic</b> data, like terrain
         correction, upward continuation, equivalent layers, modeling, and more.
         </p>

         <ul class="fa-ul project-icons">
            <li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
               <a href="https://github.com/fatiando/harmonica">fatiando/harmonica</a>
            </li>
            <li><i class="fa-li fa fa-book fa-fw" title="Documentation"></i>
               <a href="http://www.fatiando.org/harmonica/dev">www.fatiando.org/harmonica/dev</a>
            </li>
            <li><i class="fa-li fa fa-flask fa-fw" style="color: orange" title="Project status"></i>
               Early development and design
            </li>
         </ul>

      </div>

   </div>

   <div class="row">

      <div class="col-md-6 project">

         <img class="project-logo" src="_static/pooch-logo.svg">

         <p>
         Manages downloading sample data files over HTTP from a server and storing
         them in a local directory. Used by our other libraries.
         </p>

         <ul class="fa-ul project-icons">
            <li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
               <a href="https://github.com/fatiando/pooch">fatiando/pooch</a>
            </li>
            <li><i class="fa-li fa fa-book fa-fw" title="Documentation"></i>
               <a href="http://www.fatiando.org/pooch">www.fatiando.org/pooch</a>
            </li>
            <li><i class="fa-li fa fa-sync-alt fa-fw" style="color: green" title="Project status"></i>
               Ready for use but still changing
            </li>
         </ul>

      </div>

      <div class="col-md-6 project">

         <img class="project-logo" src="_static/rockhound-logo.svg">

         <p>
         Download geophysical models and datasets (PREM, CRUST1.0, ETOPO1) and load them
         into Python. Relies on Pooch to manage the downloads.
         </p>

         <ul class="fa-ul project-icons">
            <li><i class="fa-li fab fa-github fa-fw" title="Github repository"></i>
               <a href="https://github.com/fatiando/rockhound">fatiando/rockhound</a>
            </li>
            <li><i class="fa-li fa fa-book fa-fw" title="Documentation"></i>
               <a href="http://www.fatiando.org/rockhound/dev">www.fatiando.org/rockhound/dev</a>
            </li>
            <li><i class="fa-li fa fa-flask fa-fw" style="color: orange" title="Project status"></i>
               Early development and design
            </li>
         </ul>

      </div>

   </div>


.. _support:

Support Fatiando
================


All Fatiando projects are **made by scientists and volunteers** who are generous enough
to donate their time and attention. Here are some of the ways in which you can help
support the project and give back to the community:

.. raw:: html

   <ul class="fa-ul icon-list">
      <li><i class="fa-li fas fa-bookmark fa-fw"></i>
         <b>Cite the projects</b> in papers, presentations, etc. Citations help us
         justify the effort that goes into building and maintaining this project. If you
         used any of our libraries in your research, please consider citing it. There
         are <a href="https://github.com/fatiando/verde/blob/master/CITATION.rst"><span class="pre">CITATION.rst</span></a>
         files in each released project repository explaining how to cite it (and also a
         page in the documentation).
      </li>

      <li><i class="fa-li fas fa-share-alt fa-fw"></i>
         <b>Spread the word</b> by sharing links in social media, publishing your analysis
         code that uses Fatiando, including our logo in talks and posters (sources in
         <a href="https://github.com/fatiando/logo"><i class="fab fa-github"></i>
         fatiando/logo</a>), etc.
      </li>

      <li><i class="fa-li fas fa-users fa-fw"></i>
         <b>Join the community</b> by getting involved in the project. See below how you
         can <a href="#contact">participate in the conversion</a> and
         <a href="#contribute">contribute to the project</a>.
      </li>
   </ul>


.. _contact:

Contacting Us
=============

.. raw:: html

   <ul class="fa-ul icon-list">
      <li><i class="fa-li fab fa-github fa-fw"></i>
         Most discussion happens on <a href="https://github.com/fatiando">Github</a>.
         Please feel free to
         <a href="https://github.com/fatiando/contributing/blob/master/CONTRIBUTING.md#reporting-a-bug">open
         an issue</a> to report a bug or request a new feature. You can also leave a
         comment on any open issue or pull request.
      </li>

      <li><i class="fa-li fab fa-gitter fa-fw"></i>
         We have <a href="https://gitter.im/fatiando/fatiando">chat room on Gitter</a>
         where you can ask questions and leave comments.
      </li>

      <li><i class="fa-li fa fa-envelope-open-text fa-fw"></i>
         Our <a href="https://groups.google.com/d/forum/fatiando">Google Groups mailing
         list</a> is also used to answer questions and post announcements. When you sign
         up, please <b>remember to choose an email delivery option</b> (sadly the
         default is "no emails").
      </li>

      <li><i class="fa-li fab fa-twitter fa-fw"></i>
         You can follow us on Twitter <a href="https://twitter.com/fatiandoaterra">@fatiandoaterra</a>
         where we post occasional updates about the project. Feel free to @-mention to
         ask questions or get in touch.
      </li>
   </ul>


.. _contribute:

Getting Involved
================

Fatiando is a **community-driven** project, so it's people like you that make it useful
and successful. There are many ways to contribute:

.. raw:: html

   <ul class="fa-ul icon-list">
      <li><i class="fa-li fa fa-bug fa-fw"></i> Submitting bug reports and feature requests</li>
      <li><i class="fa-li fa fa-book fa-fw"></i> Writing tutorials or examples</li>
      <li><i class="fa-li fa fa-hammer fa-fw"></i> Fixing typos and improving to the documentation</li>
      <li><i class="fa-li fa fa-terminal fa-fw"></i> Writing code for everyone to use</li>
   </ul>

.. raw:: html

   Have a look at our
   <a href="https://github.com/fatiando/contributing/blob/master/CONTRIBUTING.md">Contributing Guide</a>
   to see how you can help and give feedback.
   This and other guides (for project maintenance, etc.) can be found in the
   <a href="https://github.com/fatiando/contributing"><i class="fab fa-github"></i> fatiando/contributing</a> repository.


Code of Conduct
---------------

All Fatiando projects are released with a
`Contributor Code of Conduct <https://github.com/fatiando/contributing/blob/master/CODE_OF_CONDUCT.md>`__.
By participating in any of these projects you agree to abide by its terms.

Imposter Syndrome Disclaimer
----------------------------

**We want your help.** No, really.

There may be a little voice inside your head that is telling you that you're
not ready to be an open source contributor; that your skills aren't nearly good
enough to contribute.
What could you possibly offer?

We assure you that the little voice in your head is wrong.

**Being a contributor doesn't just mean writing code**.
Equality important contributions include:
writing or proof-reading documentation, suggesting or implementing tests, or
even giving feedback about the project (including giving feedback about the
contribution process).
If you're coming to the project with fresh eyes, you might see the errors and
assumptions that seasoned contributors have glossed over.
If you can write any code at all, you can contribute code to open source.
We are constantly trying out new skills, making mistakes, and learning from
those mistakes.
That's how we all improve and we are happy to help others learn.


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
Quoting from it:

   Back [when we started Fatiando], there were very few Python geophysical modeling
   libraries. A decade later, the ecosystem has expanded. The five currently on going
   projects of which I'm aware are:

   * `PyGMI <https://github.com/Patrick-Cole/pygmi>`__: GUI + library for 3D modeling
     of gravity and magnetic data.
   * `SimPEG <http://simpeg.xyz/>`__: Forward modeling and inversion library based on
     the finite volume method.
   * `pyGIMLi <https://www.pygimli.org/>`__: Forward modeling and inversion library
     based on the finite element and finite volume methods.
   * `Bruges <https://github.com/agile-geoscience/bruges>`__: Modeling and processing
     for seismic and petrophysics.
   * `Pyrocko <https://pyrocko.org>`__: A collection of tools and libraries, mostly
     for seismology.

   The two projects that are most similar to us (SimPEG and pyGIMLi) implement flexible
   partial differential equation solvers that they use to run all forward modeling
   calculations. This makes a lot of sense because it gives them a unified framework to
   model most geophysical methods. It is the most sensible approach to build joint
   inversions of multiple geophysical datasets. However, there are some inverse problems
   that don't fit this paradigm, like inverting Moho relief from gravity data and some
   non-conventional inversion algorithms [...]

   [...]

   The niche I see for Fatiando is in gravity and magnetic methods, particularly using
   [analytical solutions for forward modeling and non-PDE based inversions]. The
   processing functions are an important feature because there are hardly any
   open-source alternatives out there to commercial software like Oasis Montaj and
   Intrepid.

   [...]

   The best way forward for Fatiando that I can see, is to become an ecosystem of
   specialized tools and libraries, rather than a single Python package. Having things
   in separate libraries allows us to better indicate what is robust and professional
   and what is experimental or meant as a teaching tool.
