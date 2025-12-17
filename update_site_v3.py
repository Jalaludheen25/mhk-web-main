
import os
import re

def update_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modified = False

    # 1. Update Header Color to "Glancy Blue"
    # Target: bg-primary-900 shadow-none border-b-4 border-golden-400
    # Replacement: bg-primary-900/90 backdrop-blur-md shadow-lg border-b-4 border-golden-400
    # Note: Some files might still have 'primary-600' if my previous blanket sed missed them or if they were reverted? 
    # But I sed'ed all *.html in Step 778.
    
    old_header_class = 'bg-primary-900 shadow-none border-b-4 border-golden-400'
    new_header_class = 'bg-primary-900/90 backdrop-blur-md shadow-lg border-b-4 border-golden-400'
    
    if old_header_class in content:
        content = content.replace(old_header_class, new_header_class)
        modified = True
        print(f"Updated header color in {filename}")

    # 2. Remove Hero Text (Index Only)
    if filename == 'index.html':
        # Locate the div containing the hero text
        # <div class="text-center px-4 max-w-5xl" data-aos="fade-up">
        #   ... content ...
        # </div>
        # We want to keep the div but empty its content.
        
        hero_pattern = re.compile(r'(<div class="text-center px-4 max-w-5xl" data-aos="fade-up">)(.*?)(</div>)', re.DOTALL)
        match = hero_pattern.search(content)
        if match:
            # Check if it's not already empty (or just whitespace)
            current_inner = match.group(2)
            if current_inner.strip():
                content = hero_pattern.sub(r'\1\3', content)
                modified = True
                print("Removed hero text in index.html")

    # 3. Move/Add Building Materials Link
    # First, remove existing Building Materials link if present to avoid duplicates
    # Regex for Building Materials link
    
    bm_link_pattern = re.compile(r'\s*<a href="building-materials\.html".*?</a>', re.DOTALL)
    
    # Store the link content if we find it, or define a standard one
    existing_bm_match = bm_link_pattern.search(content)
    
    # Standard block to insert
    bm_link_block = """
                                        <a href="building-materials.html"
                                            class="flex items-center px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-orange-700 rounded-lg transition-all duration-200">
                                            <i class="fas fa-hard-hat text-orange-500 mr-3 w-4"></i>
                                            <div>
                                                <div class="font-medium" data-key="nav.buildingMaterials">Building Materials</div>
                                                <div class="text-xs text-gray-500" data-key="nav.buildingMaterialsDesc">Construction Supplies</div>
                                            </div>
                                        </a>"""

    # Remove existing
    if existing_bm_match:
        content = bm_link_pattern.sub('', content)
        # modified = True # We will mark modified only if we also insert it back differently
        print(f"Removed existing position of Building Materials in {filename}")

    # Now insert after Ship Chandling
    # Target: Ship Chandling link block
    sc_link_pattern = re.compile(r'(<a href="ship-chandling\.html"[^>]*>.*?</a>)', re.DOTALL)
    
    if sc_link_pattern.search(content):
        # Insert after
        content = sc_link_pattern.sub(r'\1' + bm_link_block, content)
        modified = True
        print(f"Inserted Building Materials after Ship Chandling in {filename}")
    else:
        print(f"WARNING: Could not find Ship Chandling link in {filename}")

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Saved {filename}")

# Run for all html files
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        update_file(filename)
