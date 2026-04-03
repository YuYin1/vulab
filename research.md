---
title: Research
subtitle: See our current research directions
layout: page
show_sidebar: false
---

This page highlights VU Lab research themes, ongoing projects, and selected directions.

The cards below are placeholders modeled after the project-card style used on AirLab's research page.

<style>
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
</style>

<div class="research-filter-panel">
	<span class="research-filter-label">Filter by Tags:</span>
	<div id="research-filter-buttons" class="research-filter-buttons"></div>
</div>

<div id="research-grid" class="columns is-multiline">
	<div class="column is-3-desktop is-6-tablet">
		<div class="card">
			<div class="card-image">
				<figure class="image is-4by3">
					<img src="{{ '/img/research/research-placeholder-01.svg' | relative_url }}" alt="Placeholder project 01">
				</figure>
			</div>
			<div class="card-content">
				<p class="title is-5">Placeholder Project 01</p>
				<div class="content">
					A placeholder research project on multimodal scene understanding for embodied systems operating in complex real-world environments.
				</div>
				<div class="tags">
					<span class="tag is-info is-light">Learning</span>
					<span class="tag is-info is-light">Perception</span>
					<span class="tag is-info is-light">Project Overview</span>
				</div>
			</div>
		</div>
	</div>
	<div class="column is-3-desktop is-6-tablet">
		<div class="card">
			<div class="card-image">
				<figure class="image is-4by3">
					<img src="{{ '/img/research/research-placeholder-02.svg' | relative_url }}" alt="Placeholder project 02">
				</figure>
			</div>
			<div class="card-content">
				<p class="title is-5">Placeholder Project 02</p>
				<div class="content">
					A placeholder research project on spatial intelligence, memory, and planning for long-horizon autonomous decision making.
				</div>
				<div class="tags">
					<span class="tag is-info is-light">Planning</span>
					<span class="tag is-info is-light">Spatial Intelligence</span>
					<span class="tag is-info is-light">Project Overview</span>
				</div>
			</div>
		</div>
	</div>
	<div class="column is-3-desktop is-6-tablet">
		<div class="card">
			<div class="card-image">
				<figure class="image is-4by3">
					<img src="{{ '/img/research/research-placeholder-03.svg' | relative_url }}" alt="Placeholder project 03">
				</figure>
			</div>
			<div class="card-content">
				<p class="title is-5">Placeholder Project 03</p>
				<div class="content">
					A placeholder research project on robust 3D mapping, geometry-aware learning, and adaptive navigation in dynamic settings.
				</div>
				<div class="tags">
					<span class="tag is-info is-light">SLAM</span>
					<span class="tag is-info is-light">Navigation</span>
					<span class="tag is-info is-light">Project Overview</span>
				</div>
			</div>
		</div>
	</div>
	<div class="column is-3-desktop is-6-tablet">
		<div class="card">
			<div class="card-image">
				<figure class="image is-4by3">
					<img src="{{ '/img/research/research-placeholder-04.svg' | relative_url }}" alt="Placeholder project 04">
				</figure>
			</div>
			<div class="card-content">
				<p class="title is-5">Placeholder Project 04</p>
				<div class="content">
					A placeholder research project on video-language grounding and open-world recognition for long-term autonomous agents.
				</div>
				<div class="tags">
					<span class="tag is-info is-light">Vision-Language</span>
					<span class="tag is-info is-light">Recognition</span>
					<span class="tag is-info is-light">Project Overview</span>
				</div>
			</div>
		</div>
	</div>
	<div class="column is-3-desktop is-6-tablet">
		<div class="card">
			<div class="card-image">
				<figure class="image is-4by3">
					<img src="{{ '/img/research/research-placeholder-05.svg' | relative_url }}" alt="Placeholder project 05">
				</figure>
			</div>
			<div class="card-content">
				<p class="title is-5">Placeholder Project 05</p>
				<div class="content">
					A placeholder research project on foundation models for robotic manipulation, task abstraction, and reusable control primitives.
				</div>
				<div class="tags">
					<span class="tag is-info is-light">Foundation Models</span>
					<span class="tag is-info is-light">Manipulation</span>
					<span class="tag is-info is-light">Project Overview</span>
				</div>
			</div>
		</div>
	</div>
	<div class="column is-3-desktop is-6-tablet">
		<div class="card">
			<div class="card-image">
				<figure class="image is-4by3">
					<img src="{{ '/img/research/research-placeholder-06.svg' | relative_url }}" alt="Placeholder project 06">
				</figure>
			</div>
			<div class="card-content">
				<p class="title is-5">Placeholder Project 06</p>
				<div class="content">
					A placeholder research project on uncertainty estimation, risk-sensitive inference, and robust deployment under distribution shift.
				</div>
				<div class="tags">
					<span class="tag is-info is-light">Uncertainty</span>
					<span class="tag is-info is-light">Robustness</span>
					<span class="tag is-info is-light">Project Overview</span>
				</div>
			</div>
		</div>
	</div>
	<div class="column is-3-desktop is-6-tablet">
		<div class="card">
			<div class="card-image">
				<figure class="image is-4by3">
					<img src="{{ '/img/research/research-placeholder-07.svg' | relative_url }}" alt="Placeholder project 07">
				</figure>
			</div>
			<div class="card-content">
				<p class="title is-5">Placeholder Project 07</p>
				<div class="content">
					A placeholder research project on interactive 3D world models for simulation, prediction, and scalable embodied training pipelines.
				</div>
				<div class="tags">
					<span class="tag is-info is-light">World Models</span>
					<span class="tag is-info is-light">Simulation</span>
					<span class="tag is-info is-light">Project Overview</span>
				</div>
			</div>
		</div>
	</div>
	<div class="column is-3-desktop is-6-tablet">
		<div class="card">
			<div class="card-image">
				<figure class="image is-4by3">
					<img src="{{ '/img/research/research-placeholder-08.svg' | relative_url }}" alt="Placeholder project 08">
				</figure>
			</div>
			<div class="card-content">
				<p class="title is-5">Placeholder Project 08</p>
				<div class="content">
					A placeholder research project on efficient multimodal retrieval, memory indexing, and semantic search over spatial experiences.
				</div>
				<div class="tags">
					<span class="tag is-info is-light">Retrieval</span>
					<span class="tag is-info is-light">Memory</span>
					<span class="tag is-info is-light">Project Overview</span>
				</div>
			</div>
		</div>
	</div>
	<div class="column is-3-desktop is-6-tablet">
		<div class="card">
			<div class="card-image">
				<figure class="image is-4by3">
					<img src="{{ '/img/research/research-placeholder-09.svg' | relative_url }}" alt="Placeholder project 09">
				</figure>
			</div>
			<div class="card-content">
				<p class="title is-5">Placeholder Project 09</p>
				<div class="content">
					A placeholder research project on human-robot collaboration, preference alignment, and adaptive interfaces for embodied AI systems.
				</div>
				<div class="tags">
					<span class="tag is-info is-light">HRI</span>
					<span class="tag is-info is-light">Alignment</span>
					<span class="tag is-info is-light">Project Overview</span>
				</div>
			</div>
		</div>
	</div>
	<div class="column is-3-desktop is-6-tablet">
		<div class="card">
			<div class="card-image">
				<figure class="image is-4by3">
					<img src="{{ '/img/research/research-placeholder-10.svg' | relative_url }}" alt="Placeholder project 10">
				</figure>
			</div>
			<div class="card-content">
				<p class="title is-5">Placeholder Project 10</p>
				<div class="content">
					A placeholder research project on scalable policy learning for mobile platforms operating across weather, terrain, and sensing conditions.
				</div>
				<div class="tags">
					<span class="tag is-info is-light">Policy Learning</span>
					<span class="tag is-info is-light">Generalization</span>
					<span class="tag is-info is-light">Project Overview</span>
				</div>
			</div>
		</div>
	</div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
	var grid = document.getElementById('research-grid');
	var buttonHolder = document.getElementById('research-filter-buttons');
	if (!grid || !buttonHolder) {
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
	var cards = Array.from(grid.querySelectorAll('.column')).map(function(column, index) {
		var tags = Array.from(column.querySelectorAll('.tags .tag')).map(function(tagElement) {
			return tagElement.textContent.trim();
		}).filter(Boolean);

		column.dataset.tags = tags.join('|');
		column.dataset.cardIndex = String(index);

		Array.from(column.querySelectorAll('.tags .tag')).forEach(function(tagElement) {
			tagElement.classList.add('research-tag-chip');
			tagElement.setAttribute('role', 'button');
			tagElement.setAttribute('tabindex', '0');
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

	function updateFilters() {
		cards.forEach(function(card) {
			var shouldShow = selectedTags.size === 0 || card.tags.some(function(tag) {
				return selectedTags.has(tag);
			});
			card.element.style.display = shouldShow ? '' : 'none';
		});

		allButton.classList.toggle('is-active', selectedTags.size === 0);

		buttons.forEach(function(button, tag) {
			button.classList.toggle('is-active', selectedTags.has(tag));
		});

		Array.from(grid.querySelectorAll('.tags .tag')).forEach(function(tagElement) {
			tagElement.classList.toggle('is-selected-filter', selectedTags.has(tagElement.textContent.trim()));
		});
	}

	updateFilters();
});
</script>