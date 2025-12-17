
import os
import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    filename = os.path.basename(filepath)

    # 1. Add Building Materials Link to Header (All Files)
    # Target the Spices link to insert after it
    spices_pattern = re.compile(r'(<a href="spices\.html"[^>]*>.*?</a>)', re.DOTALL)
    building_materials_link = """
                                        <a href="building-materials.html"
                                            class="nav-item flex items-center px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-orange-700 rounded-lg transition-all duration-200">
                                            <i class="fas fa-hard-hat text-orange-500 mr-3 w-4"></i>
                                            <div>
                                                <div class="font-medium" data-key="nav.buildingMaterials">Building Materials</div>
                                                <div class="text-xs text-gray-500" data-key="nav.buildingMaterialsDesc">Construction Supplies</div>
                                            </div>
                                        </a>"""
    
    if 'building-materials.html' not in content and 'spices.html' in content:
        content = spices_pattern.sub(r'\1' + building_materials_link, content)
        print(f"Added Building Materials link to {filename}")

    # 2. Update Business Hours (index.html and contact.html)
    # Pattern for Business Hours in index.html (footer/contact section) and contact.html
    # We look for "Sunday - Thursday" or similar patterns and replace the whole block if possible, 
    # or finding the specific lines.
    
    # New Hours text
    new_hours = """Sunday - Friday: 9:00 AM - 6:00 PM<br>
                                                Saturday: 9:00 AM - 2:00 PM"""
    
    # Simple replacement for specific known strings
    # "Monday - Friday" isn't in current, it's Sunday - Thursday.
    # index.html has a structure with divs. contact.html uses <br>.
    
    if filename == 'index.html':
        # Remove wrongly inserted Business Hours block (if I can identify it uniquely)
        # It was inserted around line 359: <div class="bg-gray-50 p-6 rounded-lg">...Business Hours...</div>
        # But there's another one at the bottom.
        # The wrongly inserted one is inside the Intro section. 
        # I'll search for the one near "ISO 9001" or before "Main Title".
        
        # Regex to remove the specific wrongly inserted block
        wrong_block = re.search(r'(<!-- Premium Badge -->.*?)(<!-- Business Hours -->.*?</div>\s*</div>)(.*?<!-- Main Title -->)', content, re.DOTALL)
        if wrong_block:
            # We want to remove group 2
            content = content.replace(wrong_block.group(2), "")
            print("Removed wrongly inserted Business Hours from index.html")
            
        # Update the correct Business Hours (Bottom)
        # It looks like:
        # <span>Sunday - Thursday:</span>
        # <span>8:00 AM - 6:00 PM</span>
        # ...
        # <span>Saturday:</span>
        # <span>Closed</span>
        
        # Regex for the block
        hours_block_pattern = re.compile(r'(<h4[^>]*>Business Hours</h4>\s*<div[^>]*>\s*)(<div class="flex justify-between">.*?</div>\s*</div>)', re.DOTALL)
        
        new_hours_html = """<div class="flex justify-between">
                                        <span>Monday - Friday:</span>
                                        <span>9:00 AM - 6:00 PM</span>
                                    </div>
                                    <div class="flex justify-between">
                                        <span>Saturday:</span>
                                        <span>9:00 AM - 2:00 PM</span>
                                    </div>"""
                                    
        content = hours_block_pattern.sub(r'\1' + new_hours_html + '\n                                ', content)
        print("Updated Business Hours in index.html")

    if filename == 'contact.html':
        # Update Business Hours
        # Content: Sunday - Thursday: 8:00 AM - 6:00 PM<br>\nFriday: 8:00 AM - 12:00 PM<br>\nSaturday: Closed<br>
        old_hours_pattern = re.compile(r'Sunday - Thursday:.*?Closed<br>', re.DOTALL)
        new_hours_bbr = "Monday - Friday: 9:00 AM - 6:00 PM<br>\n                                                Saturday: 9:00 AM - 2:00 PM<br>"
        content = old_hours_pattern.sub(new_hours_bbr, content)
        print("Updated Business Hours in contact.html")
        
        # Fix "We're here to help 24/7." single line
        # It matches "We're\s+here to help 24/7."
        content = re.sub(r"We're\s*\n\s*here to help 24/7\.", "We're here to help 24/7.", content)
        print("Fixed 'We're here to help 24/7' in contact.html")

    if filename == 'about.html':
        # Fix "About M.H.K..." single line
        # Code: <h1 ...>About\n                        M.H.K Trading\n                        & Ship Chandlers</h1>
        title_pattern = re.compile(r'(<h1[^>]*>)\s*About\s+M\.H\.K Trading\s+&\s+Ship Chandlers\s*(</h1>)', re.DOTALL)
        content = title_pattern.sub(r'\1About M.H.K Trading & Ship Chandlers\2', content)
        print("Fixed Title in about.html")
        
    # 3. Remove Overlays
    # Remove bg-black/30, bg-black/60, bg-gradient-to-t (unless needed for text readability, but user said remove ALL)
    # User said "remove all overlay from the cards and hero sections"
    
    # Hero overlay in index.html (already removed in previous step, but check)
    if 'bg-black/30' in content:
        content = content.replace('bg-black/30', '')
        print(f"Removed bg-black/30 from {filename}")
        
    # Card overlays (bg-gradient-to-t)
    if 'bg-gradient-to-t' in content:
        content = content.replace('bg-gradient-to-t', '')
        print(f"Removed bg-gradient-to-t from {filename}")
        
    # Also "from-black/60" etc which are part of gradients usually
    # content = re.sub(r'\bfrom-black/\d+\b', '', content) # Safe? Maybe leave it, gradient removal handles it.

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Saved changes to {filename}")

# Run for all html files
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        update_file(filename)
