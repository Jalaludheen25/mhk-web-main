# MHK Trading & Ship Chandlers LLC - Complete Project Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Features](#features)
5. [Architecture](#architecture)
6. [File Descriptions](#file-descriptions)
7. [Functionality Details](#functionality-details)
8. [Deployment](#deployment)
9. [Configuration](#configuration)
10. [Maintenance & Updates](#maintenance--updates)

---

## Project Overview

**Project Name:** MHK Trading & Ship Chandlers LLC Website  
**Type:** Multi-page Static Website  
**Industry:** Maritime Supply, Ship Chandling, Food Trading, Industrial Solutions  
**Location:** United Arab Emirates  
**Established:** 2014  
**Certification:** ISO 9001:2015

### Purpose
Professional corporate website showcasing MHK Trading & Ship Chandlers LLC's comprehensive range of products and services including:
- Ship chandling and maritime supplies
- Premium food products (seafood, meat, grains, spices)
- Building materials and scaffolding
- Oil & gas supplies
- Logistics and consulting services

### Key Objectives
- Present company information and credentials
- Showcase product catalog with detailed categories
- Provide bilingual support (English/Arabic)
- Enable customer inquiries through contact forms
- Demonstrate quality certifications and standards
- Establish professional online presence

---

## Technology Stack

### Frontend Technologies
- **HTML5** - Semantic markup structure
- **CSS3** - Custom styling with modern features
- **JavaScript (ES6+)** - Vanilla JavaScript for interactivity
- **Tailwind CSS** (via CDN) - Utility-first CSS framework
- **Font Awesome 6.4.0** - Icon library
- **AOS (Animate On Scroll)** - Scroll animation library
- **Google Fonts** - Inter, Poppins, Cairo, Noto Sans Arabic

### Build & Deployment
- **No Build Process** - Pure static files
- **Service Worker** - PWA capabilities and caching
- **Apache .htaccess** - Server configuration

### Browser Support
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+
- Mobile browsers (iOS Safari, Chrome Mobile)

---

## Project Structure

```
mhk-web-main/
│
├── .git/                          # Git version control
├── .github/                       # GitHub configuration
├── .vscode/                       # VS Code settings
│
├── public/                        # Static assets
│   ├── images/
│   │   ├── logo/
│   │   │   └── Logo.png          # Company logo
│   │   └── products/             # Product images (50+ files)
│   │       ├── 1.jpg
│   │       ├── about-hero.jpg
│   │       ├── building.jpg
│   │       ├── fresh-fruits.png
│   │       ├── meat.jpg
│   │       ├── seafood.jpg
│   │       └── ... (more images)
│   │
│   ├── videos/                   # Background videos
│   │   ├── hero-bg.mp4
│   │   ├── hero-bg-4.mp4
│   │   ├── Shipping-video-01.mp4
│   │   ├── products.mp4
│   │   └── rice-video.mp4
│   │
│   ├── locales/                  # Translation files (legacy)
│   │   ├── en/
│   │   │   └── translation.json
│   │   └── ar/
│   │       └── translation.json
│   │
│   └── vite.svg                  # Vite icon (legacy)
│
├── HTML Pages (18 files)
│   ├── index.html                # Homepage
│   ├── about.html                # Company information
│   ├── products.html             # Product catalog
│   ├── services.html             # Service offerings
│   ├── contact.html              # Contact page
│   ├── ship-chandling.html       # Ship chandling details
│   ├── seafood.html              # Seafood products
│   ├── meat-poultry.html         # Meat & poultry
│   ├── fresh-provisions.html     # Fresh provisions
│   ├── grains-pulses.html        # Grains & pulses
│   ├── spices.html               # Spices & seasonings
│   ├── processed-foods.html      # Processed foods
│   ├── building-materials.html   # Building materials
│   ├── scaffolding.html          # Scaffolding materials
│   ├── oil-gas.html              # Oil & gas supplies
│   ├── logistics.html            # Logistics services
│   ├── quality-assurance.html    # Quality assurance
│   ├── consulting.html           # Consulting services
│   ├── leadership.html           # Leadership team
│   └── certifications.html       # Certifications
│
├── Core Files
│   ├── script.js                 # Main JavaScript functionality
│   ├── styles.css                # Custom CSS styles
│   ├── sw.js                     # Service worker
│   ├── .htaccess                 # Apache configuration
│   └── .gitignore                # Git ignore rules
│
└── Documentation
    ├── README.md                 # Project readme
    └── DEPLOYMENT.md             # Deployment guide
```

---

## Features

### 1. Responsive Design
- **Mobile-first approach** with breakpoints for all devices
- **Adaptive navigation** - Desktop dropdown menus, mobile hamburger menu
- **Flexible layouts** using CSS Grid and Flexbox
- **Touch-optimized** interactions for mobile devices

### 2. Bilingual Support (English/Arabic)
- **Language toggle** button in header
- **RTL (Right-to-Left)** support for Arabic
- **LocalStorage persistence** - Remembers user's language preference
- **Dynamic content translation** using JavaScript
- **Arabic-specific fonts** - Cairo, Noto Sans Arabic
- **Bidirectional layouts** with proper text alignment

### 3. Video & Image Backgrounds
- **Rotating media carousel** on homepage hero section
- **Smooth transitions** between videos and images
- **Autoplay with fallback** handling
- **Optimized loading** with preload strategies
- **Multiple video formats** for compatibility

### 4. Navigation System
- **Fixed header** with scroll effects
- **Multi-level dropdown menus** for products and services
- **Active page indicators** with visual feedback
- **Smooth scroll** to anchor links
- **Mobile-responsive** hamburger menu

### 5. Animation & Effects
- **AOS (Animate On Scroll)** library integration
- **Custom CSS animations** - fade-in, slide-in, scale effects
- **Hover effects** on cards and buttons
- **Glass morphism** design elements
- **Gradient backgrounds** and overlays
- **Shimmer effects** on hero elements

### 6. Contact Forms
- **Client-side validation** for required fields
- **Email format validation** using regex
- **Phone number validation**
- **Success/error messaging** with visual feedback
- **Form reset** after successful submission
- **Loading states** during submission

### 7. Product Showcase
- **Category-based organization** with filtering
- **Product cards** with hover effects
- **High-quality images** for all products
- **Detailed product pages** for major categories
- **Rice product carousel** with navigation controls

### 8. Performance Optimization
- **Service Worker** for offline caching
- **CDN-based libraries** for faster loading
- **Image optimization** recommendations
- **Lazy loading** for images and videos
- **Compressed assets** via .htaccess
- **Browser caching** headers

### 9. SEO & Accessibility
- **Semantic HTML5** structure
- **Meta tags** for search engines
- **Open Graph** tags for social sharing
- **Alt text** for all images
- **ARIA labels** for screen readers
- **Keyboard navigation** support
- **Focus indicators** for accessibility
- **Proper heading hierarchy** (h1-h6)

### 10. Security Features
- **X-Content-Type-Options** header
- **X-Frame-Options** header (clickjacking protection)
- **XSS Protection** header
- **Sensitive file protection** in .htaccess
- **HTTPS redirect** option (commented out)

---

## Architecture

### Design Pattern
**Multi-Page Application (MPA)** with shared components and consistent styling across all pages.

### Component Structure
```
Header (Fixed)
├── Logo
├── Desktop Navigation
│   ├── Home
│   ├── About (Dropdown)
│   ├── Products (Dropdown)
│   ├── Services
│   └── Contact
├── Language Toggle
└── Mobile Menu Button

Main Content (Variable per page)
├── Hero Section
├── Content Sections
└── Call-to-Action

Footer
├── Quick Links
├── Contact Information
└── Copyright
```

### Data Flow
```
User Interaction
    ↓
JavaScript Event Handlers
    ↓
DOM Manipulation / LocalStorage
    ↓
Visual Feedback / State Update
```

### Translation System
```
translations object (script.js)
    ↓
setLanguage() function
    ↓
Update DOM elements with [data-key] attributes
    ↓
Apply RTL/LTR direction
    ↓
Save preference to LocalStorage
```

---

## File Descriptions

### HTML Files

#### index.html (Homepage)
- **Purpose:** Main landing page
- **Key Sections:**
  - Hero section with video/image rotation
  - Company introduction
  - Premium food products showcase
  - Rice product carousel
  - Quality certifications
  - Key statistics
  - Call-to-action sections
- **Special Features:**
  - Dynamic video background rotation
  - Animated statistics counters
  - Product carousel with navigation
  - AOS scroll animations

#### about.html
- Company history and timeline
- Mission, vision, and values
- Leadership team information
- Company milestones
- Certifications and accreditations

#### products.html
- Complete product catalog
- Category filtering system
- Product cards with images
- Links to detailed product pages

#### Product Detail Pages
- **ship-chandling.html** - Vessel provisioning services
- **seafood.html** - Fresh and frozen seafood
- **meat-poultry.html** - Halal meat products
- **fresh-provisions.html** - Fruits, vegetables, dairy
- **grains-pulses.html** - Rice, pulses, cereals
- **spices.html** - Spices and seasonings
- **processed-foods.html** - Canned and packaged foods
- **building-materials.html** - Construction supplies
- **scaffolding.html** - Scaffolding materials
- **oil-gas.html** - Oil & gas supplies

#### Service Pages
- **logistics.html** - Supply chain management
- **quality-assurance.html** - ISO certification and QA
- **consulting.html** - Technical advisory services

#### Other Pages
- **contact.html** - Contact forms and information
- **leadership.html** - Executive team profiles
- **certifications.html** - Quality certifications

### JavaScript Files

#### script.js (Main Application Logic)
**Size:** ~800 lines  
**Key Components:**

1. **Translation System**
   - `translations` object with EN/AR content
   - `setLanguage()` - Language switching function
   - `initializeLanguage()` - Setup language toggle
   - LocalStorage integration

2. **Navigation**
   - `initializeNavigation()` - Mobile menu toggle
   - Dropdown menu handlers
   - Active page indicators
   - Smooth scrolling

3. **Header Effects**
   - `initializeHeader()` - Scroll-based shadow effects
   - Sticky header behavior

4. **Video/Image Rotation**
   - `initializeVideoRotation()` - Media carousel
   - `playCurrentItem()` - Play video or show image
   - `playNextItem()` - Advance to next item
   - Playlist management with timing

5. **Contact Form**
   - `initializeContactForm()` - Form submission handler
   - `validateForm()` - Client-side validation
   - `showMessage()` - Success/error messaging

6. **Animations**
   - AOS initialization
   - Intersection Observer for scroll animations
   - Custom animation triggers

7. **Utilities**
   - `debounce()` - Performance optimization
   - Error handling
   - Service worker registration

#### sw.js (Service Worker)
**Purpose:** PWA capabilities and offline caching  
**Features:**
- Cache static assets
- Offline fallback
- Cache versioning
- Automatic cache cleanup

### CSS Files

#### styles.css (Custom Styles)
**Size:** ~1000 lines  
**Key Sections:**

1. **Base Styles**
   - CSS reset and normalization
   - Typography settings
   - Smooth scrolling

2. **RTL Support**
   - Bidirectional text support
   - Flexbox direction adjustments
   - Text alignment for Arabic
   - Font family switching

3. **Navigation**
   - Header styling
   - Dropdown menus
   - Mobile menu
   - Active states

4. **Animations**
   - @keyframes definitions
   - Fade, slide, scale effects
   - Hover transitions
   - Loading spinners

5. **Components**
   - Cards and hover effects
   - Buttons with gradients
   - Form inputs
   - Glass morphism effects

6. **Responsive Design**
   - Media queries
   - Mobile optimizations
   - Print styles

7. **Accessibility**
   - Focus indicators
   - High contrast mode
   - Reduced motion support
   - Skip links

### Configuration Files

#### .htaccess (Apache Configuration)
- **Compression:** Gzip compression for text files
- **Caching:** Browser cache headers for assets
- **Security:** XSS protection, clickjacking prevention
- **Error Pages:** Custom 404/500 handlers
- **File Protection:** Deny access to sensitive files

#### .gitignore
- Node modules (if any)
- Log files
- Editor-specific files
- OS-specific files (.DS_Store)

---

## Functionality Details

### Language Switching

**Implementation:**
```javascript
// Translation data structure
const translations = {
    en: { "key": "English text" },
    ar: { "key": "Arabic text" }
};

// HTML markup
<span data-key="company.name">M.H.K Trading</span>

// Switching logic
function setLanguage(lang) {
    // Update all elements with data-key
    document.querySelectorAll('[data-key]').forEach(element => {
        const key = element.getAttribute('data-key');
        element.textContent = translations[lang][key];
    });
    
    // Set direction
    document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
    
    // Save preference
    localStorage.setItem('language', lang);
}
```

**Features:**
- Instant switching without page reload
- Persistent preference across sessions
- Dynamic content updates
- RTL layout transformation
- Font family changes

### Video/Image Rotation

**Playlist Structure:**
```javascript
const playlist = [
    { type: 'image', src: 'path/to/image.jpg', duration: 5000 },
    { type: 'video', src: 'path/to/video.mp4' },
    // ...
];
```

**Rotation Logic:**
1. Load first item from playlist
2. If image: Display for specified duration
3. If video: Play until ended
4. Fade out current item
5. Fade in next item
6. Loop back to start

**Error Handling:**
- Video playback failures skip to next item
- Image load errors handled gracefully
- Autoplay restrictions managed

### Form Validation

**Validation Rules:**
- **Required fields:** Name, email, message
- **Email format:** Regex pattern `/^[^\s@]+@[^\s@]+\.[^\s@]+$/`
- **Phone format:** Optional validation
- **Real-time feedback:** Error messages on blur

**Submission Flow:**
1. Prevent default form submission
2. Validate all fields
3. Show loading state
4. Simulate API call (2-second timeout)
5. Display success/error message
6. Reset form on success

### Navigation System

**Desktop Navigation:**
- Hover-activated dropdown menus
- Smooth transitions (0.3s)
- Active page highlighting
- Border bottom indicators

**Mobile Navigation:**
- Hamburger menu toggle
- Slide-in animation
- Full-screen overlay
- Touch-optimized spacing

**Scroll Behavior:**
- Fixed header with backdrop blur
- Shadow intensity increases on scroll
- Smooth scroll to anchor links
- Header height compensation

### Animation System

**AOS Integration:**
```javascript
AOS.init({
    duration: 800,
    once: true,
    offset: 100
});
```

**Custom Animations:**
- `fadeInUp` - Fade in from bottom
- `slideInRight` - Slide from right
- `slideInLeft` - Slide from left
- `scaleIn` - Scale up from center

**Intersection Observer:**
- Triggers animations on scroll
- Observes card and section elements
- Adds animation classes dynamically

---

## Deployment

### Hosting Requirements
- **Web Server:** Apache or Nginx
- **PHP:** Not required (static site)
- **Database:** Not required
- **SSL Certificate:** Recommended for HTTPS

### Deployment Steps

#### 1. Bluehost cPanel Deployment
```bash
# 1. Login to cPanel
# 2. Open File Manager
# 3. Navigate to public_html
# 4. Upload all files:
#    - HTML files
#    - script.js
#    - styles.css
#    - sw.js
#    - .htaccess
#    - public/ folder (complete)
# 5. Set permissions:
#    - Files: 644
#    - Folders: 755
```

#### 2. GitHub Pages Deployment
```bash
# 1. Push to GitHub repository
git add .
git commit -m "Deploy website"
git push origin main

# 2. Enable GitHub Pages in repository settings
# 3. Select main branch
# 4. Site will be available at: https://username.github.io/repo-name
```

#### 3. Netlify Deployment
```bash
# 1. Connect GitHub repository to Netlify
# 2. Build settings:
#    - Build command: (none)
#    - Publish directory: /
# 3. Deploy
```

#### 4. Vercel Deployment
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Follow prompts
```

### Post-Deployment Checklist
- [ ] Test all pages load correctly
- [ ] Verify images and videos display
- [ ] Test language switching
- [ ] Check mobile responsiveness
- [ ] Test contact form
- [ ] Verify navigation links
- [ ] Test on multiple browsers
- [ ] Check SSL certificate
- [ ] Test page load speed
- [ ] Verify SEO meta tags

---

## Configuration

### Customization Guide

#### 1. Update Company Information
**File:** `script.js`
```javascript
// Edit translations object
const translations = {
    en: {
        "company.name": "Your Company Name",
        "company.tagline": "Your Tagline",
        // ...
    }
};
```

#### 2. Change Colors
**File:** `index.html` (Tailwind config)
```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: {
                    500: '#YOUR_COLOR',
                    // ...
                }
            }
        }
    }
}
```

#### 3. Update Logo
**File:** Replace `public/images/logo/Logo.png`
**Update in:** All HTML files
```html
<img src="public/images/logo/Logo.png" alt="Company Logo">
```

#### 4. Modify Navigation
**File:** All HTML files (header section)
```html
<nav class="hidden md:flex items-center space-x-1">
    <!-- Add/remove navigation items -->
</nav>
```

#### 5. Add New Products
1. Create new HTML file (e.g., `new-product.html`)
2. Copy structure from existing product page
3. Update content and images
4. Add link in `products.html`
5. Add dropdown item in navigation

#### 6. Configure Contact Form
**File:** `script.js`
```javascript
// Replace setTimeout with actual API call
fetch('YOUR_API_ENDPOINT', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: { 'Content-Type': 'application/json' }
})
.then(response => response.json())
.then(data => {
    showMessage('success', translations[currentLanguage]['form.success']);
})
.catch(error => {
    showMessage('error', translations[currentLanguage]['form.error']);
});
```

#### 7. Update Videos
**File:** `script.js`
```javascript
const playlist = [
    { type: 'video', src: 'public/videos/your-video.mp4' },
    // Add more items
];
```

### Environment Variables
Not applicable (static site with no build process)

### API Integration
Currently simulated. To integrate real backend:

1. **Contact Form API:**
```javascript
// In script.js, replace setTimeout with:
const response = await fetch('/api/contact', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formData)
});
```

2. **Product Data API:**
```javascript
// Fetch products dynamically
const products = await fetch('/api/products').then(r => r.json());
```

---

## Maintenance & Updates

### Regular Maintenance Tasks

#### Weekly
- [ ] Check website uptime
- [ ] Monitor form submissions
- [ ] Review error logs
- [ ] Test critical user paths

#### Monthly
- [ ] Update product images
- [ ] Review and update content
- [ ] Check for broken links
- [ ] Analyze performance metrics
- [ ] Update certifications if changed

#### Quarterly
- [ ] Security audit
- [ ] Performance optimization
- [ ] Browser compatibility testing
- [ ] Mobile responsiveness check
- [ ] SEO audit

#### Annually
- [ ] Renew SSL certificate
- [ ] Update copyright year
- [ ] Review and update company information
- [ ] Major content refresh
- [ ] Technology stack review

### Content Updates

#### Adding New Products
1. Prepare product images (optimize for web)
2. Upload to `public/images/products/`
3. Create product page or add to existing
4. Update navigation if needed
5. Add to product catalog page
6. Update translations

#### Updating Text Content
1. Edit HTML files directly
2. Update `translations` object in `script.js`
3. Test both English and Arabic versions
4. Verify RTL layout for Arabic

#### Adding New Pages
1. Copy existing page as template
2. Update content and metadata
3. Add navigation link
4. Update sitemap (if using)
5. Test all links

### Performance Optimization

#### Image Optimization
```bash
# Use tools like:
- TinyPNG (https://tinypng.com/)
- ImageOptim (Mac)
- Squoosh (https://squoosh.app/)

# Target sizes:
- Hero images: < 500KB
- Product images: < 200KB
- Thumbnails: < 50KB
```

#### Video Optimization
```bash
# Use FFmpeg for compression:
ffmpeg -i input.mp4 -vcodec h264 -acodec aac -b:v 1M output.mp4

# Target:
- Resolution: 1920x1080 or lower
- Bitrate: 1-2 Mbps
- Format: MP4 (H.264)
```

#### Code Optimization
- Minify CSS and JavaScript for production
- Remove unused CSS classes
- Optimize font loading
- Implement lazy loading for images

### Troubleshooting

#### Common Issues

**1. Videos Not Playing**
- Check file paths are correct
- Verify video format (MP4 recommended)
- Check browser autoplay policies
- Ensure videos are uploaded to server

**2. Language Switching Not Working**
- Check browser console for errors
- Verify `translations` object has all keys
- Check `data-key` attributes match
- Clear browser cache and localStorage

**3. Images Not Loading**
- Verify file paths (case-sensitive)
- Check file permissions (644)
- Ensure images are uploaded
- Check browser network tab for 404 errors

**4. Mobile Menu Not Opening**
- Check JavaScript console for errors
- Verify `mobileMenuBtn` and `mobileMenu` IDs exist
- Test on actual mobile device
- Check for JavaScript conflicts

**5. Forms Not Submitting**
- Check browser console for validation errors
- Verify form action/method
- Test with simple alert first
- Check network tab for API errors

### Backup Strategy

#### What to Backup
- All HTML files
- `script.js` and `styles.css`
- `public/` folder (images and videos)
- `.htaccess` configuration
- Database (if added later)

#### Backup Methods
1. **Manual Backup:**
   - Download via FTP/cPanel File Manager
   - Store in dated folders
   - Keep at least 3 versions

2. **Automated Backup:**
   - Use cPanel backup feature
   - Schedule weekly backups
   - Store off-site (Google Drive, Dropbox)

3. **Version Control:**
   - Use Git for code versioning
   - Push to GitHub/GitLab regularly
   - Tag releases

### Security Best Practices

1. **Keep Software Updated**
   - Update CDN library versions
   - Monitor for security advisories
   - Update server software

2. **Secure Hosting**
   - Use HTTPS (SSL certificate)
   - Enable firewall
   - Regular security scans

3. **Access Control**
   - Strong passwords
   - Limit FTP/cPanel access
   - Use SSH keys for Git

4. **Monitoring**
   - Set up uptime monitoring
   - Monitor for suspicious activity
   - Review access logs

### Support & Resources

#### Documentation
- Tailwind CSS: https://tailwindcss.com/docs
- Font Awesome: https://fontawesome.com/docs
- AOS Library: https://michalsnik.github.io/aos/
- MDN Web Docs: https://developer.mozilla.org/

#### Tools
- **Testing:** BrowserStack, LambdaTest
- **Performance:** Google PageSpeed Insights, GTmetrix
- **SEO:** Google Search Console, Ahrefs
- **Analytics:** Google Analytics, Plausible

#### Contact Information
- **Developer:** [Your Name/Company]
- **Email:** [Your Email]
- **Support:** [Support Channel]

---

## Appendix

### Browser Compatibility Matrix

| Feature | Chrome | Firefox | Safari | Edge | Mobile |
|---------|--------|---------|--------|------|--------|
| CSS Grid | ✅ 57+ | ✅ 52+ | ✅ 10.1+ | ✅ 16+ | ✅ |
| Flexbox | ✅ 29+ | ✅ 28+ | ✅ 9+ | ✅ 12+ | ✅ |
| Service Worker | ✅ 40+ | ✅ 44+ | ✅ 11.1+ | ✅ 17+ | ✅ |
| Video Autoplay | ⚠️ Muted | ⚠️ Muted | ⚠️ Muted | ⚠️ Muted | ⚠️ |
| LocalStorage | ✅ 4+ | ✅ 3.5+ | ✅ 4+ | ✅ 12+ | ✅ |

### Performance Benchmarks

**Target Metrics:**
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Time to Interactive: < 3.5s
- Cumulative Layout Shift: < 0.1
- First Input Delay: < 100ms

**Current Performance:**
- Homepage size: ~2-3 MB (with videos)
- Load time: 2-4s (depending on connection)
- Lighthouse score: 85-95 (varies by page)

### Accessibility Checklist

- [x] Semantic HTML structure
- [x] Alt text for images
- [x] ARIA labels where needed
- [x] Keyboard navigation support
- [x] Focus indicators
- [x] Color contrast ratios (WCAG AA)
- [x] Responsive text sizing
- [x] Screen reader compatibility
- [ ] Captions for videos (to be added)
- [ ] Transcripts for audio (N/A)

### SEO Checklist

- [x] Unique title tags
- [x] Meta descriptions
- [x] Open Graph tags
- [x] Semantic HTML
- [x] Mobile-friendly
- [x] Fast loading
- [x] HTTPS (recommended)
- [ ] XML sitemap (to be added)
- [ ] robots.txt (to be added)
- [ ] Structured data markup (to be added)

---

## Version History

**Version 2.0** (Current)
- Converted from React to vanilla HTML/CSS/JS
- Added bilingual support (EN/AR)
- Implemented video rotation system
- Enhanced animations and effects
- Added service worker for PWA
- Improved mobile responsiveness

**Version 1.0** (Previous)
- React/TypeScript implementation
- Basic product catalog
- Contact form
- Single language (English)

---

## License & Credits

**Copyright:** © 2024 M.H.K Trading & Ship Chandlers LLC. All rights reserved.

**Third-Party Libraries:**
- Tailwind CSS - MIT License
- Font Awesome - Font Awesome Free License
- AOS - MIT License
- Google Fonts - SIL Open Font License

**Images & Videos:**
- All product images and videos are property of MHK Trading & Ship Chandlers LLC

---

## Conclusion

This documentation provides a comprehensive overview of the MHK Trading & Ship Chandlers LLC website. The project is a modern, professional, multi-page static website built with vanilla web technologies, featuring bilingual support, responsive design, and rich multimedia content.

For questions, updates, or support, please refer to the contact information provided or consult the inline code comments for technical details.

**Last Updated:** December 18, 2024
