---
title: Team
subtitle: Meet the people behind VU Lab
layout: page
show_sidebar: false
---

This page mirrors the SAIR Lab style at a high level by grouping members into core lab roles.

The profiles below are placeholders and can be replaced with real names, bios, headshots, and personal pages.

{% assign principal_investigators = site.team | where: "group", "Principal Investigator" | sort: "order" %}
{% assign phd_students = site.team | where: "group", "PhD Students" | sort: "order" %}
{% assign collaborators = site.team | where: "group", "Long-term Collaborators" | sort: "order" %}
{% assign undergrads = site.team | where: "group", "Undergraduate Students" | sort: "order" %}
{% assign robots = site.team | where: "group", "Robot" | sort: "order" %}
{% assign zoo = site.team | where: "group", "Zoo" | sort: "order" %}

## Principal Investigator

<div class="columns is-multiline team-grid">
	{% for member in principal_investigators %}
		<div class="column is-one-fifth-desktop is-3-tablet is-6-mobile">
			<a href="{{ member.url | relative_url }}" class="team-member-link">
				<div class="card team-member-card">
					<div class="card-image">
						{% if member.image %}
							<figure class="image is-3by3">
								<img src="{{ member.image | relative_url }}" alt="{{ member.title }}">
							</figure>
						{% else %}
							<figure class="image is-3by3 team-member-photo">
								<div class="team-member-placeholder">{{ member.placeholder_label }}</div>
							</figure>
						{% endif %}
					</div>
					<div class="card-content has-text-centered">
						<p class="title is-6">{{ member.title }}</p>
						<p class="subtitle is-6">{{ member.subtitle }}</p>
					</div>
				</div>
			</a>
		</div>
	{% endfor %}
</div>

## PhD Students

<div class="columns is-multiline team-grid">
	{% for member in phd_students %}
		<div class="column is-one-fifth-desktop is-3-tablet is-6-mobile">
			<a href="{{ member.url | relative_url }}" class="team-member-link">
				<div class="card team-member-card">
					<div class="card-image">
						{% if member.image %}
							<figure class="image is-3by3">
								<img src="{{ member.image | relative_url }}" alt="{{ member.title }}">
							</figure>
						{% else %}
							<figure class="image is-3by3 team-member-photo">
								<div class="team-member-placeholder">{{ member.placeholder_label }}</div>
							</figure>
						{% endif %}
					</div>
					<div class="card-content has-text-centered">
						<p class="title is-6">{{ member.title }}</p>
						<p class="subtitle is-6">{{ member.subtitle }}</p>
					</div>
				</div>
			</a>
		</div>
	{% endfor %}
</div>

## Long-term Collaborators

<div class="columns is-multiline team-grid">
	{% for member in collaborators %}
		<div class="column is-one-fifth-desktop is-3-tablet is-6-mobile">
			<a href="{{ member.url | relative_url }}" class="team-member-link">
				<div class="card team-member-card">
					<div class="card-image">
						{% if member.image %}
							<figure class="image is-3by3">
								<img src="{{ member.image | relative_url }}" alt="{{ member.title }}">
							</figure>
						{% else %}
							<figure class="image is-3by3 team-member-photo">
								<div class="team-member-placeholder">{{ member.placeholder_label }}</div>
							</figure>
						{% endif %}
					</div>
					<div class="card-content has-text-centered">
						<p class="title is-6">{{ member.title }}</p>
						<p class="subtitle is-6">{{ member.subtitle }}</p>
					</div>
				</div>
			</a>
		</div>
	{% endfor %}
</div>

## Undergraduate Students

<div class="columns is-multiline team-grid">
	{% for member in undergrads %}
		<div class="column is-one-fifth-desktop is-3-tablet is-6-mobile">
			<a href="{{ member.url | relative_url }}" class="team-member-link">
				<div class="card team-member-card">
					<div class="card-image">
						{% if member.image %}
							<figure class="image is-3by3">
								<img src="{{ member.image | relative_url }}" alt="{{ member.title }}">
							</figure>
						{% else %}
							<figure class="image is-3by3 team-member-photo">
								<div class="team-member-placeholder">{{ member.placeholder_label }}</div>
							</figure>
						{% endif %}
					</div>
					<div class="card-content has-text-centered">
						<p class="title is-6">{{ member.title }}</p>
						<p class="subtitle is-6">{{ member.subtitle }}</p>
					</div>
				</div>
			</a>
		</div>
	{% endfor %}
</div>

## Robot

<div class="columns is-multiline team-grid">
	{% for member in robots %}
		<div class="column is-one-fifth-desktop is-3-tablet is-6-mobile">
			<a href="{{ member.url | relative_url }}" class="team-member-link">
				<div class="card team-member-card">
					<div class="card-image">
						{% if member.image %}
							<figure class="image is-3by3">
								<img src="{{ member.image | relative_url }}" alt="{{ member.title }}">
							</figure>
						{% else %}
							<figure class="image is-3by3 team-member-photo">
								<div class="team-member-placeholder">{{ member.placeholder_label }}</div>
							</figure>
						{% endif %}
					</div>
					<div class="card-content has-text-centered">
						<p class="title is-6">{{ member.title }}</p>
						<p class="subtitle is-6">{{ member.subtitle }}</p>
					</div>
				</div>
			</a>
		</div>
	{% endfor %}
</div>

## Zoo

<div class="columns is-multiline team-grid">
	<div class="column is-one-fifth-desktop is-3-tablet is-6-mobile">
		<div class="card team-member-card">
			<div class="card-image">
				<figure class="image is-3by3">
					<img src="{{ '/img/team/Mifa.jpeg' | relative_url }}" alt="Mifa">
				</figure>
			</div>
			<div class="card-content has-text-centered">
				<p class="title is-6">Mifa</p>
				<p class="subtitle is-6">Zoo</p>
			</div>
		</div>
	</div>
	<div class="column is-one-fifth-desktop is-3-tablet is-6-mobile">
		<div class="card team-member-card">
			<div class="card-image">
				<figure class="image is-3by3">
					<img src="{{ '/img/team/Rachel.jpeg' | relative_url }}" alt="Rachel">
				</figure>
			</div>
			<div class="card-content has-text-centered">
				<p class="title is-6">Rachel</p>
				<p class="subtitle is-6">Zoo</p>
			</div>
		</div>
	</div>
	<div class="column is-one-fifth-desktop is-3-tablet is-6-mobile">
		<div class="card team-member-card">
			<div class="card-image">
				<figure class="image is-3by3">
					<img src="{{ '/img/team/yoyo.jpeg' | relative_url }}" alt="Yoyo">
				</figure>
			</div>
			<div class="card-content has-text-centered">
				<p class="title is-6">Yoyo</p>
				<p class="subtitle is-6">Zoo</p>
			</div>
		</div>
	</div>
</div>
