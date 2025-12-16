# MHK Website Deployment Guide

## Overview
This is a professional, multi-page website for M.H.K Trading & Ship Chandlers LLC, converted from React/TypeScript to plain HTML, CSS, and JavaScript with Tailwind CSS. The website features a modern, responsive design with enhanced animations, professional content, and comprehensive business information.

## Files Structure
```
/
├── index.html              # Homepage with enhanced hero section
├── about.html              # Company information and history
├── products.html           # Product catalog with filtering
├── services.html           # Service offerings and guarantees
├── contact.html            # Contact forms and information
├── ship-chandling.html     # Ship chandling services detail page
├── seafood.html            # Seafood products detail page
├── meat-poultry.html       # Meat & poultry products detail page
├── logistics.html          # Logistics & supply chain services page
├── quality-assurance.html  # Quality assurance & certification page
├── consulting.html         # Consulting services page
├── styles.css              # Enhanced professional CSS
├── script.js               # JavaScript functionality
├── sw.js                   # Service worker (optional)
├── .htaccess               # Apache configuration
├── DEPLOYMENT.md           # This deployment guide
├── README.md               # Project documentation
└── public/                 # Assets folder
    ├── images/             # Images and logos
    │   └── logo/           # Company logo files
    ├── videos/             # Background videos (6 files)
    └── locales/            # Translation files (legacy - not needed)
```

## Deployment Steps for Bluehost cPanel

### 1. Prepare Files
- Download all files from this project
- Ensure you have the `public` folder with images and videos

### 2. Upload to cPanel
1. Login to your Bluehost cPanel
2. Open "File Manager"
3. Navigate to `public_html` directory
4. Upload all files:
   - `index.html`
   - `styles.css`
   - `script.js`
   - `sw.js`
   - `.htaccess`
   - `public/` folder (with all contents)

### 3. Set File Permissions
- Files: 644
- Folders: 755
- `.htaccess`: 644

### 4. Test the Website
- Visit your domain
- Check all sections work properly
- Test language switching (EN/AR)
- Test contact form
- Verify mobile responsiveness

## Features Included

### ✅ Enhanced Professional Features

#### **Multi-Page Structure**
- **Homepage** - Enhanced hero section with statistics and trust indicators
- **About Page** - Company history, mission, vision, values, and timeline
- **Products Page** - Comprehensive product catalog with filtering system
- **Services Page** - Detailed service offerings with process flow
- **Contact Page** - Advanced contact forms with FAQ section

#### **Product Detail Pages**
- **Ship Chandling** - Complete vessel provisioning services with categories
- **Seafood** - Premium seafood products with quality standards
- **Meat & Poultry** - Halal certified meat products with certification process

#### **Service Detail Pages**
- **Logistics** - Supply chain management with technology platform
- **Quality Assurance** - ISO certification and compliance management
- **Consulting** - Technical advisory and project management services

#### **Professional Design Elements**
- **Enhanced Typography** - Google Fonts (Inter + Poppins) for professional look
- **Advanced Animations** - AOS library for smooth scroll animations
- **Glass Morphism Effects** - Modern backdrop blur and transparency effects
- **Professional Color Scheme** - Primary blue and accent orange with proper gradients
- **Responsive Grid Layouts** - Mobile-first design with advanced CSS Grid

#### **Business Features**
- **Multi-language support** (English/Arabic) with localStorage
- **Video background rotation** with professional overlay effects
- **Interactive navigation** with dropdown menus and hover effects
- **Product filtering system** on products page
- **Advanced contact forms** with validation and multiple contact methods
- **FAQ sections** with collapsible answers
- **Service process visualization** with step-by-step flow
- **Company statistics** and performance metrics
- **Quality certifications** display
- **Timeline of company milestones**

#### **Technical Enhancements**
- **Performance optimized** with lazy loading and efficient animations
- **SEO optimized** with proper meta tags and structured data
- **Accessibility compliant** with ARIA labels and keyboard navigation
- **Cross-browser compatible** with fallbacks for older browsers

### ✅ Performance Optimizations
- **CDN-based Tailwind CSS** (no build process needed)
- **Font Awesome icons** from CDN
- **Service worker** for caching
- **Compressed assets** via .htaccess
- **Proper cache headers**

### ✅ SEO & Accessibility
- **Semantic HTML structure**
- **Meta tags** for SEO
- **Alt text** for images
- **Proper heading hierarchy**
- **RTL support** for Arabic

## Configuration

### Language Settings
The website automatically detects and saves language preference in localStorage. Default is English.

### Contact Form
Currently shows success message after 2 seconds. To connect to a real backend:

1. Replace the setTimeout in `script.js` with actual API call
2. Update the form action in `index.html` if needed
3. Add server-side form processing

### Video Background
Videos are loaded from `public/videos/` folder. Make sure all video files are uploaded:
- `hero-bg.mp4`
- `hero-bg-1.mp4` through `hero-bg-5.mp4`

## Troubleshooting

### Common Issues

1. **Nothing shows after upload**
   - Check file permissions (644 for files, 755 for folders)
   - Ensure `index.html` is in the root `public_html` directory
   - Check browser console for JavaScript errors

2. **Images not loading**
   - Verify `public/images/` folder is uploaded
   - Check image paths in HTML
   - Ensure proper file permissions

3. **Videos not playing**
   - Upload all video files to `public/videos/`
   - Check video file formats (MP4 recommended)
   - Some browsers block autoplay - this is normal

4. **Styles not working**
   - Ensure Tailwind CSS CDN is accessible
   - Check if `styles.css` is uploaded
   - Verify internet connection for CDN resources

### Browser Compatibility
- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+
- ✅ Mobile browsers

## Maintenance

### Adding New Content
1. Edit `index.html` for structure changes
2. Update `translations` object in `script.js` for new text
3. Add new images to `public/images/`

### Performance Monitoring
- Use browser DevTools to check loading times
- Monitor Core Web Vitals
- Test on different devices and connections

## Support
For technical issues with deployment, contact your hosting provider's support team.

## Backup
Always keep a backup of your files before making changes. Use cPanel's backup feature or download files regularly.