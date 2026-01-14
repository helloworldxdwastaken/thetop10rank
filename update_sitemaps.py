import os
import glob
from datetime import datetime

base_dir = "/Users/tokyo/Desktop/TheTop10Rank"
domain = "https://thetop10rank.com"
today = datetime.now().strftime("%Y-%m-%d")

# Map category to sitemap filename
sitemaps = {
    "banks": "sitemap-banks.xml",
    "design-studios": "sitemap-design-studios.xml",
    "dentists": "sitemap-dentists.xml",
    "gyms": "sitemap-gyms.xml",
    "hair-salons": "sitemap-hair-salons.xml",
    "tattoo-studios": "sitemap-tattoo-studios.xml",
    "restaurants": "sitemap-restaurants.xml",
    "clubs": "sitemap-clubs.xml",
    "main": "sitemap-main.xml"
}

# Generic Function to generate XML
def generate_xml(urls):
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for url in urls:
        xml.append('    <url>')
        xml.append(f'        <loc>{url}</loc>')
        xml.append(f'        <lastmod>{today}</lastmod>')
        xml.append('        <changefreq>weekly</changefreq>')
        xml.append('        <priority>0.8</priority>')
        xml.append('    </url>')
    xml.append('</urlset>')
    return "\n".join(xml)

# Usage: scan directory
for category, filename in sitemaps.items():
    urls = []
    
    if category == "main":
        # Special case for root pages
        root_pages = ["", "about", "contact", "privacy", "terms", "corrections", "editorial-policy", "how-we-rank", "changelog"]
        for p in root_pages:
            path = os.path.join(base_dir, p, "index.html") if p else os.path.join(base_dir, "index.html")
            if os.path.exists(path):
                urls.append(f"{domain}/{p}/" if p else f"{domain}/")
    else:
        # Recursive scan for category
        search_path = os.path.join(base_dir, category, "**/*.html")
        files = glob.glob(search_path, recursive=True)
        
        for f in files:
            # Convert to URL
            rel_path = f.replace(base_dir, "").lstrip("/")
            # Remove index.html
            if rel_path.endswith("index.html"):
                url_path = rel_path[:-10] # remove index.html
            else:
                url_path = rel_path
                
            urls.append(f"{domain}/{url_path}")
            
    # Write sitemap
    if urls:
        out_path = os.path.join(base_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(generate_xml(urls))
        print(f"Updated {filename} with {len(urls)} URLs")

print("Sitemaps updated.")
