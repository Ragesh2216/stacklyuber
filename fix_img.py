import urllib.request
import os

req = urllib.request.Request('https://picsum.photos/seed/uberhome1/800/400.webp', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response, open('images/home2_img1.webp', 'wb') as out_file:
    out_file.write(response.read())

size_kb = os.path.getsize('images/home2_img1.webp') / 1024
print(f'New size: {size_kb:.2f} KB')
