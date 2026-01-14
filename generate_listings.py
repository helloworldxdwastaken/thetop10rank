import os
import glob
import re
import shutil

base_dir = "/Users/tokyo/Desktop/TheTop10Rank"

# Template for listing page
listing_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - {category} Review | Rankin</title>
    <link rel="stylesheet" href="/assets/css/main.css">
    <link rel="icon" type="image/png" href="/assets/images/logo%20and%20artwork/logo.png">
</head>
<body>
    <header class="site-header">
        <div class="container">
            <div class="logo"><a href="/"><img src="/assets/images/logo%20and%20artwork/logo.png" alt="TheTop10Rank" class="site-logo"></a></div>
            <nav class="main-nav">
                <a href="/banks/">Banks</a>
                <a href="/design-studios/">Design Studios</a>
                <a href="/dentists/">Dentists</a>
                <a href="/gyms/">Gyms</a>
                <a href="/tattoo-studios/">Tattoo Studios</a>
                <a href="/hair-salons/">Hair Salons</a>
                <a href="/how-we-rank/">How We Rank</a>
                <a href="/about/">About</a>
            </nav>
        </div>
    </header>

    <main>
        <section class="hero" style="background: linear-gradient(135deg, #0B1F3A 0%, #1e3a8a 100%); color: white; min-height: 50vh;">
            <div class="container">
                <div class="breadcrumb" style="padding: 0 0 20px 0;"><a href="/">Home</a> / <a href="/{root_slug}/">{category}</a> / <span>{name}</span></div>
                <div class="listing-header">
                    <span class="rank-badge-large" style="background: var(--secondary); color: var(--primary); padding: 5px 15px; border-radius: 20px; font-weight: bold;">Rank #{rank} in {city}</span>
                    <h1 style="margin-top: 20px;">{name}</h1>
                </div>
            </div>
        </section>

        <section>
            <div class="container">
                <div class="listing-details">
                    <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #eee;">
                        <h2>Review Summary</h2>
                        <p><strong>{name}</strong> is ranked <strong>#{rank}</strong> out of top {category} in {city}.</p>
                        
                        <div style="margin-top: 30px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
                            <div class="stat-box">
                                <h4 style="color: var(--primary);">Score</h4>
                                <span style="font-size: 2em; font-weight: bold; color: var(--secondary);">{score}</span>
                            </div>
                            <div class="stat-box">
                                <h4 style="color: var(--primary);">Specialization</h4>
                                <p>{specialization}</p>
                            </div>
                            <div class="stat-box">
                                <h4 style="color: var(--primary);">Best For</h4>
                                <p>{best_for}</p>
                            </div>
                        </div>

                        <div style="margin-top: 40px;">
                            <a href="{external_link}" class="cta-button" target="_blank" rel="noopener">Visit Official Website</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="site-footer">
        <div class="container">
             <div class="footer-bottom">
                <p>&copy; 2025 Rankin. All rankings are editorial opinions based on published criteria.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""

# Scan for index files
html_files = glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True)

# Regex to find table rows
row_pattern = re.compile(r'<tr>(.*?)</tr>', re.DOTALL)
col_pattern = re.compile(r'<td.*?>(.*?)</td>', re.DOTALL)
link_pattern = re.compile(r'href=["\']([^"\']+)["\']')

count = 0

for file_path in html_files:
    # Skip if not an index file (likely) or if it's not a city page
    # A simple heuristic: city pages usually have a table.ranking-table
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "ranking-table" not in content:
        continue
        
    print(f"Processing {file_path}...")
    
    # Determine basic info
    parts = file_path.replace(base_dir, "").strip("/").split("/")
    if len(parts) >= 2:
        root_slug = parts[0] # e.g. hair-salons
        city = parts[1].replace("-", " ").title() if len(parts) > 1 else "Unknown"
        category = root_slug.replace("-", " ").title()
    else:
        continue
        
    # Extract rows within tbody
    tbody_search = re.search(r'<tbody>(.*?)</tbody>', content, re.DOTALL)
    if not tbody_search:
        continue
        
    tbody_content = tbody_search.group(1)
    rows = row_pattern.findall(tbody_content)
    
    for row in rows:
        cols = col_pattern.findall(row)
        if len(cols) < 5:
            continue
            
        # Parse Cols
        # 0: Rank span
        # 1: Name strong a
        # 2: Score span
        # 3: Spec
        # 4: Best For
        # 5: Button (optional)
        
        try:
            rank = re.sub(r'<[^>]+>', '', cols[0]).strip()
            
            name_html = cols[1]
            name = re.sub(r'<[^>]+>', '', name_html).strip()
            
            # Extract internal link from name col if exists
            target_link = None
            link_match = link_pattern.search(name_html)
            if link_match:
                target_link = link_match.group(1)
            
            score = re.sub(r'<[^>]+>', '', cols[2]).strip()
            specialization = cols[3].strip()
            best_for = cols[4].strip()
            
            # If target link is internal (points to listings/), generate that file
            if target_link and '/listings/' in target_link:
                # Construct path
                if target_link.startswith("/"):
                    # Absolute
                    rel_path = target_link.lstrip("/")
                else:
                    # Relative
                    rel_path = os.path.normpath(os.path.join(os.path.dirname(file_path), target_link).replace(base_dir, "").lstrip("/"))

                full_target_path = os.path.join(base_dir, rel_path)
                
                # If it looks like a directory (ends in /) or does not end in .html, append index.html
                if target_link.endswith("/") or not full_target_path.endswith(".html"):
                    full_target_path = os.path.join(full_target_path, "index.html")

                # Check if file exists, if not create it
                if not os.path.exists(full_target_path):
                    # Find external link (usually in the button in col 5)
                    external_link = "#"
                    if len(cols) > 5:
                         btn_link_match = link_pattern.search(cols[5])
                         if btn_link_match:
                             external_link = btn_link_match.group(1)
                    
                    # Ensure dir
                    os.makedirs(os.path.dirname(full_target_path), exist_ok=True)
                    
                    # Render
                    page_content = listing_template.format(
                        name=name,
                        category=category,
                        root_slug=root_slug,
                        city=city,
                        rank=rank,
                        score=score,
                        specialization=specialization,
                        best_for=best_for,
                        external_link=external_link
                    )
                    
                    # Write
                    with open(full_target_path, "w", encoding="utf-8") as out_f:
                        out_f.write(page_content)
                    
                    print(f"Created listing: {full_target_path}")
                    count += 1
                    
        except Exception as e:
            print(f"Error parsing row: {e}")

print(f"Generated {count} listing pages.")
