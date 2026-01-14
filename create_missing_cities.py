import os

base_dir = "/Users/tokyo/Desktop/TheTop10Rank"

tasks = [
    # Source, Destination, City Name, Update Title?
    ("/Users/tokyo/Desktop/TheTop10Rank/gyms/austin/index.html", "/Users/tokyo/Desktop/TheTop10Rank/gyms/chicago/index.html", "Chicago"),
    ("/Users/tokyo/Desktop/TheTop10Rank/gyms/austin/index.html", "/Users/tokyo/Desktop/TheTop10Rank/gyms/los-angeles/index.html", "Los Angeles"),
    ("/Users/tokyo/Desktop/TheTop10Rank/gyms/austin/index.html", "/Users/tokyo/Desktop/TheTop10Rank/gyms/miami/index.html", "Miami"),
    ("/Users/tokyo/Desktop/TheTop10Rank/gyms/austin/index.html", "/Users/tokyo/Desktop/TheTop10Rank/gyms/new-york/index.html", "New York"),
    ("/Users/tokyo/Desktop/TheTop10Rank/hair-salons/tampa/index.html", "/Users/tokyo/Desktop/TheTop10Rank/hair-salons/miami/index.html", "Miami"),
    ("/Users/tokyo/Desktop/TheTop10Rank/hair-salons/tampa/index.html", "/Users/tokyo/Desktop/TheTop10Rank/hair-salons/orlando/index.html", "Orlando"),
    ("/Users/tokyo/Desktop/TheTop10Rank/tattoo-studios/austin/index.html", "/Users/tokyo/Desktop/TheTop10Rank/tattoo-studios/london/index.html", "London"),
]

for src, dest, city_name in tasks:
    if os.path.exists(dest):
        print(f"Skipping {dest} (already exists)")
        continue
        
    if not os.path.exists(src):
        print(f"Source {src} missing!")
        continue
        
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Simple replace of City Name
    # Assuming source has "Austin" or "Tampa"
    src_city = "Austin" if "austin" in src else ("Tampa" if "tampa" in src else "Unknown")
    
    new_content = content.replace(src_city, city_name)
    
    # Also update dates to 2026 if not already (templates might be old?)
    # But we updated them previously.
    
    with open(dest, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Created {dest}")
