---
title: Publications
template: base.html
---

# {{ page.title }}

<div class="lead">

These are publications about Fatiando and some examples of papers, software, and
other instances where Fatiando software were used and cited.

</div>

## Paper about Fatiando

<ul role="list" class="flow">
{%- for pub in page.papers %}
  <li>{{ pub.authors }} ({{ pub.year }}). <strong>{{ pub.title }}</strong>. <em>{{ pub.journal }}</em>. doi:<a target="_blank" href="https://doi.org/{{ pub.doi }}">{{ pub.doi }}</a>.</li>
{%- endfor %}
</ul>


<h2 id="used-by">Users of Fatiando</h2>

<div class="callout-secondary">

**Help us complete the list!** Open an Issue or send a Pull Request to the
[fatiando/website](https://github.com/fatiando/website) repository suggesting
new entries. If you need help doing that, [reach out](../contact) and we'll
lend a hand.

</div>

**Go to year:** {% for year, items in page.used_by|groupby("year")|reverse %}[{{ year }}](#{{ year }}){% if not loop.last%} - {% endif %}{% endfor %}

<!-- Add new items to the entries.yml file -->
<!-- Use https://citation.doi.org/ with the american-geophysical-union style to format citations to papers -->

{%- set counter = namespace(count=page.used_by|length) %}

{%- for year, items in page.used_by|groupby("year")|reverse %}

### {{ year }}

<ul role="list" class="flow">
{%- for item in items %}
  <li>[{{ counter.count }}] <strong>{{ item.type|title }}:</strong> <a target="_blank" href="{{ item.link }}">{{ item.description }}</a></li>
  {%- set counter.count = counter.count - 1 %}
{%- endfor %}
</ul>

<p class="text-center"><a href="#used-by">Back to top</a></p>

{%- endfor %}
