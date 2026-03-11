import os
import glob
import re

html_files = glob.glob(r'c:\Users\Lenovo\uber\*.html')
js_files = glob.glob(r'c:\Users\Lenovo\uber\*.js')

all_files = html_files + js_files

for filepath in all_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Case-sensitive replacements
    content = content.replace('Uber', 'Stacklyuber')
    content = content.replace('uber', 'stacklyuber')
    content = content.replace('UBER', 'STACKLYUBER')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated text in {filepath}")

print("Successfully replaced all instances of Uber with Stacklyuber.")
