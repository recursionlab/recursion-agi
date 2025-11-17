---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: recursive_ontology_site
version_uuid: 0fd7b827-9142-41ce-903a-3b6873887431
version_number: 1
command: create
conversation_id: a82836e1-9ef5-491b-8cb3-23defc1a9cb9
create_time: 2025-09-06T01:17:04.000Z
format: markdown
aliases: [Recursive Meta-Ontology + Journalism Site, recursive_ontology_site_v1]
---

# Recursive Meta-Ontology + Journalism Site (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/09/Free Website Platform Strategy|Free Website Platform Strategy]]

## Content

# _config.yml - Jekyll Configuration
title: "Recursive Ontologies | New World Order Analysis"
description: "Meta-ontological frameworks and journalism exploring emergent world systems"
url: "https://yourusername.github.io"
baseurl: "/recursive-ontology"

# Author info
author:
  name: "Your Name"
  email: "your.email@domain.com"
  twitter: "yourusername"

# Build settings
markdown: kramdown
highlighter: rouge
theme: minima
plugins:
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag

# Collections for organized content
collections:
  frameworks:
    output: true
    permalink: /:collection/:name/
  journalism:
    output: true
    permalink: /:collection/:name/
  ontologies:
    output: true
    permalink: /:collection/:name/

# Navigation
navigation:
  - title: "Home"
    url: "/"
  - title: "Framework"
    url: "/framework/"
  - title: "Journalism"
    url: "/journalism/"
  - title: "Ontologies"
    url: "/ontologies/"
  - title: "About"
    url: "/about/"

# Defaults
defaults:
  - scope:
      path: ""
      type: "frameworks"
    values:
      layout: "framework"
      author: "Your Name"
  - scope:
      path: ""
      type: "journalism"
    values:
      layout: "post"
      author: "Your Name"
  - scope:
      path: ""
      type: "ontologies"
    values:
      layout: "ontology"
      author: "Your Name"