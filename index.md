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

<style>
.home-highlight-grid {
  margin-top: 1.5rem;
}

.home-highlight-column {
  display: flex;
}

.home-highlight-link {
  color: inherit;
  display: block;
  height: 100%;
  width: 100%;
}

.home-highlight-link:hover,
.home-highlight-link:focus-visible {
  color: inherit;
}

.home-highlight-card {
  display: flex;
  flex-direction: column;
  height: 100%;
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}

.home-highlight-link:hover .home-highlight-card,
.home-highlight-link:focus-visible .home-highlight-card {
  box-shadow: 0 1rem 2rem rgba(15, 23, 42, 0.12);
  transform: translateY(-4px);
}

.home-highlight-media {
  background: #0f172a;
  overflow: hidden;
}

.home-highlight-media .image {
  background: #0f172a;
}

.home-highlight-image {
  background: #ffffff;
}

.home-highlight-image .image {
  background: #ffffff;
}

.home-highlight-image img {
  display: block;
  height: 100%;
  object-fit: contain;
  width: 100%;
}

.home-highlight-card .card-content {
  display: flex;
  flex: 1;
  flex-direction: column;
}

.home-highlight-summary {
  flex: 1;
}
</style>

# About Us

VU Lab studies visual understanding and spatial intelligence for robust embodied systems. We focus on perception, spatial reasoning, and decision-making methods that help intelligent agents interpret complex environments and act reliably in the real world.

Our work spans scene understanding, 3D perception, language-guided reasoning, and spatial intelligence. This homepage now provides direct entry points to the lab team and research overview.

# Highlights
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'highlights'" %}
<div class="columns is-multiline home-highlight-grid">
  {% for post in posts %}
  {% assign card_href = post.external_url | default: post.url %}
  {% if card_href contains '://' %}
    {% assign resolved_card_href = card_href %}
  {% else %}
    {% assign resolved_card_href = card_href | relative_url %}
  {% endif %}
  <div class="column is-3-desktop is-6-tablet home-highlight-column">
    <a href="{{ resolved_card_href }}" class="home-highlight-link">
      <div class="card home-highlight-card">
        {% if post.video or post.image %}
        <div class="card-image home-highlight-media{% unless post.video %} home-highlight-image{% endunless %}">
          {% if post.video %}
          <figure class="image is-4by3">
            <div class="post-card-video-frame">
              <video class="post-card-video" autoplay muted loop playsinline preload="metadata"{% if post.video_poster %} poster="{{ post.video_poster | relative_url }}"{% elsif post.image %} poster="{{ post.image | relative_url }}"{% endif %} aria-label="{{ post.title }} video preview">
                <source src="{{ post.video | relative_url }}" type="video/mp4">
              </video>
            </div>
          </figure>
          {% else %}
          <figure class="image is-4by3">
            <img src="{{ post.image | relative_url }}" alt="{{ post.title }}">
          </figure>
          {% endif %}
        </div>
        {% endif %}
        <div class="card-content">
          <p class="title is-5">{{ post.title }}</p>
          <div class="content home-highlight-summary">{{ post.summary }}</div>
        </div>
        <footer class="card-footer">
          <p class="card-footer-item">Updated: {{ post.updated | default: post.date | date: "%b %-d, %Y" }}</p>
        </footer>
      </div>
    </a>
  </div>
  {% endfor %}
</div>

## Focus Areas

* Visual understanding for complex real-world scenes
* Spatial intelligence for embodied reasoning and planning
* Scalable learning systems for perception and autonomy

## Explore

Use the navigation above to browse the lab's team, research, publications, and contact pages.