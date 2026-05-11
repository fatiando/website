---
title: Used by
template: base.html
---

# {{ page.title }}

<div class="lead">

These are some examples of papers, software, and other instances where Fatiando
software were used and cited.

</div>

<div class="callout-secondary">

**Help us complete the list!** Open an Issue or send a Pull Request to the
[fatiando/website](https://github.com/fatiando/website) repository suggesting
new entries.

</div>

<!-- Add new items to the entries.yml file -->
<!-- Use https://citation.doi.org/ with the american-geophysical-union style to format citations to papers -->

{%- set counter = namespace(count=page.entries|length) %}

{%- for year, items in page.entries|groupby("year")|reverse %}

## {{ year }}

<ul role="list" class="flow">
{%- for item in items %}
  <li>[{{ counter.count }}] <strong>{{ item.type|title }}:</strong> <a target="_blank" href="{{ item.link }}">{{ item.description }}</a></li>
  {%- set counter.count = counter.count - 1 %}
{%- endfor %}
</ul>

{%- endfor %}
