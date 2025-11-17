---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: site_index
version_uuid: 9f6c80b1-63b8-4e81-91aa-5cb11ab8236e
version_number: 1
command: create
conversation_id: a82836e1-9ef5-491b-8cb3-23defc1a9cb9
create_time: 2025-09-06T01:17:04.000Z
format: html
aliases: [Homepage - index.html, site_index_v1]
---

# Homepage - index.html (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/09/Free Website Platform Strategy|Free Website Platform Strategy]]

## Content

```html
---
layout: default
title: "Recursive Ontologies | Mapping the New World Order"
---

<div class="hero-section">
  <div class="hero-content">
    <h1>Recursive Meta-Ontological Framework</h1>
    <p class="hero-subtitle">Mapping emergent world systems through recursive analysis and investigative journalism</p>
    <div class="hero-actions">
      <a href="/framework/" class="btn-primary">Explore Framework</a>
      <a href="/journalism/" class="btn-secondary">Latest Analysis</a>
    </div>
  </div>
</div>

<section class="intro-section">
  <div class="container">
    <div class="row">
      <div class="col-md-8">
        <h2>Understanding Recursive Systems</h2>
        <p>The world order is not static—it's a recursive system of interlocking patterns that generate new realities while referencing their own structures. This site documents both the journalistic investigation and the meta-ontological framework needed to comprehend these dynamics.</p>
        
        <div class="framework-preview">
          <h3>Core Principles</h3>
          <ul class="principle-list">
            <li><strong>Recursive Analysis:</strong> Systems that reference and modify themselves</li>
            <li><strong>Meta-Ontological Mapping:</strong> The study of how reality-frameworks emerge</li>
            <li><strong>Pattern Recognition:</strong> Identifying self-similar structures across scales</li>
            <li><strong>Journalistic Verification:</strong> Grounding theory in observable phenomena</li>
          </ul>
        </div>
      </div>
      
      <div class="col-md-4">
        <div class="sidebar-widget">
          <h3>Latest Updates</h3>
          <div class="recent-posts">
            {% for post in site.journalism limit:3 %}
              <div class="recent-post">
                <h4><a href="{{ post.url }}">{{ post.title }}</a></h4>
                <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
                <p>{{ post.excerpt | strip_html | truncate: 100 }}</p>
              </div>
            {% endfor %}
          </div>
          
          <a href="/journalism/" class="view-all">View All Articles →</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="framework-overview">
  <div class="container">
    <h2>Framework Components</h2>
    <div class="component-grid">
      <div class="component-card">
        <h3><a href="/ontologies/recursive-structures/">Recursive Structures</a></h3>
        <p>How systems reference and modify their own operational logic</p>
      </div>
      
      <div class="component-card">
        <h3><a href="/ontologies/emergence-patterns/">Emergence Patterns</a></h3>
        <p>Tracking how new organizational forms arise from existing systems</p>
      </div>
      
      <div class="component-card">
        <h3><a href="/ontologies/meta-analysis/">Meta-Analysis Tools</a></h3>
        <p>Methods for analyzing the analysis—recursive examination techniques</p>
      </div>
      
      <div class="component-card">
        <h3><a href="/frameworks/verification-protocols/">Verification Protocols</a></h3>
        <p>Journalistic methods adapted for complex systems research</p>
      </div>
    </div>
  </div>
</section>

<style>
.hero-section {
  background: linear-gradient(135deg, #1a1a2e, #16213e);
  color: white;
  padding: 100px 0;
  text-align: center;
}

.hero-content h1 {
  font-size: 3.5rem;
  font-weight: 300;
  margin-bottom: 1rem;
  letter-spacing: -1px;
}

.hero-subtitle {
  font-size: 1.3rem;
  opacity: 0.9;
  margin-bottom: 2rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.hero-actions {
  margin-top: 2rem;
}

.btn-primary, .btn-secondary {
  display: inline-block;
  padding: 12px 30px;
  margin: 0 10px;
  text-decoration: none;
  border-radius: 5px;
  font-weight: 500;
  transition: all 0.3s ease;
}

.btn-primary {
  background: #4f46e5;
  color: white;
}

.btn-primary:hover {
  background: #4338ca;
}

.btn-secondary {
  border: 2px solid #4f46e5;
  color: #4f46e5;
}

.btn-secondary:hover {
  background: #4f46e5;
  color: white;
}

.intro-section {
  padding: 80px 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.row {
  display: flex;
  gap: 40px;
}

.col-md-8 {
  flex: 2;
}

.col-md-4 {
  flex: 1;
}

.principle-list {
  list-style: none;
  padding: 0;
}

.principle-list li {
  padding: 10px 0;
  border-bottom: 1px solid #eee;
}

.sidebar-widget {
  background: #f8f9fa;
  padding: 30px;
  border-radius: 8px;
}

.recent-post {
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #dee2e6;
}

.recent-post h4 {
  margin: 0 0 5px 0;
}

.recent-post h4 a {
  color: #333;
  text-decoration: none;
}

.post-meta {
  color: #666;
  font-size: 0.9rem;
  margin: 0 0 10px 0;
}

.framework-overview {
  background: #f8f9fa;
  padding: 80px 0;
}

.component-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
  margin-top: 40px;
}

.component-card {
  background: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.component-card:hover {
  transform: translateY(-5px);
}

.component-card h3 a {
  color: #333;
  text-decoration: none;
}

.view-all {
  color: #4f46e5;
  text-decoration: none;
  font-weight: 500;
}

@media (max-width: 768px) {
  .row {
    flex-direction: column;
  }
  
  .hero-content h1 {
    font-size: 2.5rem;
  }
  
  .component-grid {
    grid-template-columns: 1fr;
  }
}
</style>
```