---
title: VU Lab
subtitle: We research <strong>Visual Understanding</strong> and <strong>Spatial Intelligence</strong>
layout: page
show_sidebar: false
hero_image: /img/about.jpg
hero_darken: true
hero_links:
  - text: See Our Team
    link: /team/
  - text: See Our Research
    link: /research/
---

# About Us

VU Lab studies visual understanding and spatial intelligence for robust embodied systems. We focus on perception, spatial reasoning, and decision-making methods that help intelligent agents interpret complex environments and act reliably in the real world.

Our work spans scene understanding, 3D perception, language-guided reasoning, and spatial intelligence. This homepage now provides direct entry points to the lab team and research overview.

# Highlights
{% assign posts = site.posts | where:"categories","highlights" %}
<div class="columns is-multiline">
  {% for post in posts %}
  <div class="column is-4-desktop is-6-tablet">
    {% include post-card.html %}
  </div>
  {% endfor %}
</div>

## Focus Areas

* Visual understanding for complex real-world scenes
* Spatial intelligence for embodied reasoning and planning
* Scalable learning systems for perception and autonomy

## Explore

Use the navigation above to browse the lab's team, research, publications, and contact pages.