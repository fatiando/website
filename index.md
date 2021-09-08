```{title} Home
```

```{toctree}
:hidden:

about/index.md
install/index.md
learn/index.md
contact/index.md
community/index.md
cite/index.md
```

<div class="container-fluid banner" style="background-image: linear-gradient(to bottom, transparent, #02020e55), url(_static/background.svg);">
<div class="container page-content">
<div class="row align-items-center gx-5">
<div class="col-sm-4">
  <img class="banner-logo mx-auto d-block" src="_static/fatiando-logo.svg">
</div>
<div class="col-sm-8">

# Fatiando a Terra

<p class="banner-description">Open-source Python tools for Geophysics</p>

We are a **community** of geoscientists and software developers,
bounded by our shared commitment to **open-source** software and
**open-science**.
We provide several **Python libraries** for data processing, modeling, and
inversion across the Geosciences.
All of our code is distributed under the permissive [BSD 3-clause
license][bsd].

<div class="mt-4">
<a href="/about"><button type="button" class="btn btn-primary mb-2 me-3">More about us</button></a>
<a href="/community"><button type="button" class="btn btn-primary mb-2">Join the community</button></a>
</div>

</div>
</div>
</div>
</div>

<div class="container page-content">

We maintain several Python projects which are in various stages of development:
from early design to polished and published products. We'll also be adding new
projects to our toolkit in the future.

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


<h2 class="text-center">Looking for the <code>fatiando</code> package?</h2>

**It still exists!**
While development of the `fatiando` library has stopped in favour of our new
tools, you can still view the
[documentation for the last release (v0.5)](https://legacy.fatiando.org)
and the [source code archive on GitHub](https://github.com/fatiando/fatiando).
The library will remain archived and usable for the foreseeable future.
To get a sense for the reasoning behind the choice to abandon `fatiando`, please read
[this blog post](http://www.leouieda.com/blog/future-of-fatiando.html).

</div>

[bsd]: https://opensource.org/licenses/BSD-3-Clause
