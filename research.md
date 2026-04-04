---
title: Research
subtitle: We advance state-of-the-art autonomous systems.
layout: page
show_sidebar: false
hero_height: is-small
---

{% assign research_posts = site.posts | where_exp: "post", "post.categories contains 'research'" %}

<style>
.research-search-panel {
	margin: 1rem 0 1.5rem;
}

.research-search-container {
	max-width: 34rem;
	position: relative;
}

.research-search-input {
	appearance: none;
	background: #ffffff;
	border: 1px solid rgba(31, 41, 51, 0.16);
	border-radius: 0.9rem;
	box-shadow: 0 0.5rem 1.6rem rgba(15, 23, 42, 0.06);
	font-size: 0.98rem;
	padding: 0.85rem 1rem;
	width: 100%;
}

.research-search-input:focus {
	border-color: #40e0d0;
	box-shadow: 0 0 0 3px rgba(64, 224, 208, 0.16);
	outline: none;
}

.results-container {
	background: #ffffff;
	border: 1px solid rgba(31, 41, 51, 0.12);
	border-radius: 1rem;
	box-shadow: 0 1rem 2rem rgba(15, 23, 42, 0.12);
	display: none;
	list-style: none;
	margin: 0.6rem 0 0;
	max-height: 20rem;
	overflow-y: auto;
	padding: 0;
	position: relative;
	z-index: 10;
}

.results-container.has-results {
	display: block;
}

.results-container li + li {
	border-top: 1px solid rgba(31, 41, 51, 0.08);
}

.research-search-result-link {
	color: inherit;
	display: block;
	padding: 0.85rem 1rem;
	text-decoration: none;
}

.research-search-result-link:hover {
	background: rgba(64, 224, 208, 0.08);
	color: inherit;
}

.research-search-result-title {
	display: block;
	font-weight: 700;
	margin-bottom: 0.2rem;
}

.research-search-result-meta,
.research-search-empty {
	color: #52606d;
	display: block;
	font-size: 0.88rem;
	padding: 0.85rem 1rem;
}

.research-filter-panel {
	margin: 1.5rem 0 2rem;
}

.research-filter-label {
	display: inline-block;
	margin-right: 0.75rem;
	margin-bottom: 0.5rem;
	font-weight: 700;
}

.research-filter-buttons {
	display: inline-flex;
	flex-wrap: wrap;
	gap: 0.45rem;
	vertical-align: middle;
}

.research-filter-button {
	background-color: #ffffff;
	border: 2px solid var(--filter-accent, #40e0d0);
	border-radius: 999px;
	color: #1f2933;
	cursor: pointer;
	font-size: 0.78rem;
	font-weight: 700;
	line-height: 1.2;
	padding: 0.4rem 0.8rem;
	transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease;
}

.research-filter-button:hover,
.research-filter-button:focus-visible {
	background-color: #f3f4f6;
	outline: none;
}

.research-filter-button.is-active {
	background-color: var(--filter-accent, #40e0d0);
	border-color: var(--filter-accent, #40e0d0);
}

.research-tag-chip {
	cursor: pointer;
	transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.research-tag-chip:hover,
.research-tag-chip:focus-visible {
	box-shadow: 0 0 0 2px rgba(58, 99, 140, 0.18);
	outline: none;
	transform: translateY(-1px);
}

.research-tag-chip.is-selected-filter {
	box-shadow: 0 0 0 2px rgba(58, 99, 140, 0.28);
	transform: translateY(-1px);
}

.research-card-link {
	color: inherit;
	display: block;
	height: 100%;
}

.research-card-link:hover {
	color: inherit;
}

.research-card {
	height: 100%;
	transition: transform 0.18s ease, box-shadow 0.18s ease;
}


.research-card-media {
	background: #0f172a;
	overflow: hidden;
}

.research-card-media .image {
	background: #0f172a;
}

.research-card-image img {
	display: block;
	height: 100%;
	object-fit: cover;
	width: 100%;
}

.research-card-video-frame {
	align-items: center;
	background: #0f172a;
	display: flex;
	height: 100%;
	justify-content: center;
	left: 0;
	position: absolute;
	top: 0;
	width: 100%;
}

.research-card-video {
	background: #0f172a;
	display: block;
	height: auto;
	max-height: 100%;
	max-width: 100%;
	width: auto;
}

.research-card-link:hover .research-card,
.research-card-link:focus-visible .research-card {
	box-shadow: 0 1rem 2rem rgba(15, 23, 42, 0.12);
	transform: translateY(-4px);
}

.research-empty-state {
	display: none;
	margin-top: 1rem;
}
</style>

<div class="research-search-panel">
	<label class="research-filter-label" for="search-input">Search:</label>
	<div class="research-search-container">
		<input id="search-input" class="research-search-input" type="text" placeholder="Search research projects...">
		<ul id="results-container" class="results-container"></ul>
	</div>
</div>

<div class="research-filter-panel">
	<span class="research-filter-label">Filter by Tags:</span>
	<div id="research-filter-buttons" class="research-filter-buttons"></div>
</div>

<div id="research-grid" class="columns is-multiline">
	{% for post in research_posts %}
		{% assign card_id = post.title | slugify %}
		<div class="column is-3-desktop is-6-tablet research-card-column" id="{{ card_id }}">
			<a href="{{ post.url | relative_url }}" class="research-card-link">
				<div class="card research-card">
					<div class="card-image research-card-media{% unless post.video %} research-card-image{% endunless %}">
						{% if post.video %}
							<figure class="image is-4by3">
								<div class="research-card-video-frame">
									<video class="research-card-video" autoplay muted loop playsinline preload="metadata"{% if post.video_poster %} poster="{{ post.video_poster | relative_url }}"{% elsif post.image %} poster="{{ post.image | relative_url }}"{% endif %} aria-label="{{ post.title }} video preview">
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
					<div class="card-content">
						<p class="title is-5">{{ post.title }}</p>
						<div class="content">{{ post.summary }}</div>
						<div class="tags">
							{% for tag in post.tags %}
								<span class="tag is-info is-light research-tag-chip" data-tag="{{ tag }}" role="button" tabindex="0">{{ tag }}</span>
							{% endfor %}
						</div>
					</div>
				</div>
			</a>
		</div>
	{% endfor %}
</div>

<div id="research-empty-state" class="notification is-light research-empty-state">
	No research projects match the current search and filter settings.
</div>

<script src="https://cdn.jsdelivr.net/npm/simple-jekyll-search@1.10.0/dest/simple-jekyll-search.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
	var grid = document.getElementById('research-grid');
	var buttonHolder = document.getElementById('research-filter-buttons');
	var searchInput = document.getElementById('search-input');
	var resultsContainer = document.getElementById('results-container');
	var emptyState = document.getElementById('research-empty-state');
	if (!grid || !buttonHolder || !searchInput || !resultsContainer || !emptyState) {
		return;
	}

	var filterPalette = [
		'#40E0D0',
		'#DFFF00',
		'#FF3333',
		'#33FF4C',
		'#F633FF',
		'#CCCCFF',
		'#FFA533',
		'#33FFB2'
	];

	var selectedTags = new Set();
	var cards = Array.from(grid.querySelectorAll('.research-card-column')).map(function(column, index) {
		var tags = Array.from(column.querySelectorAll('.research-tag-chip')).map(function(tagElement) {
			return tagElement.textContent.trim();
		}).filter(Boolean);

		column.dataset.tags = tags.join('|');
		column.dataset.cardIndex = String(index);
		column.dataset.cardTitle = (column.querySelector('.title') || {}).textContent ? column.querySelector('.title').textContent.trim().toLowerCase() : '';
		column.dataset.cardSummary = (column.querySelector('.content') || {}).textContent ? column.querySelector('.content').textContent.trim().toLowerCase() : '';

		Array.from(column.querySelectorAll('.research-tag-chip')).forEach(function(tagElement) {
			tagElement.addEventListener('click', function(event) {
				event.preventDefault();
				event.stopPropagation();
				toggleTag(tagElement.textContent.trim());
			});
			tagElement.addEventListener('keydown', function(event) {
				if (event.key === 'Enter' || event.key === ' ') {
					event.preventDefault();
					toggleTag(tagElement.textContent.trim());
				}
			});
		});

		return {
			element: column,
			tags: tags
		};
	});

	var allTags = Array.from(new Set(cards.flatMap(function(card) {
		return card.tags;
	}))).sort();

	var buttons = new Map();

	function createButton(label, color, isAllButton) {
		var button = document.createElement('button');
		button.type = 'button';
		button.className = 'research-filter-button';
		button.textContent = label;
		button.style.setProperty('--filter-accent', color);
		button.addEventListener('click', function() {
			if (isAllButton) {
				selectedTags.clear();
			} else {
				toggleTag(label);
				return;
			}
			updateFilters();
		});
		buttonHolder.appendChild(button);
		return button;
	}

	var allButton = createButton('All', '#40E0D0', true);

	allTags.forEach(function(tag, index) {
		var color = filterPalette[index % filterPalette.length];
		buttons.set(tag, createButton(tag, color, false));
		Array.from(grid.querySelectorAll('.tags .tag')).forEach(function(tagElement) {
			if (tagElement.textContent.trim() === tag) {
				tagElement.style.setProperty('--filter-accent', color);
			}
		});
	});

	function toggleTag(tag) {
		if (selectedTags.has(tag)) {
			selectedTags.delete(tag);
		} else {
			selectedTags.add(tag);
		}
		updateFilters();
	}

	function matchesSearch(card) {
		var query = searchInput.value.trim().toLowerCase();
		if (!query) {
			return true;
		}

		return card.element.dataset.cardTitle.includes(query) ||
			card.element.dataset.cardSummary.includes(query) ||
			card.tags.some(function(tag) {
				return tag.toLowerCase().includes(query);
			});
	}

	function updateFilters() {
		var visibleCount = 0;

		cards.forEach(function(card) {
			var matchesTags = selectedTags.size === 0 || card.tags.some(function(tag) {
				return selectedTags.has(tag);
			});
			var shouldShow = matchesTags && matchesSearch(card);
			card.element.style.display = shouldShow ? '' : 'none';
			if (shouldShow) {
				visibleCount += 1;
			}
		});

		allButton.classList.toggle('is-active', selectedTags.size === 0);

		buttons.forEach(function(button, tag) {
			button.classList.toggle('is-active', selectedTags.has(tag));
		});

		Array.from(grid.querySelectorAll('.research-tag-chip')).forEach(function(tagElement) {
			tagElement.classList.toggle('is-selected-filter', selectedTags.has(tagElement.textContent.trim()));
		});

		emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
		resultsContainer.classList.toggle('has-results', searchInput.value.trim().length > 0);
	}

	if (window.SimpleJekyllSearch) {
		SimpleJekyllSearch({
			searchInput: searchInput,
			resultsContainer: resultsContainer,
			json: "{{ '/search.json' | relative_url }}",
			searchResultTemplate: '<li><a class="research-search-result-link" href="{url}"><span class="research-search-result-title">{title}</span><span class="research-search-result-meta">{tags}</span></a></li>',
			noResultsText: '<li class="research-search-empty">No matching projects</li>',
			limit: 8,
			fuzzy: false
		});
	}

	searchInput.addEventListener('input', function() {
		updateFilters();
	});

	searchInput.addEventListener('focus', function() {
		if (searchInput.value.trim().length > 0) {
			resultsContainer.classList.add('has-results');
		}
	});

	document.addEventListener('click', function(event) {
		if (!event.target.closest('.research-search-container')) {
			resultsContainer.classList.remove('has-results');
		}
	});

	updateFilters();
});
</script>