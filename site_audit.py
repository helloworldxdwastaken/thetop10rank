import os
import glob
import re

base_dir = "/Users/tokyo/Desktop/TheTop10Rank"
html_files = glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True)

issues = []

for file_path in html_files:
    rel_path = file_path.replace(base_dir, "")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1. SEO CHECKS
        if "<title>" not in content:
            issues.append(f"[SEO] Missing <title>: {rel_path}")
        if 'name="description"' not in content:
            issues.append(f"[SEO] Missing Meta Description: {rel_path}")
        if '<h1' not in content:
            issues.append(f"[SEO] Missing <h1>: {rel_path}")
        if 'rel="canonical"' not in content:
            issues.append(f"[SEO] Missing Canonical Tag: {rel_path}")
            
        # 2. DATE CHECKS
        # Suspicious old years in context of "Best ... 2024" or "2023"
        if "2024" in content:
             # Check context - might be historical, but flag it
             issues.append(f"[DATE] '2024' found (potential stale content): {rel_path}")
        if "2023" in content:
             issues.append(f"[DATE] '2023' found (potential stale content): {rel_path}")
             
        # 3. UI COHERENCE
        if "site-header" not in content and "navbar" not in content: # relaxed check
            issues.append(f"[UI] Missing Standard Header class: {rel_path}")
        if "site-footer" not in content:
            issues.append(f"[UI] Missing Standard Footer class: {rel_path}")
        if "assets/css/main.css" not in content:
            issues.append(f"[UI] Missing Main CSS link: {rel_path}")
        if "assets/js/main.js" not in content:
            issues.append(f"[UI] Missing Main JS script: {rel_path}")

    except Exception as e:
        issues.append(f"[ERROR] Could not read {rel_path}: {e}")

# Output results
if issues:
    print("Found the following potential issues:")
    for i in sorted(issues):
        print(i)
else:
    print("No obvious issues found.")
