---
title: Publications
# subtitle: Browse papers, preprints, and reports
layout: page
show_sidebar: false
hero_height: is-small
---

<style>
.csl-block {
    font-size: 16px;
}

.csl-title,
.csl-author,
.csl-event,
.csl-editor,
.csl-venue {
    display: block;
    position: relative;
    font-size: 16px;
}

.csl-title b {
    font-weight: 600;
}

.csl-content {
    display: inline-block;
    vertical-align: top;
    padding-left: 20px;
}

.bibliography {
    list-style-type: none;
}

.bibliography > li::marker {
    content: "[" counter(list-item) "]";
    counter-increment: list;
}

.publication-actions {
    margin-top: 0.5rem;
}

.publication-actions .button {
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
}

.publication-panel {
    display: none;
    margin-top: 0.75rem;
}

.publication-panel pre {
    white-space: pre-wrap;
    word-break: break-word;
}
</style>

# 2026
{% bibliography --query @*[year=2026] %}

# 2025
{% bibliography --query @*[year=2025] %}

# 2024
{% bibliography --query @*[year=2024] %}

# 2023
{% bibliography --query @*[year=2023] %}