import glob

html_files = glob.glob(r'c:\Users\Lenovo\uber\*.html')

desktop_add = """
                <div class="dropdown">
                    <button class="nav-link dropdown-btn">Home 2 <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                    <div class="dropdown-content">
                        <a href="home2.html">Home 2 Page</a>
                    </div>
                </div>"""

mobile_add = """
            <button class="mobile-dropdown-btn" onclick="this.nextElementSibling.classList.toggle('show')">Home 2 <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
            <div class="mobile-dropdown-content">
                <a href="home2.html">Home 2 Page</a>
            </div>"""

for filepath in html_files:
    if '404' in filepath or 'login' in filepath or 'dashboard' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Inject desktop Dropdown
    if '<a href="index.html" class="nav-link active">Home</a>' in content:
        content = content.replace('<a href="index.html" class="nav-link active">Home</a>', '<a href="index.html" class="nav-link active">Home</a>' + desktop_add)
    elif '<a href="index.html" class="nav-link">Home</a>' in content:
        content = content.replace('<a href="index.html" class="nav-link">Home</a>', '<a href="index.html" class="nav-link">Home</a>' + desktop_add)
        
    # Inject mobile Dropdown
    if '<a href="index.html" class="mobile-nav-link">Home</a>' in content:
        content = content.replace('<a href="index.html" class="mobile-nav-link">Home</a>', '<a href="index.html" class="mobile-nav-link">Home</a>' + mobile_add)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated navigation in HTML files successfully.")
