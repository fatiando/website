---
title: Installing our software
template: base.html
---

# {{ page.title }}

Our tools are built in Python and can be used in Jupyter notebooks,
scripts, and other libraries and programs. All of our software is
compatible with <strong>Linux, Mac, and Windows</strong>.

## Getting Python

In order to start using the Fatiando tools you need to **install a Python
distribution**.
We recommend using [the conda-forge installer](https://conda-forge.org/download/).
It's cross-platform and comes with the `conda` (or `mamba`) package manager
already installed, which you can then use to install our software and other
things.

## Install the latest tools

Once you've finished setting up Python, you can install all of the latest
Fatiando tools.

The **recommended** method is using the `conda` (or `mamba`) package manager
with a single command:

```bash
conda install verde harmonica boule pooch choclo bordado ensaio --channel conda-forge
```

Alternatively, you can use the `pip` package manager:

```bash
pip install verde harmonica boule pooch choclo bordado ensaio
```

<div class="callout">

**Tip:**
Run these commands in a terminal (Linux/Mac) or "Anaconda prompt" (Windows).

</div>

## Installing the legacy "fatiando" package

The old `fatiando` package **is not currently maintained or developed**,
meaning that **it won't get bug fixes or new features**. The purpose of these
instructions are for **legacy use only**, in order to run old code to check
reproducibility of results.

<div class="callout">

**Note:**
If you are working on some new research or data analysis, we **strongly
recommend** using the [latest tools](#install-the-latest-tools) instead.

</div>

If you need to install the old `fatiando` package, you can still do so through
`conda`. Please note the following instructions were only tested under a GNU/Linux distribution, so
we don't guarantee that they will also work on a different OS.

Since the old `fatiando` runs on Python 2.7, a deprecated version of Python,
you need to create a separate environment for our installation in order to
avoid conflicts with your Anaconda or conda-forge installation.

Create a new environment and install the required packages:

```bash
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

<div class="callout">

**More information:**
The documentation for the legacy `fatiando` package is available at
[legacy.fatiando.org](https://legacy.fatiando.org).

</div>
