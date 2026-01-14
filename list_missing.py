import os
import glob
import re
from urllib.parse import unquote

base_dir = "/Users/tokyo/Desktop/TheTop10Rank"

html_files = glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True)

missing_files = set()

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    ref_matches = re.findall(r'href=["\']([^"\']+)["\']', content)
    
    for ref in ref_matches:
        if ref.startswith(('http', 'https', 'mailto:', 'tel:', '#', 'javascript:')):
            continue
        
        # Clean ref
        clean_ref = ref.split('#')[0].split('?')[0]
        clean_ref = unquote(clean_ref)
        
        if not clean_ref or clean_ref == "/":
            continue
            
        # Determine strict path
        if clean_ref.startswith('/'):
            target_path = os.path.join(base_dir, clean_ref.lstrip('/'))
        else:
            target_path = os.path.join(os.path.dirname(file_path), clean_ref)
            
        target_path = os.path.normpath(target_path)
        
        # Check existence
        exists = False
        if os.path.exists(target_path):
            if os.path.isdir(target_path):
                if os.path.exists(os.path.join(target_path, "index.html")):
                    exists = True
            else:
                exists = True
        
        if not exists:
            # We want the "intended" file path. 
            # If it looks like a directory, append index.html for report
            if not target_path.endswith('.html') and not os.path.splitext(target_path)[1]:
                 missing_files.add(os.path.join(target_path, "index.html"))
            else:
                 missing_files.add(target_path)

print("Missing Files to Create:")
for p in sorted(missing_files):
    # Print relative path
    print(os.path.relpath(p, base_dir))
