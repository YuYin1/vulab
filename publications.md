---
title: Publications
subtitle: Our research is published in top-tier venues
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

.button0 {
    background-color: #003A70;
    border: none;
    color: white;
    padding: 2px 4px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 7px;
    font-weight: bold;
    margin-left: 20px;
    cursor: pointer;
    border-radius: 5px;
}

.button1,
.button2,
.button3,
.button4,
.button5 {
    border: none;
    color: white;
    padding: 2px 4px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 7px;
    font-weight: bold;
    margin: 2px 1px;
    cursor: pointer;
    border-radius: 5px;
}

.button1 { background-color: #2563EB; } /* doi */
.button2 { background-color: #7C3AED; } /* preprint */
.button3 { background-color: #059669; } /* cite / code */
.button4 { background-color: #D97706; } /* link */
.button5 { background-color: #DC2626; } /* video */

@media (min-width: 48em) {
    .button0 {
        background-color: #003A70;
        border: none;
        color: white;
        padding: 4px 8px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 10px;
        font-weight: bold;
        margin-left: 20px;
        cursor: pointer;
        border-radius: 5px;
    }

    .button1,
    .button2,
    .button3,
    .button4,
    .button5 {
        border: none;
        color: white;
        padding: 4px 8px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 10px;
        font-weight: bold;
        margin: 2px 1px;
        cursor: pointer;
        border-radius: 5px;
    }
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