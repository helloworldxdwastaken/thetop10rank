
import os
import re

root_dir = "/Users/tokyo/Desktop/TheTop10Rank"

# The unified navigation block
new_nav = """
            <nav class="main-nav">
                <a href="/banks/">Banks</a>
                <a href="/design-studios/">Design Studios</a>
                <a href="/dentists/">Dentists</a>
                <a href="/gyms/">Gyms</a>
                <a href="/tattoo-studios/">Tattoo Studios</a>
                <a href="/hair-salons/">Hair Salons</a>
                <a href="/how-we-rank/">How We Rank</a>
                <a href="/about/">About</a>
            </nav>"""

# Regex to find existing nav
# It looks for <nav class="main-nav"> ... </nav> across multiple lines
nav_regex = re.compile(r'<nav class="main-nav">.*?</nav>', re.DOTALL)

count = 0

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".html"):
            filepath = os.path.join(dirpath, filename)
            
            with open(filepath, "r") as f:
                content = f.read()
            
            # Check if nav exists
            if '<nav class="main-nav">' in content:
                # Replace the entire nav block
                new_content = nav_regex.sub(new_nav.strip(), content)
                
                # Only write if there was a change
                if new_content != content:
                    with open(filepath, "w") as f:
                        f.write(new_content)
                    print(f"Updated nav in: {filepath}")
                    count += 1
                else:
                    print(f"No changes needed for: {filepath}")
            else:
                print(f"No nav found in: {filepath}")

print(f"Total files updated: {count}")
