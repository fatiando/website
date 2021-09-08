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
