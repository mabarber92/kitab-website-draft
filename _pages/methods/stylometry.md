---
excerpt:	""
header:
  overlay_image: /images/covers/banner_methods.png
  overlay_filter: rgba(40, 99, 165, 0.60)
title:		"Stylometry"

layout:		single
toc: true
toc_sticky: true

permalink: /methods/stylometry
sidebar:
  nav: "methods"
---

Stylometry, or the computational analysis of writing style, is based on the premise that each author has a unique way of writing, which can be quantified in the form of word frequencies and be measured against texts by other authors. As such, stylometry can enhance traditional ‘close reading’ by focusing on one or several texts, as well as ‘distant reading’ approaches by analysing and visualising enormous corpora at once for macroanalysis. Stylometry is most used in literary history for authorship attribution and genre detection. This makes it also a relevant and attractive method for the study of textual heritage in Arabic and Persian. It must be said that most of the methods and tools currently available are designed for and trained on Western languages and literatures. At KITAB we are interested in adapting methods and techniques from stylometry to the study of the Arabic texts, which by virtue of its intertextuality presents different types of challenges from that of European languages, but also exciting opportunities for researchers. With every OpenITI corpus release we also prepare a parallel corpus specially pre-processed for use with the Stylometric program, [R stylo]( https://cran.r-project.org/web/packages/stylo/index.html).

{% capture figure1 %}
[![A dentrogram produced through R stylo](/images/methods/Stylometry-tree.png)](/images/methods/Stylometry-tree.png)

*Figure 1. Cluster Analysis of about 2000 texts from the first five hundred years of the Arabic book (622-1111 CE).*
{% endcapture %}

<div class="notice--primary">
{{ figure1 | markdownify }}
</div>

## Networks from Stylo results

Thematic and stylistic relationship between texts in a corpus can also be viewed as a network in which the strength of the relationship is determined by the distance between them. In other words, the corpus as a network in which all texts are related to each other with varying degrees of similarity. Individual books are nodes and the distances between them are the edges (links). We can gauge the degree of similarity and influence between the texts by how closely they are located to each other in the network. The package  R stylo produces a table of links between the books in the corpus, which can then be fed to a network analysis software such as Gephi, or other network analysis packages.

{% capture figure2 %}
[![A network produced using data from R stylo](/images/methods/network-from-stylo.svg)](/images/methods/network-from-stylo.svg)

*Figure 2. A network based on stylometric distance between the books in the corpus of 500 years of Arabic Written Tradition*
{% endcapture %}

<div class="notice--primary">
{{ figure2 | markdownify }}
</div>