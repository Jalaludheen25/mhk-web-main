
import os
import re

def update_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modified = False

    # 1. Remove Building Materials Navigation Link (from all files)
    # The block we added previously.
    # We need to be careful to match it exactly.
    # It contains "building-materials.html" and "nav.buildingMaterials".
    
    # Regex to match the specific link structure we added
    # Note: It might have different indentation in different files if auto-formatter touched it,
    # but I inserted it with specific whitespace.
    
    # Pattern covers the <a> tag until </a>
    bm_link_pattern = re.compile(r'\s*<a href="building-materials\.html"[^>]*class="[^"]*flex items-center[^"]*"[^>]*>.*?</a>', re.DOTALL)
    
    if bm_link_pattern.search(content):
        content = bm_link_pattern.sub('', content)
        modified = True
        print(f"Removed Building Materials nav link from {filename}")

    # 2. Index Page Specifics
    if filename == 'index.html':
        # A. Remove specific cards
        # 1. "500+ Vessels" card
        # Structure: <div class="text-center group p-4 ..."> ... 500+ Vessels ... </div>
        # I'll rely on the text content to identify the div block.
        # Since it's nested, regex is tricky. But the indentation helps.
        
        # Regex for "500+ Vessels" card
        card1_pattern = re.compile(r'\s*<div class="text-center group p-4.*?500\+ Vessels.*?</div>\s*</div>', re.DOTALL)
        if card1_pattern.search(content):
            content = card1_pattern.sub('', content)
            modified = True
            print("Removed '500+ Vessels' card from index.html")
            
        # 2. "24/7 Support" card
        card2_pattern = re.compile(r'\s*<div class="text-center group p-4.*?24/7 Support.*?</div>\s*</div>', re.DOTALL)
        if card2_pattern.search(content):
            content = card2_pattern.sub('', content)
            modified = True
            print("Removed '24/7 Support' card from index.html")
            
        # B. Reduce gap between Hero and Section
        # Find: id="about-intro" class="py-20
        # Replace with: id="about-intro" class="pt-10 pb-20
        if 'id="about-intro"' in content and 'class="py-20' in content:
            content = content.replace('class="py-20', 'class="pt-10 pb-20')
            modified = True
            print("Reduced top padding in index.html about-intro section")

    # 3. Products Page Specifics
    if filename == 'products.html':
        # Add Building Materials Product Card
        # We need to add it to the grid. 
        # Ideally after "Ship Chandling" card.
        # Find the Ship Chandling card closing tag </a>
        
        # The Ship Chandling card ends with </a>
        # We can look for the comment <!-- Ship Chandling (De-emphasized) --> ... </a>
        
        sc_card_pattern = re.compile(r'(<!-- Ship Chandling \(De-emphasized\) -->.*?</a>)', re.DOTALL)
        
        bm_card = """
                    <!-- Building Materials -->
                    <a href="building-materials.html" class="block">
                        <div class="product-card bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-all duration-300 group cursor-pointer"
                            data-category="industrial" data-aos="fade-up" data-aos-delay="450">
                            <div class="relative overflow-hidden h-56">
                                <img src="public/images/products/construction-materials.png" alt="Building Materials"
                                    class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                            </div>
                            <div class="p-6">
                                <h3 class="font-display text-xl font-bold text-gray-900 mb-3">Building Materials</h3>
                                <p class="text-gray-600 mb-4 leading-relaxed">
                                    Premium construction materials including steel, cement, and specialized structural components.
                                </p>
                                <span
                                    class="inline-flex items-center text-primary-600 hover:text-primary-700 font-medium">
                                    View Catalog <i class="fas fa-arrow-right ml-2"></i>
                                </span>
                            </div>
                        </div>
                    </a>"""
        
        # Check if we already have this card to avoid duplication
        if 'alt="Building Materials"' not in content:
            if sc_card_pattern.search(content):
                content = sc_card_pattern.sub(r'\1' + bm_card, content)
                modified = True
                print("Added Building Materials card to products.html")
            else:
                print("WARNING: Could not find Ship Chandling card in products.html to append after")

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Saved {filename}")

# Run for all html files
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        update_file(filename)
