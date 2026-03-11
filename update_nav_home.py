import glob
import re

html_files = glob.glob(r'c:\Users\Lenovo\uber\*.html')

desktop_replacement_active = """            <!-- Desktop Nav -->
            <nav class="nav-menu">
                <div class="dropdown">
                    <button class="nav-link dropdown-btn active">Home <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                    <div class="dropdown-content">
                        <a href="index.html">Home 1</a>
                        <a href="home2.html">Home 2</a>
                    </div>
                </div>
                <a href="services.html" """

desktop_replacement_inactive = """            <!-- Desktop Nav -->
            <nav class="nav-menu">
                <div class="dropdown">
                    <button class="nav-link dropdown-btn">Home <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
                    <div class="dropdown-content">
                        <a href="index.html">Home 1</a>
                        <a href="home2.html">Home 2</a>
                    </div>
                </div>
                <a href="services.html" """

mobile_replacement = """        <nav class="mobile-nav-list">
            <button class="mobile-dropdown-btn" onclick="this.nextElementSibling.classList.toggle('show')">Home <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
            <div class="mobile-dropdown-content">
                <a href="index.html">Home 1</a>
                <a href="home2.html">Home 2</a>
            </div>
            <a href="services.html" """

for filepath in html_files:
    if '404' in filepath or 'login' in filepath or 'dashboard' in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop replacement
    is_active = filepath.endswith('index.html') or filepath.endswith('home2.html')
    replacement = desktop_replacement_active if is_active else desktop_replacement_inactive
    
    content = re.sub(
        r'<!-- Desktop Nav -->\s*<nav class="nav-menu">.*?<a href="services\.html"\s',
        replacement,
        content,
        flags=re.DOTALL
    )

    # Mobile replacement
    content = re.sub(
        r'<nav class="mobile-nav-list">.*?<a href="services\.html"\s',
        mobile_replacement,
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated navigation to unify Home dropdown in HTML files successfully.")
