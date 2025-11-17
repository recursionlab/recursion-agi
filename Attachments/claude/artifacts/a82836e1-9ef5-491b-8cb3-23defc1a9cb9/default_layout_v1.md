---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: default_layout
version_uuid: aed18893-2149-42bc-ae6f-96d9152fbe03
version_number: 1
command: create
conversation_id: a82836e1-9ef5-491b-8cb3-23defc1a9cb9
create_time: 2025-09-06T01:17:04.000Z
format: html
aliases: [Default Layout - _layoutsdefault.html, default_layout_v1]
---

# Default Layout - _layouts/default.html (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/09/Free Website Platform Strategy|Free Website Platform Strategy]]

## Content

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if page.title %}{{ page.title }} | {% endif %}{{ site.title }}</title>
    <meta name="description" content="{% if page.description %}{{ page.description }}{% else %}{{ site.description }}{% endif %}">
    
    <!-- SEO -->
    {% seo %}
    
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Main CSS -->
    <style>
        :root {
            --primary-color: #4f46e5;
            --secondary-color: #1a1a2e;
            --text-color: #333;
            --text-light: #666;
            --border-color: #e1e5e9;
            --bg-light: #f8f9fa;
            --shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background: white;
        }
        
        .site-header {
            background: white;
            border-bottom: 1px solid var(--border-color);
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: var(--shadow);
        }
        
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 70px;
        }
        
        .site-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--secondary-color);
            text-decoration: none;
        }
        
        .site-nav {
            display: flex;
            list-style: none;
            gap: 30px;
        }
        
        .site-nav a {
            text-decoration: none;
            color: var(--text-color);
            font-weight: 500;
            transition: color 0.3s ease;
        }
        
        .site-nav a:hover {
            color: var(--primary-color);
        }
        
        .main-content {
            min-height: calc(100vh - 140px);
        }
        
        .site-footer {
            background: var(--secondary-color);
            color: white;
            padding: 40px 0;
            text-align: center;
        }
        
        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .mobile-menu-toggle {
            display: none;
            background: none;
            border: none;
            font-size: 1.5rem;
            color: var(--text-color);
            cursor: pointer;
        }
        
        @media (max-width: 768px) {
            .site-nav {
                display: none;
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background: white;
                flex-direction: column;
                padding: 20px;
                box-shadow: var(--shadow);
            }
            
            .site-nav.active {
                display: flex;
            }
            
            .mobile-menu-toggle {
                display: block;
            }
        }
        
        /* Typography */
        h1, h2, h3, h4, h5, h6 {
            font-weight: 600;
            line-height: 1.3;
            margin-bottom: 1rem;
        }
        
        h1 { font-size: 2.5rem; }
        h2 { font-size: 2rem; }
        h3 { font-size: 1.5rem; }
        h4 { font-size: 1.25rem; }
        
        p {
            margin-bottom: 1rem;
        }
        
        a {
            color: var(--primary-color);
        }
        
        a:hover {
            text-decoration: underline;
        }
        
        /* Utilities */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .text-center {
            text-align: center;
        }
        
        .mt-4 { margin-top: 2rem; }
        .mb-4 { margin-bottom: 2rem; }
        .py-4 { padding: 2rem 0; }
    </style>
</head>
<body>
    <header class="site-header">
        <div class="header-content">
            <a href="{{ '/' | relative_url }}" class="site-title">{{ site.title | split: ' | ' | first }}</a>
            
            <nav>
                <ul class="site-nav" id="site-nav">
                    {% for item in site.navigation %}
                        <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
                    {% endfor %}
                </ul>
                
                <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">☰</button>
            </nav>
        </div>
    </header>
    
    <main class="main-content">
        {{ content }}
    </main>
    
    <footer class="site-footer">
        <div class="footer-content">
            <p>&copy; {{ 'now' | date: "%Y" }} {{ site.author.name }}. Exploring recursive ontologies and emergent world systems.</p>
            <p>
                <a href="mailto:{{ site.author.email }}" style="color: #ccc;">Contact</a> | 
                <a href="/feed.xml" style="color: #ccc;">RSS</a>
            </p>
        </div>
    </footer>
    
    <script>
        function toggleMobileMenu() {
            const nav = document.getElementById('site-nav');
            nav.classList.toggle('active');
        }
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            const nav = document.getElementById('site-nav');
            const toggle = document.querySelector('.mobile-menu-toggle');
            
            if (!nav.contains(event.target) && !toggle.contains(event.target)) {
                nav.classList.remove('active');
            }
        });
    </script>
</body>
</html>
```