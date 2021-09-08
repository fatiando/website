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

<div class="container-fluid banner">
<div class="container">
<div class="row align-items-center gx-5 gy-5">
<div class="col-md-8">

# Fatiando a Terra

<p class="banner-description">Open-source Python tools for Geophysics</p>

Fatiando provides **Python libraries** for data processing, modeling, and
inversion across the Geosciences.

It is built by a **community** of geoscientists and software developers with
a passion for well-designed tools and helping our peers.

All of our code is **free and open-source**, distributed under the permissive
[BSD 3-clause license][bsd].

<div class="mt-5">
  <a href="/about"><button type="button" class="btn btn-primary mb-3 me-3">
  More about us
  </button></a>
  <a href="/install"><button type="button" class="btn btn-light mb-3">
  Install on your computer
  <span class="bullet-separator">&bull;</span>
  <i class="fab fa-linux"></i>
  <i class="fab fa-apple"></i>
  <i class="fab fa-windows"></i>
  </button></a>
</div>

</div> <!-- column -->
<div class="col-md-4 order-md-first">
  <img class="banner-logo" src="_static/fatiando-logo.svg">
</div>
</div> <!-- row -->
</div> <!-- container -->
</div> <!-- container-fluid -->



<div class="container-fluid section background-1">
<div class="container">

<div class="row align-items-center gx-5 gy-5">
<div class="col-md-7">

## Getting started

Placeholder placeholder placeholder placeholder placeholder placeholder
placeholder placeholder placeholder placeholder placeholder

Placeholder placeholder placeholder placeholder placeholder placeholder
placeholder placeholder placeholder placeholder placeholder

Placeholder placeholder placeholder placeholder placeholder placeholder
placeholder placeholder placeholder placeholder placeholder

<div class="mt-5">
  <a href="/learn"><button type="button" class="btn btn-light mb-3 me-3">
  <i class="fa fa-graduation-cap"></i>
  Learning resources
  </button></a>
  <a href="/contact"><button type="button" class="btn btn-warning mb-3">
  <i class="fa fa-hands-helping"></i>
  Need help?
  </button></a>
</div>

</div> <!-- column -->
<div class="col-md-5 order-md-last text-center fs-6">

<div class="ratio ratio-16x9">
  <iframe src="https://www.youtube.com/embed/z-5dvWfB_SM?start=850" title="YouTube video player" frameborder="0" allowfullscreen></iframe>
</div>

<i class="fab fa-github"></i>
[leouieda/2021-06-22-gfz](https://github.com/leouieda/2021-06-22-gfz)
<span class="bullet-separator">&bull;</span>
<i class="fab fa-python"></i>
[Jupyter notebook](https://nbviewer.jupyter.org/github/leouieda/2021-06-22-gfz/blob/main/demo.ipynb)

</div> <!-- column -->
</div> <!-- row -->
</div> <!-- container -->
</div> <!-- container-fluid -->



<div class="container-fluid transition">
<div class="container narrow text-center">

<h2 class="no-top-margin">
<i class="fa fa-tools me-3"></i>
A multi-tool for Geophysics
</h2>

<div class="row g-5 pt-4 align-items-center">
<div class="col-6 col-md-3">
  <a href="#pooch">
  <img src="_static/pooch-logo.svg" title="Pooch">
  </a>
</div>
<div class="col-6 col-md-3">
  <a href="#verde">
  <img src="_static/verde-logo.svg" title="Verde">
  </a>
</div>
<div class="col-6 col-md-3">
  <a href="#harmonica">
  <img src="_static/harmonica-logo.svg" title="Harmonica">
  </a>
</div>
<div class="col-6 col-md-3">
  <a href="#boule">
  <img src="_static/boule-logo.svg" title="Boule">
  </a>
</div>
</div>

</div> <!-- container -->
</div> <!-- container-fluid -->



<div class="container-fluid section background-2">
<div class="container">

<div class="row align-items-center gx-5 gy-5">
<div class="col-md-7">

(pooch)=
## **Pooch:** Easily download datasets

Pooch is the easiest way to **download data files** to your computer.

It is used to manage sample data downloads not only by our own tools but also
other popular Scientific Python libraries:
[scikit-image](https://github.com/scikit-image/scikit-image),
[MetPy](https://github.com/Unidata/MetPy),
[xarray](https://github.com/pydata/xarray),
[SHTOOLS](https://github.com/SHTOOLS/SHTOOLS),
[satpy](https://github.com/pytroll/satpy),
[icepack](https://github.com/icepack/icepack),
[histolab](https://github.com/histolab/histolab),
[yt](https://github.com/yt-project/yt),
[napari](https://github.com/napari/napari),
and [more](https://github.com/fatiando/pooch/network/dependents).

<ul class="project-info">
<li>
  <i class="fa fa-check fa-fw" style="color: green" title="Project status"></i>
   Stable and ready for use
</li>
<li>
  <i class="fab fa-github fa-fw" title="GitHub repository"></i>
  <a href="https://github.com/fatiando/pooch">fatiando/pooch</a>
</li>
<li>
  <i class="fas fa-bookmark fa-fw" title="Publication"></i>
   doi: <a href="https://doi.org/10.21105/joss.01943">10.21105/joss.01943</a>
</li>
</ul>

<div class="mt-5">
  <a target="_blank" href="https://www.fatiando.org/pooch/">
  <button type="button" class="btn btn-primary mb-3">
  <i class="fa fa-book"></i>
  Pooch documentation
  </button>
  </a>
</div>

</div> <!-- column -->
<div class="col-md-5 order-md-first">

```python
"""
Download Australian gravity data from figshare
"""
import pooch

# The Digital Object Identifier of the data
doi = "10.6084/m9.figshare.13643837"
# Known MD5 checksum (from figshare)
checksum = "md5:16c94a792003714efee2bdb4f3181d3a"
# Download the netCDF file and check integrity
fname = pooch.retrieve(
    url=f"doi:{doi}/australia-ground-gravity.nc",
    known_hash=checksum,
)

# Load the data with xarray
import xarray as xr

# fname is the path to the file
data = xr.load_dataset(fname)
```

<p class="text-center fs-6">
Running this code multiple times will only result in a single download
because the data are cached where Pooch can find it.
</p>

</div> <!-- column -->
</div> <!-- row -->
</div> <!-- container -->
</div> <!-- container-fluid -->



<div class="container-fluid section background-3">
<div class="container">

<div class="row align-items-center gx-5 gy-5">
<div class="col-md-7">

(verde)=
## **Verde:** Gridding, machine learning style

Verde offers **spatial** data processing and interpolation (**gridding**) with
a sprinkle of machine learning.


<ul class="project-info">
<li>
  <i class="fa fa-check fa-fw" style="color: green" title="Project status"></i>
   Stable and ready for use
</li>
<li>
  <i class="fab fa-github fa-fw" title="GitHub repository"></i>
  <a href="https://github.com/fatiando/verde">fatiando/verde</a>
</li>
<li>
  <i class="fas fa-bookmark fa-fw" title="Publication"></i>
   doi: <a href="https://doi.org/10.21105/joss.00957">10.21105/joss.00957</a>
</li>
</ul>

<div class="mt-5">
  <a target="_blank" href="https://www.fatiando.org/verde/">
  <button type="button" class="btn btn-primary mb-3">
  <i class="fa fa-book"></i>
  Verde documentation
  </button>
  </a>
</div>

</div> <!-- column -->
<div class="col-md-5 order-md-last text-center fs-6">
  <img class="mb-3" src="_static/verde-spline-example.png">
  Vertical ground velocity in California interpolated from GPS data with and
  without weights based on data uncertainty.
</div> <!-- column -->
</div> <!-- row -->
</div> <!-- container -->
</div> <!-- container-fluid -->



<div class="container-fluid section background-2">
<div class="container">

<div class="row align-items-center gx-5 gy-5">
<div class="col-md-7">

(harmonica)=
## **Harmonica:** All things potential fields

Processing and modeling <b>gravity</b> and <b>magnetic</b> data, like terrain
correction, upward continuation, equivalent layers, 3D inversion, and more.

<ul class="project-info">
<li>
  <i class="fa fa-sync-alt fa-fw" style="color: green" title="Project status"></i>
  Functional but still evolving
</li>
<li>
  <i class="fab fa-github fa-fw" title="GitHub repository"></i>
  <a href="https://github.com/fatiando/harmonica">fatiando/harmonica</a>
</li>
<li>
  <i class="fas fa-bookmark fa-fw" title="Publication"></i>
   doi: <a href="https://doi.org/10.5281/zenodo.3628741">10.5281/zenodo.3628741</a>
</li>
</ul>

<div class="mt-5">
  <a target="_blank" href="https://www.fatiando.org/harmonica/">
  <button type="button" class="btn btn-primary mb-3">
  <i class="fa fa-book"></i>
  Harmonica documentation
  </button>
  </a>
</div>

</div> <!-- column -->
<div class="col-md-5 order-md-first text-center fs-6">
  <img class="mb-3" src="_static/harmonica-example-bushveld.png">
  Residual gravity disturbances of the Bushveld Complex, South Africa,
  gridded to a uniform height with equivalent sources.
</div> <!-- column -->
</div> <!-- row -->
</div> <!-- container -->
</div> <!-- container-fluid -->



<div class="container-fluid section background-3">
<div class="container">

<div class="row align-items-center gx-5 gy-5">
<div class="col-md-7">

(boule)=
## **Boule:** Ellipsoids and normal gravity

Boule defines **reference ellipsoids** for calculating normal gravity of
the Earth and other planetary bodies (Moon, Mars, Venus, Mercury).

<ul class="project-info">
<li>
  <i class="fa fa-sync-alt fa-fw" style="color: green" title="Project status"></i>
  Functional but still evolving
</li>
<li>
  <i class="fab fa-github fa-fw" title="GitHub repository"></i>
  <a href="https://github.com/fatiando/boule">fatiando/boule</a>
</li>
<li>
  <i class="fas fa-bookmark fa-fw" title="Publication"></i>
   doi: <a href="https://doi.org/10.5281/zenodo.3530749">10.5281/zenodo.3530749</a>
</li>
</ul>

<div class="mt-5">
  <a target="_blank" href="https://www.fatiando.org/boule/">
  <button type="button" class="btn btn-primary mb-3">
  <i class="fa fa-book"></i>
  Boule documentation
  </button>
  </a>
</div>

</div> <!-- column -->
<div class="col-md-5 order-md-last text-center fs-6">
  <img class="mb-3" src="_static/boule-example-normal-gravity.png">
  Normal gravity of the WGS84 ellipsoid calculated at the Earth's surface using
  an analytical expression (no free-air correction required).
</div> <!-- column -->
</div> <!-- row -->
</div> <!-- container -->
</div> <!-- container-fluid -->



<div class="container-fluid section background-4">
<div class="container">

<div class="row align-items-center gx-5 gy-5">
<div class="col-md-7">

# Interested?

Placeholder placeholder placeholder placeholder placeholder placeholder
placeholder placeholder placeholder placeholder placeholder

Placeholder placeholder placeholder placeholder placeholder placeholder
placeholder placeholder placeholder placeholder placeholder

Placeholder placeholder placeholder placeholder placeholder placeholder
placeholder placeholder placeholder placeholder placeholder

<div class="mt-5">
  <a href="/community"><button type="button" class="btn btn-light mb-3">
  <i class="fa fa-users"></i>
  Participate in our community
  </button></a>
</div>

</div> <!-- column -->
<div class="col-md-5 order-md-first">
  <img src="_static/fatiando-community-call.jpg" title="Screenshot from a virtual Fatiando community call.">
</div>
</div> <!-- row -->
</div> <!-- container -->
</div> <!-- container-fluid -->


[bsd]: https://opensource.org/licenses/BSD-3-Clause
