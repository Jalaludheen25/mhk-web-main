
import os
import re

directory = "/Users/jalaludheenok/Desktop/mhk-web-main"
exclude_files = ["index.html"]

def update_header(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    
    # 1. Header Container Class
    content = content.replace(
        'class="backdrop-blur-md shadow-lg border-b-4 border-white"',
        'class="bg-white shadow-lg border-b border-gray-200"'
    )
    
    # 2. Header Inline Style (Remove)
    content = content.replace(
        ' style="background-color: rgba(0, 77, 79, 0.95);"',
        ''
    )
    
    # 3. Mobile Menu Button
    content = content.replace(
        'button class="md:hidden text-white p-2"',
        'button class="md:hidden text-gray-800 p-2"'
    )
    
    # 4. Nav Items (Inactive) - General Text & Hover
    content = content.replace(
        'text-white hover:text-golden-300',
        'text-gray-700 hover:text-primary-600'
    )
    # Border thickness and hover
    content = content.replace(
        'border-b-3 border-transparent',
        'border-b-2 border-transparent hover:border-primary-100'
    )
    
    # 5. Nav Items (Active)
    content = content.replace(
        'text-white font-semibold',
        'text-primary-700 font-semibold'
    )
    content = content.replace(
        'border-b-3 border-golden-400',
        'border-b-2 border-primary-600'
    )
    
    # 6. CTA Button
    # Pattern matching for CTA class string which is long
    # We'll use replace for the exact string from index.html (before edit)
    # But files might have slight variations (newlines). Let's try flexible replacement or just specific parts.
    
    # Part 1: Colors
    content = content.replace(
        'bg-white text-primary-600',
        'bg-primary-600 text-white'
    )
    # Part 2: Border and Hover
    content = content.replace(
        'border-2 border-golden-400 hover:bg-golden-50',
        'hover:bg-primary-700'
    )
    
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Updated {file_path}")

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html") and filename not in exclude_files:
        update_header(os.path.join(directory, filename))
        count += 1

print(f"Processed {count} files.")
