
import os
import re

HEADER_START_TAG = '<!-- Header -->'
HEADER_END_TAG = '</header>'

def get_master_header():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(f'({HEADER_START_TAG}.*?{HEADER_END_TAG})', content, re.DOTALL)
    if match:
        return match.group(1)
    else:
        raise Exception("Could not find header in index.html")

def deactivate_home(header_html):
    # Active Home style from index.html
    active_style = 'class="nav-item active px-4 py-2 text-white font-semibold transition-all duration-300 border-b-3 border-golden-400"'
    # Target Inactive style (standard generic link)
    inactive_style = 'class="nav-item px-4 py-2 text-white hover:text-golden-300 font-medium transition-all duration-300 border-b-3 border-transparent"'
    
    return header_html.replace(active_style, inactive_style)

def activate_link(header_html, filename):
    # Base active style parts
    base_classes = 'nav-item active px-4 py-2 text-white font-semibold transition-all duration-300'
    border_class = 'border-b-3 border-golden-400'
    
    # Mapping
    target_link_href = None
    target_button_text = None
    is_flex = False
    
    products_pages = [
        'products.html', 'scaffolding.html', 'solar-solutions.html', 'oil-gas.html', 
        'building-materials.html', 'fresh-provisions.html', 'grains-pulses.html', 
        'spices.html', 'meat-poultry.html', 'seafood.html', 'processed-foods.html', 
        'cooking-oils.html', 'dry-fruits.html', 'ship-chandling.html'
    ]
    
    about_pages = ['about.html', 'leadership.html', 'certifications.html', 'quality-assurance.html', 'consulting.html']
    
    if filename == 'services.html':
        target_link_href = 'services.html'
    elif filename == 'contact.html':
        target_link_href = 'contact.html'
    elif filename in products_pages:
        target_link_href = 'products.html'
        is_flex = True
    elif filename in about_pages:
        target_button_text = 'About'
        is_flex = True

    if not target_link_href and not target_button_text:
        return header_html

    # Construct the full active class string
    final_active_class = base_classes
    if is_flex:
        final_active_class += ' flex items-center'
    final_active_class += f' {border_class}'


    if target_button_text:
        # Targeting the Button (About)
        # Regex to find: <button ...>...About
        # We need to replace the class attribute of this button.
        # We assume the button has class="..." before the text "About"
        # Since we are working with the string from index.html, we know the structure.
        # <button class="nav-item ...">
        #    About <i ...
        
        # We'll use a specific regex for the About button in index.html
        # It looks like: class="nav-item px-4 py-2 text-white hover:text-golden-300 font-medium transition-all duration-300 flex items-center border-b-3 border-transparent"
        
        inactive_button_class = 'nav-item px-4 py-2 text-white hover:text-golden-300 font-medium transition-all duration-300 flex items-center border-b-3 border-transparent'
        
        # We just replace the distinctive part of the inactive class with active class
        # But wait, there might be multiple buttons? No, just "About" and mobile menu button (which has different classes).
        # To be safe, look for the button followed immediately by "About"
        
        pattern = r'(<button\s+class=")([^"]+)(">\s*About)'
        # We replace group 2 with final_active_class
        if re.search(pattern, header_html):
             header_html = re.sub(pattern, f'\\1{final_active_class}\\3', header_html)
             
    elif target_link_href:
        # Targeting <a> link
        # Look for <a href="target"... class="..."> OR <a class="..." href="target">
        # In index.html: <a href="services.html" class="...">
        
        # Inactive class for flex items (Products)
        inactive_flex_class = 'nav-item px-4 py-2 text-white hover:text-golden-300 font-medium transition-all duration-300 flex items-center border-b-3 border-transparent'
        # Inactive class for non-flex items (Services, Contact)
        inactive_std_class = 'nav-item px-4 py-2 text-white hover:text-golden-300 font-medium transition-all duration-300 border-b-3 border-transparent'
        
        target_inactive_class = inactive_flex_class if is_flex else inactive_std_class
        
        # We will try to replace the class attribute for the specific link
        # Pattern: <a href="products.html" class="OLD_CLASS"
        pattern = f'(<a\\s+href="{target_link_href}"\\s+class=")([^"]+)(")'
        
        if re.search(pattern, header_html):
            header_html = re.sub(pattern, f'\\1{final_active_class}\\3', header_html)

    return header_html

def apply_header():
    try:
        master_header = get_master_header()
        print("Successfully read master header from index.html")
    except Exception as e:
        print(e)
        return

    neutral_header = deactivate_home(master_header)
    
    files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
    count = 0
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_header = activate_link(neutral_header, file)
        
        pattern = f'{HEADER_START_TAG}.*?{HEADER_END_TAG}'
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, new_header, content, count=1, flags=re.DOTALL)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
            count += 1
        else:
            print(f"Skipped {file} (Header tags not found)")

    print(f"Total files updated: {count}")

if __name__ == '__main__':
    apply_header()
