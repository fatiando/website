---
title: Support the project
template: base.html
logos:
  - name: Fatiando a Terra
    img: "../images/fatiando-logo-background.png"
  - name: Verde
    img: "../images/verde-logo.png"
  - name: Harmonica
    img: "../images/harmonica-logo.png"
  - name: Pooch
    img: "../images/pooch-logo.png"
  - name: Boule
    img: "../images/boule-logo.png"
  - name: Ensaio
    img: "../images/ensaio-logo.png"
  - name: Choclo
    img: "../images/choclo-logo.png"
---

# {{ page.title }}

<div class="lead">

Here are some of the ways in which you can help support the project and give
back to the community.

</div>

## Cite our software

If you use our software, please consider citing it in your publications.
Our software is <strong>made by scientists and volunteers</strong> who
generously donate their time and attention.
Citations help us justify the effort that goes into building
and maintaining this project.

Please **cite the libraries** that you used and **also the Fatiando project as a whole**.

### Citing the libraries

Each of our libraries has a citation page that describes the best way to cite
it in publications. Usually it will be a journal publication describing the
software or a code archive on [Zenodo](https://zenodo.org/communities/fatiando).
Below are the links to the citation pages:

<ul role="list" class="list-inline-center">
{%- for lib in site["index"].libraries %}
  <li><a class="button-link-primary" href="https://www.fatiando.org/{{ lib.id }}/latest/citing.html">{{ lib.id|title }}</a></li>
{%- endfor %}
</ul>

### Citing the Fatiando project

If you wish to reference the Fatiando project as a whole, please use the
following reference:

> Uieda, L., V. C. Oliveira Jr, and V. C. F. Barbosa (2013), Modeling the
> Earth with Fatiando a Terra, Proceedings of the 12th Python in Science
> Conference, pp. 91-98. doi:[10.25080/Majora-8b375195-010](https://doi.org/10.25080/Majora-8b375195-010)

This article was [peer-reviewed](https://github.com/scipy-conference/scipy_proceedings/pull/52)
and is open-access.
Source files and extra material for the paper are on the
[leouieda/scipy2013](https://github.com/leouieda/scipy2013) GitHub
repository.

Here is a BibTex entry for LaTeX users:

```bibtex
@inproceedings{Uieda2013,
  series = {SciPy},
  title = {Modeling the {E}arth with {F}atiando a {T}erra},
  ISSN = {2575-9752},
  DOI = {10.25080/majora-8b375195-010},
  booktitle = {Proceedings of the 12th {P}ython in {S}cience {C}onference},
  publisher = {SciPy},
  author = {Uieda, Leonardo and Oliveira, Vanderlei and Barbosa, Valéria},
  year = {2013},
  pages = {92–98},
  collection = {SciPy}
}
```

## Get involved

Fatiando only exists because of the efforts of our **community members**, most
of which volunteer their time and energy.
One of the **most impactful ways you can help** is by
[being involved](../contact)!

## Spread the word

We benefit greatly from **recommendations and acknowledgements of usage** of
our software.
It helps boost morale, encourage participation, and can even help with funding
applications and job interviews for our community members.

<i class="fab fa-mastodon fa-fw"></i>
**Social media:** Share links to this website, our [GitHub][gh] repositories,
project documentation, etc.

<i class="fab fa-python fa-fw"></i>
**Publish your code:** Used our tools in your research? Why not publish your
analysis code along with the paper? [Give us a shout](../contact) and we'll
gladly share it on our social media.

<i class="fa fa-paint-brush fa-fw"></i>
**Use our logos:** Include the project logos in talks, posters, videos, and
websites about work that used our tools.

<ul role="list" class="list-inline-center padding-vertical-l">
{%- for logo in page.logos %}
  <li><img style="max-width: 4em;" title="{{ logo.name }}" src="{{ logo.img }}"></li>
{%- endfor %}
</ul>

<div class="callout-secondary">

<i class="fas fa-download"></i> Want all of them + vector graphics versions?
High quality SVG and PNG versions of the logos and other variants are all
available at the [fatiando/logo][logo-repo] repository.

</div>

Can't get enough? Here is a sweet **Fatiando wallpaper** in 4k resolution and
16x9 aspect ratio:

<figure>
<img src="https://raw.githubusercontent.com/fatiando/logo/main/fatiando-wallpaper.png">
<figcaption>
<a target="_blank" href="https://raw.githubusercontent.com/fatiando/logo/main/fatiando-wallpaper.png"><i class="fas fa-download"></i> Download the wallpaper</a> and use it on your computer, phone, or tablet.
</figcaption>
</figure>

[logo-repo]: https://github.com/fatiando/logo
[gh]: https://github.com/fatiando
