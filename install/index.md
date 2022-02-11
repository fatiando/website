# Installing

<p class="lead">
Our tools are built in Python and can be used in Jupyter notebooks,
scripts, and other libraries and programs. All of our software is
compatible with <strong>Linux, Mac, and Windows</strong>.
</p>

## Getting Python

In order to start using the Fatiando tools you need to **install a Python
distribution**.
We recommend using [Anaconda][anaconda].
You can find detailed instructions on how to install it on any operating system
in the [Software Carpentry setup instructions][swc-install].

## Install the latest tools

Once you've finished setting up Python, you can install all of the latest
Fatiando tools.

The **recommended** method is using the `conda` package manager with a single
command:

```bash
conda install verde harmonica boule pooch --channel conda-forge
```

Alternatively, you can use the `pip` package manager:

```bash
pip install verde harmonica boule pooch
```

```{tip}
Run these commands in a terminal (Linux/Mac) or "Anaconda prompt" (Windows).
```

[anaconda]: https://www.anaconda.com/products/individual
[swc-install]: https://carpentries.github.io/workshop-template/#python

---

## Installing the legacy `fatiando` package

```{warning}
The old `fatiando` package **is not currently maintained or developed**,
meaning that **it won't get bug fixes or new features**. The purpose of these
instructions are for **legacy use only**, in order to run old code to check
reproducibility of results.
```

```{tip}
If you are working on some new research or data analysis, we strongly
**recommend using the [latest tools](#install-the-latest-tools)** instead.
```

If you need to install the old `fatiando` package, you can still do so through
`conda`. Please note the following instructions were only tested under a GNU/Linux distribution, so
we don't guarantee that they will also work on a different OS.

Since the old `fatiando` runs on Python 2.7, a deprecated version of Python,
you need to create a separate environment for our installation in order to
avoid conflicts with your Anaconda installation.

Create a new environment and install the required packages:

```
conda create --name fatiando-legacy -c conda-forge python=2.7 numpy=1.10 scipy=1.2 matplotlib=2.2 pillow=6.2 future=0.18 numba=0.43 pytest=4.6 fatiando=0.5
```

Activate the newly created environment:

```bash
conda activate fatiando-legacy
```

And test your installation:

```bash
python -c "import fatiando; fatiando.test()"
```

You should see a green dot after each test is run and no red `F`.

The documentation for the legacy `fatiando` package is available at
[legacy.fatiando.org](https://legacy.fatiando.org).
