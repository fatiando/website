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
<div class="row align-items-center gy-5">
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
  <a href="install"><button type="button" class="btn btn-light mb-3 me-3">
  Install
  <span class="bullet-separator">&bull;</span>
  <i class="fab fa-linux"></i>
  <i class="fab fa-apple"></i>
  <i class="fab fa-windows"></i>
  </button></a>
  <a href="cite"><button type="button" class="btn btn-success mb-3">
  <i class="fa fa-bookmark"></i>
  Cite our tools
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

<div class="row align-items-start gy-5">
<div class="col-md-7">

## Getting started

**Looking for an overview?**
A good place to start is [this recorded example][yt-demo] (~20 min) that uses
our tools to download, process, and interpolate public domain gravity data from
the Bushveld Complex in South Africa.

**No time for a video?**
You can also browse the <i class="fab fa-python"></i>
[Jupyter notebook][yt-demo-nb] used in the example.


**New to Python?**
We provide links to {ref}`excellent free resources <learn>` for starting your
Scientific Python journey.

**Used Fatiando for research?**
Please {ref}`cite our tools <cite>` in your publications.

<div class="mt-5">
  <a href="learn"><button type="button" class="btn btn-light mb-3 me-3">
  <i class="fa fa-graduation-cap"></i>
  Learning resources
  </button></a>
  <a href="contact"><button type="button" class="btn btn-warning mb-3">
  <i class="fa fa-hands-helping"></i>
  Need help?
  </button></a>
</div>

</div> <!-- column -->
<div class="col-md-5 order-md-last text-center fs-6">

<div class="ratio ratio-16x9">
  <iframe src="https://www.youtube.com/embed/z-5dvWfB_SM?start=850" title="YouTube video player" frameborder="0" allowfullscreen></iframe>
</div>

Source code for this demonstration:
<i class="fab fa-github ms-1"></i>
[leouieda/2021-06-22-gfz](https://github.com/leouieda/2021-06-22-gfz)

</div> <!-- column -->
</div> <!-- row -->
</div> <!-- container -->
</div> <!-- container-fluid -->



<div class="container-fluid transition">
<div class="container narrow text-center">

<h2 class="no-top-margin">
A toolbox for Geophysics
</h2>

<div class="row gy-4 pt-4 align-items-center">
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

<div class="row align-items-start gy-5">
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

<div class="mt-4">
  <a target="_blank" href="https://www.fatiando.org/pooch/">
  <button type="button" class="btn btn-secondary mb-3">
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

<div class="row align-items-start gy-5">
<div class="col-md-7">

(verde)=
## **Verde:** Gridding, machine learning style

Verde offers **spatial** data processing and **interpolation** (gridding) with
a sprinkling of machine learning.


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

<div class="mt-4">
  <a target="_blank" href="https://www.fatiando.org/verde/">
  <button type="button" class="btn btn-secondary mb-3">
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

<div class="row align-items-start gy-5">
<div class="col-md-7">

(harmonica)=
## **Harmonica:** All things potential fields

Harmonica is our library for processing, forward modeling, and inversion of
**gravity and magnetic** data.
Our goal is to incentivise good practices by **carefully designing** the
software and offering **state-of-the-art methods** with efficient
implementations.

<ul class="project-info">
<li>
  <i class="fa fa-sync-alt fa-fw" style="color: orange" title="Project status"></i>
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

<div class="mt-4">
  <a target="_blank" href="https://www.fatiando.org/harmonica/">
  <button type="button" class="btn btn-secondary mb-3">
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

<div class="row align-items-start gy-5">
<div class="col-md-7">

(boule)=
## **Boule:** Ellipsoids and normal gravity

Boule defines **reference ellipsoids** for calculating normal gravity of
the Earth and other planetary bodies (Moon, Mars, Venus, Mercury).

<ul class="project-info">
<li>
  <i class="fa fa-sync-alt fa-fw" style="color: orange" title="Project status"></i>
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

<div class="mt-4">
  <a target="_blank" href="https://www.fatiando.org/boule/">
  <button type="button" class="btn btn-secondary mb-3">
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

<div class="row align-items-start gy-5">
<div class="col-md-7">

# Interested?

We are always happy to **welcome anyone** who is interested in getting
involved!
Whether it be coding, teaching, designing, or just hanging out.
**Come say "Hi! 👋🏾"** on {ref}`Slack <contact>` or at our
{ref}`next online gathering <community>`.

Getting involved in open-source can be great way to meet new people, improve
your coding skills, and **make an impact** in your field.

<div class="mt-5">
  <a href="community"><button type="button" class="btn btn-light mb-3">
  <i class="fa fa-users"></i>
  Join the conversation!
  </button></a>
</div>

</div> <!-- column -->
<div class="col-md-5 order-md-first">

<img class="mb-3" src="_static/fatiando-community-call.jpg" title="Screenshot from a virtual Fatiando community call.">

Happy community members at a [Fatiando Community Call](https://youtu.be/gsYKW7XNzzw).

</div>
</div> <!-- row -->
</div> <!-- container -->
</div> <!-- container-fluid -->



<div class="container-fluid section background-1">
<div class="container narrow">
<hr class="mb-5">
<div class="row align-items-start gy-5 mb-5">
<div class="col-md-6">

<h2 class="text-center fs-3">News</h2>

* 2021/09/01: Documentation for the Python 2.7 <kbd>fatiando</kbd> package has
  been moved to [legacy.fatiando.org](https://legacy.fatiando.org).
* 2021/09/01: Fatiando is now on LinkedIn! Give
  [our page](https://www.linkedin.com/company/fatiando) a follow to keep up
  with the latest releases, events, and other news.
* 2021/05/20: Santiago, Agustina, and Leo gave a talk to the Geophysical
  Society of Houston about using Fatiando for potential field data
  ([slides are available](https://github.com/fatiando/2021-gsh)).

</div>
<div class="col-md-6">

<h2 class="text-center fs-3">Events</h2>

* **Weekly Fatiando Development Calls**: we discuss various aspects of the
  project. All are welcome, regardless of skill level and prior knowledge!
  Notes and connection details:
  [`fatiando/meeting-notes`](https://github.com/fatiando/meeting-notes)
* **AGU 2021**: Going to the AGU Fall Meeting? Come to our talk! Details at
  [`fatiando/agu2021`](https://github.com/fatiando/agu2021).


</div>
</div> <!-- row -->

<!--<h2 class="text-center fs-4">Releases</h2>-->
<div class="text-center">

**Latest releases:**
<a href="https://pypi.python.org/pypi/pooch"><img class="shield" alt="Pooch latest version" src="https://img.shields.io/pypi/v/pooch.svg?style=flat-square&label=Pooch"></a>
<a href="https://pypi.python.org/pypi/verde"><img class="shield" alt="Verde latest version" src="https://img.shields.io/pypi/v/verde.svg?style=flat-square&label=Verde"></a>
<a href="https://pypi.python.org/pypi/harmonica"><img class="shield" alt="Harmonica latest version" src="https://img.shields.io/pypi/v/harmonica.svg?style=flat-square&label=Harmonica"></a>
<a href="https://pypi.python.org/pypi/boule"><img class="shield" alt="Boule latest version" src="https://img.shields.io/pypi/v/boule.svg?style=flat-square&label=Boule"></a>

</div>

</div> <!-- container -->
</div> <!-- container-fluid -->


[bsd]: https://opensource.org/licenses/BSD-3-Clause
[yt-demo]: https://www.youtube.com/watch?v=z-5dvWfB_SM&t=850s
[yt-demo-nb]: https://nbviewer.jupyter.org/github/leouieda/2021-06-22-gfz/blob/main/demo.ipynb
