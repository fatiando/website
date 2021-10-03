# About

<div class="lead">
<em>Fatiando a Terra</em> is a collection of <strong>open-source Python
packages</strong> aimed primarily at Geophysics (though not exclusively).
This page contains some information about the project, our community, and its
history.
</div>

```{admonition} Trivia
*Fatiando a Terra* is Portuguese for *Slicing the Earth*, a reference to the
project's Brazilian origins and ambitious initial goals to model the whole
planet.
```


## Who we are

Fatiando tools are developed by **working geoscientists and community
volunteers** from across the globe.

### Authors

The [GitHub repositories][gh] for each project contain `AUTHORS.md` files which
list everyone involved:


<ul class="nav nav-pills mb-3" id="authors-tab" role="tablist">
  <li class="nav-item" role="presentation">
    <button
        class="nav-link active"
        id="authors-harmonica-tab"
        data-bs-toggle="pill"
        data-bs-target="#authors-harmonica"
        type="button"
        role="tab"
        aria-controls="authors-harmonica"
        aria-selected="true"
        aria-label="Harmonica"
    >
    <i class="fa fa-users"></i>
    Harmonica
    </button>
  </li>
  <li class="nav-item" role="presentation">
    <button
        class="nav-link"
        id="authors-verde-tab"
        data-bs-toggle="pill"
        data-bs-target="#authors-verde"
        type="button"
        role="tab"
        aria-controls="authors-verde"
        aria-selected="true"
        aria-label="Verde"
    >
    <i class="fa fa-users"></i>
    Verde
    </button>
  </li>
  <li class="nav-item" role="presentation">
    <button
        class="nav-link"
        id="authors-pooch-tab"
        data-bs-toggle="pill"
        data-bs-target="#authors-pooch"
        type="button"
        role="tab"
        aria-controls="authors-pooch"
        aria-selected="true"
        aria-label="Pooch"
    >
    <i class="fa fa-users"></i>
    Pooch
    </button>
  </li>
  <li class="nav-item" role="presentation">
    <button
        class="nav-link"
        id="authors-boule-tab"
        data-bs-toggle="pill"
        data-bs-target="#authors-boule"
        type="button"
        role="tab"
        aria-controls="authors-boule"
        aria-selected="true"
        aria-label="Boule"
    >
    <i class="fa fa-users"></i>
    Boule
    </button>
  </li>
</ul>
<div class="tab-content" id="authors-tabContent">
  <div
      class="tab-pane fade show active"
      id="authors-harmonica"
      role="tabpanel"
      aria-labelledby="authors-harmonica-tab"
  >

```{include} harmonica-authors.md
```

  </div>
  <div
      class="tab-pane fade"
      id="authors-verde"
      role="tabpanel"
      aria-labelledby="authors-verde-tab"
  >

```{include} verde-authors.md
```

  </div>
  <div
      class="tab-pane fade"
      id="authors-pooch"
      role="tabpanel"
      aria-labelledby="authors-pooch-tab"
  >

```{include} pooch-authors.md
```

  </div>
  <div
      class="tab-pane fade"
      id="authors-boule"
      role="tabpanel"
      aria-labelledby="authors-boule-tab"
  >

```{include} boule-authors.md
```

  </div>
</div>


```{note}
Our [Authorship Guidelines][authorship] define the rules for attributing
authorship to those involved in our projects.
```

### Maintainers

The maintainers are the ones responsible for leading the projects, merging
changes, making releases, and more.

<div class="row gy-3">
<div class="col-4 col-sm-3 col-md-2 gx-2 d-flex align-items-stretch">
  <div class="card">
    <img class="card-img-top" src="https://github.com/santisoler.png">
    <div class="card-body">
      <h4 class="card-title fs-6">
        Santiago Soler
      </h4>
      <p class="card-text text-muted fs-6">
        <a href="https://github.com/santisoler">@santisoler</a>
      </p>
    </div>
  </div>
</div>
<div class="col-4 col-sm-3 col-md-2 gx-2 d-flex align-items-stretch">
  <div class="card">
    <img class="card-img-top" src="https://github.com/leouieda.png">
    <div class="card-body">
      <h4 class="card-title fs-6">
        Leonardo Uieda
      </h4>
      <p class="card-text text-muted fs-6">
        <a href="https://github.com/leouieda">@leouieda</a>
      </p>
    </div>
  </div>
</div>
</div>

## Brief history

The Fatiando a Terra project had it's start around 2008 as a C++ program to
perform geophysical modeling of various data types (gravity, magnetics,
seismic, etc.).
At least that was what a small group of Geophysics undergraduate students at
the [University of São Paulo][usp], Brazil, set out to do.
Unsurprisingly, this overly ambitious goal was never achieved.

<div class="row text-muted align-items-center fs-6">
<div class="col-md-9">

<img src="../_static/fatiando-as-a-gravmag-gui.svg" alt="Box diagram of the layout and flow of information planned for the GUI program." >

</div>
<div class="col-md-3">

First diagram (in Portuguese) of the planned graphical user interface (GUI) for
the Fatiando C++ program.
Retrieved from commit [<i class="fab fa-github"></i> 10c8ff7][commit-gui]
from 11 February 2009.

</div>
</div>

In 2010, we started developing the [`fatiando`][gh-fatiando]
Python library, which included several state-of-the-art methods for forward
modeling and inversion of gravity and magnetic data, as well as toy problems in
other fields useful for teaching.
Development of this library was discontinued in 2018  as our focus shifted to
our newer and more well-scoped libraries.
This [blog post announcing the shift][blog-fatiando-future] explains the
reasoning behind this decision.

```{note}
The last version that was released of `fatiando` is [v0.5][v0.5-doi].
The documentation for it can still be accessed at
[legacy.fatiando.org](https://legacy.fatiando.org)
```

<div class="row text-muted align-items-center fs-6">
<div class="col-md-9">
<div class="ratio ratio-16x9">
  <iframe src="https://www.youtube.com/embed/videoseries?list=PLPA_RM8wsOqLQRajw_e9ByUe56z7TETaL" title="YouTube video player" frameborder="0" allowfullscreen></iframe>
</div>
</div>
<div class="col-md-3">

Our [YouTube channel][youtube] has a [playlist of talks][yt-playlist] given
about Fatiando over the years.

</div>
</div>

## The geophysics Python ecosystem

Fatiando is a part of the larger geophysics open-source Python ecosystem,
which has grown tremendously since we started development in 2010.

<div class="row gy-4 py-3 align-items-center">
<div class="col-6 col-sm-4 col-md-3">
  <a target="_blank" href="https://simpeg.xyz/">
  <img src="../_static/simpeg-logo.png" title="SimPEG">
  </a>
</div>
<div class="col-6 col-sm-4 col-md-3">
  <a target="_blank" href="https://www.gempy.org/">
  <img src="../_static/gempy-logo.png" title="GemPy">
  </a>
</div>
<div class="col-6 col-sm-4 col-md-3">
  <a target="_blank" href="https://emsig.xyz/">
  <img src="../_static/emsig-logo.svg" title="emsig">
  </a>
</div>
<div class="col-6 col-sm-4 col-md-3">
  <a target="_blank" href="https://docs.pyvista.org/">
  <img src="../_static/pyvista-logo.png" title="PyVista">
  </a>
</div>
<div class="col-6 col-sm-4 col-md-3">
  <a target="_blank" href="https://www.pygimli.org/">
  <img src="../_static/pygimli-logo.svg" title="pyGIMLi">
  </a>
</div>
<div class="col-6 col-sm-4 col-md-3">
  <a target="_blank" href="https://softwareunderground.github.io/subsurface/">
  <img src="../_static/subsurface-logo.svg" title="subsurface">
  </a>
</div>
<div class="col-6 col-sm-4 col-md-3">
  <a target="_blank" href="https://www.pygmt.org/">
  <img src="../_static/pygmt-logo.svg" title="PyGMT">
  </a>
</div>
<div class="col-6 col-sm-4 col-md-3">
  <img src="../_static/fatiando-banner-small.svg" title="Fatiando a Terra">
</div>
</div>

## Funding and support

Development and maintenance of the Fatiando a Terra project is supported by:

* Salary support for Leonardo Uieda from the [University of Liverpool][liv]
  (from 2019) and [Universidade do Estado do Rio de Janeiro][uerj] (2014-2017).
* A PhD scholarship for Santiago Soler from [CONICET][conicet], Argentina
  (2017-2022).
* MSc and PhD scholarships for Leonardo Uieda from [Capes][capes], Brazil
  (2010-2016).

[youtube]: https://www.youtube.com/fatiandoorg
[yt-playlist]: https://youtube.com/playlist?list=PLPA_RM8wsOqLQRajw_e9ByUe56z7TETaL
[gh]: https://github.com/fatiando
[gh-fatiando]: https://github.com/fatiando/fatiando
[usp]: https://www.iag.usp.br/
[commit-gui]: https://github.com/fatiando/fatiando/blob/10c8ff7c17df53e3e0abd83f1ce8d2a3f6bc57aa/fluxo-simples.pdf
[pinga]: https://www.pinga-lab.org/
[v0.5-doi]: https://doi.org/10.5281/zenodo.157746
[blog-fatiando-future]: https://www.leouieda.com/blog/future-of-fatiando.html
[liv]: https://www.liverpool.ac.uk/earth-ocean-and-ecological-sciences/
[uerj]: https://www.uerj.br/
[conicet]: https://www.conicet.gov.ar/
[capes]: https://www.gov.br/capes
[authorship]: https://github.com/fatiando/community/blob/main/AUTHORSHIP.md
