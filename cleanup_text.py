import glob

html_files = glob.glob(r'c:\Users\Lenovo\uber\*.html')
js_files = glob.glob(r'c:\Users\Lenovo\uber\*.js')
all_files = html_files + js_files

for filepath in all_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Fix double-replacements
    content = content.replace('Stacklystacklyuber', 'Stacklyuber')
    content = content.replace('STACKLYSTACKLYUBER', 'STACKLYUBER')
    content = content.replace('stacklystacklyuber', 'stacklyuber')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed double string in {filepath}")

print("Successfully cleaned up text.")
