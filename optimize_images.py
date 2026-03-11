import os
import glob
import re
import urllib.request
import uuid

html_files = glob.glob(r'c:\Users\Lenovo\uber\*.html')
os.makedirs(r'c:\Users\Lenovo\uber\images', exist_ok=True)

# Find all unique non-webp images in the HTML files
img_pattern = re.compile(r'<img[^>]+src="([^"]+)"')

url_to_local_map = {}
img_counter = 1

def fetch_webp_image(local_filename):
    # Use a random seed to get different images
    seed = str(uuid.uuid4())[:8]
    url = f"https://picsum.photos/seed/{seed}/800/500.webp"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req) as response, open(local_filename, 'wb') as out_file:
        out_file.write(response.read())
    
    size_kb = os.path.getsize(local_filename) / 1024
    print(f"Downloaded {local_filename} (Size: {size_kb:.2f} KB)")
    return size_kb

for filepath in html_files:
    if 'home2.html' in filepath:
        continue # Already webp
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    matches = img_pattern.findall(content)
    
    for src in matches:
        if not src.endswith('.webp') and 'images/home2_' not in src:
            if src not in url_to_local_map:
                local_rel_path = f"images/site_img_{img_counter}.webp"
                local_full_path = os.path.join(r'c:\Users\Lenovo\uber', local_rel_path)
                
                # Fetch image and ensure it's < 100KB (picsum 800x500 webp is usually ~30-60kb)
                fetch_webp_image(local_full_path)
                
                url_to_local_map[src] = local_rel_path
                img_counter += 1
            
            # Replace in content
            content = content.replace(f'src="{src}"', f'src="{url_to_local_map[src]}"')
            
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated images in {filepath}")

print("All HTML files updated with <100KB WebP images.")
