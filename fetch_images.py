import urllib.request
import os

urls = [
    'https://picsum.photos/seed/uberhome1/800/600.webp',
    'https://picsum.photos/seed/uberhome2/800/500.webp',
    'https://picsum.photos/seed/uberhome3/800/500.webp'
]

os.makedirs('images', exist_ok=True)

for i, url in enumerate(urls):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
    webp_path = f'images/home2_img{i+1}.webp'
    
    with urllib.request.urlopen(req) as response, open(webp_path, 'wb') as out_file:
        out_file.write(response.read())
    
    size_kb = os.path.getsize(webp_path) / 1024
    print(f'Saved {webp_path}, size: {size_kb:.2f} KB')
