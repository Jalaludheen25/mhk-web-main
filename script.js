// MHK Website JavaScript

// Translations data
const translations = {
    en: {
        "nav.home": "Home",
        "nav.about": "About Us",
        "nav.products": "Products",
        "nav.contact": "Contact",
        "company.name": "M.H.K Trading & Ship Chandlers LLC",
        "company.tagline": "Reliable Ship Chandler Partner Supplying All Ranges of Provisions",
        "company.founded": "Founded in 2014",
        "company.founder": "Founded by Hariharasudan Gnanasekaran",
        "company.location": "United Arab Emirates",
        "company.mission": "Our mission is to provide exceptional service, quality products, and innovative solutions to our customers, while maintaining the highest standards of integrity, professionalism, and environmental responsibility.",
        "contact.phone": "+971 4 299 7911",
        "contact.email": "info@mhkts.ae",
        "contact.address": "P.O.Box: 111133, Deira, Dubai, United Arab Emirates",
        "contact.getQuote": "Get a Quote",
        "contact.contactUs": "Contact Us",
        "contact.sendMessage": "Send Message",
        "categories.shipChandling.name": "Ship Chandling",
        "categories.shipChandling.description": "Reliable ship chandler partner supplying fresh, dry, and frozen provisions to ships",
        "categories.seafood.name": "Seafood",
        "categories.seafood.description": "Leading distributor of high-quality fresh & frozen seafood",
        "categories.meat.name": "Meat",
        "categories.meat.description": "High-quality fresh & frozen mutton, beef & poultry",
        "categories.spices.name": "Spices",
        "categories.spices.description": "Leading distributor of high-quality spices & spice powders",
        "categories.buildingMaterials.name": "Building Materials",
        "categories.buildingMaterials.description": "Custom-made steel rebar, alloy steel, stainless steel, tool steel, mild steel",
        "categories.oilGas.name": "Oil & Gas",
        "categories.oilGas.description": "Gas processing plant projects and EPC contractor assistance",
        "categories.scaffolding.name": "Scaffolding Materials",
        "categories.scaffolding.description": "Certified GI Stainless Steel Tube, Hot Galvanized Scaffold Pipe & Fittings",
        "categories.mep.name": "MEP",
        "categories.mep.description": "Mechanical, Electrical, and Plumbing supplies",
        "categories.mep.description": "Mechanical, Electrical, and Plumbing supplies",
        "nav.freshProvisions": "Fresh Provisions",
        "nav.freshProvisionsDesc": "Fruits, Vegetables & Dairy",
        "nav.grains": "Grains & Spices",
        "nav.grainsDesc": "Rice, Pulses & Herbs",
        "nav.meat": "Meat & Poultry",
        "nav.meatDesc": "Fresh & Frozen",
        "nav.seafood": "Seafood",
        "nav.seafoodDesc": "Fresh & Marine Products",
        "nav.shipChandling": "Ship Chandling",
        "nav.shipChandlingDesc": "Vessel Supplies",
        "nav.logistics": "Logistics & Supply Chain",
        "nav.logisticsDesc": "End-to-end logistics solutions",
        "nav.quality": "Quality Assurance",
        "nav.qualityDesc": "ISO certified processes",
        "nav.consulting": "Consulting Services",
        "nav.consultingDesc": "Expert technical advisory",
        "nav.companyOverview": "Company Overview",
        "nav.companyOverviewDesc": "Our story & mission",
        "nav.leadership": "Leadership Team",
        "nav.leadershipDesc": "Meet our executives",
        "nav.certifications": "Certifications",
        "nav.certificationsDesc": "Quality standards",
        "home.hero.title": "PREMIUM FOOD TRADING & SHIP CHANDLERS",
        "home.hero.subtitle": "Your Trusted Partner in Global Food Trading, Maritime Supply & Industrial Solutions",
        "home.hero.cta": "Explore Solutions",
        "company.tagline": "Global Food Excellence",
        "home.certifications.title": "Quality Certifications",
        "home.certifications.iso": "ISO 9001:2015 Certified",
        "home.certifications.alwaysFresh": "Always Fresh",
        "home.certifications.halal": "100% Halal",
        "home.certifications.premium": "Premium Quality",
        "about.title": "About MHK",
        "about.history": "M H K Trading & Ship Chandlers LLC is a reputable trading company based in the United Arab Emirates, specializing in providing top-quality products and services to the maritime industry, Industrial & Construction Materials, Consumer Goods, Food & Beverages. Since its inception in 2014, our company has been committed to excellence, reliability, and customer satisfaction.",
        "about.growth": "Founded by Hariharasudan Gnanasekaran, our company has grown steadily over the years, establishing itself as a trusted partner for ship owners, operators, and suppliers. With a strong foundation in trading and ship chandling, we have expanded our portfolio to cater to the diverse needs of the maritime, & general trading sector.",
        "about.certifications": "ISO 9001:2015 Quality Management System",
        "form.name": "Name",
        "form.email": "Email",
        "form.phone": "Phone",
        "form.company": "Company",
        "form.category": "Product Category",
        "form.message": "Message",
        "form.selectCategory": "Select a category",
        "form.required": "This field is required",
        "form.invalidEmail": "Please enter a valid email address",
        "form.invalidPhone": "Please enter a valid phone number",
        "form.success": "Thank you! We will contact you soon.",
        "form.error": "Unable to send your message. Please try again or contact us directly.",
        "footer.quickLinks": "Quick Links",
        "footer.contactInfo": "Contact Information",
        "footer.copyright": "© 2024 M.H.K Trading & Ship Chandlers LLC. All rights reserved."
    },
    ar: {
        "nav.home": "الرئيسية",
        "nav.about": "من نحن",
        "nav.products": "المنتجات",
        "nav.contact": "اتصل بنا",
        "company.name": "ام اتش كي للتجارة وتموين السفن ش.ذ.م.م",
        "company.tagline": "شريك موثوق لتموين السفن بجميع أنواع المؤن",
        "company.founded": "تأسست في 2014",
        "company.founder": "تأسست من قبل هاريهاراسودان جناناسيكاران",
        "company.location": "الإمارات العربية المتحدة",
        "company.mission": "مهمتنا هي تقديم خدمة استثنائية ومنتجات عالية الجودة وحلول مبتكرة لعملائنا، مع الحفاظ على أعلى معايير النزاهة والاحترافية والمسؤولية البيئية.",
        "contact.phone": "7911 299 4 971+",
        "contact.email": "info@mhkts.ae",
        "contact.address": "ص.ب: 111133، ديرة، دبي، الإمارات العربية المتحدة",
        "contact.getQuote": "احصل على عرض أسعار",
        "contact.contactUs": "اتصل بنا",
        "contact.sendMessage": "إرسال رسالة",
        "categories.shipChandling.name": "تموين السفن",
        "categories.shipChandling.description": "شريك موثوق لتموين السفن بالمؤن الطازجة والجافة والمجمدة",
        "categories.seafood.name": "المأكولات البحرية",
        "categories.seafood.description": "موزع رائد للمأكولات البحرية الطازجة والمجمدة عالية الجودة",
        "categories.meat.name": "اللحوم",
        "categories.meat.description": "لحوم طازجة ومجمدة عالية الجودة من الضأن والبقر والدواجن",
        "categories.spices.name": "التوابل",
        "categories.spices.description": "موزع رائد للتوابل ومساحيق التوابل عالية الجودة",
        "categories.buildingMaterials.name": "مواد البناء",
        "categories.buildingMaterials.description": "حديد التسليح المخصص، الفولاذ السبائكي، الفولاذ المقاوم للصدأ، فولاذ الأدوات، الفولاذ الطري",
        "categories.oilGas.name": "النفط والغاز",
        "categories.oilGas.description": "مشاريع محطات معالجة الغاز ومساعدة مقاولي EPC",
        "categories.scaffolding.name": "مواد السقالات",
        "categories.scaffolding.description": "أنابيب فولاذية مقاومة للصدأ معتمدة، أنابيب سقالات مجلفنة وتجهيزات",
        "categories.mep.name": "MEP",
        "categories.mep.description": "إمدادات ميكانيكية وكهربائية وسباكة",
        "categories.mep.description": "إمدادات ميكانيكية وكهربائية وسباكة",
        "nav.freshProvisions": "المؤن الطازجة",
        "nav.freshProvisionsDesc": "الفواكه والخضروات ومنتجات الألبان",
        "nav.grains": "الحبوب والبهارات",
        "nav.grainsDesc": "الأرز والبقوليات والأعشاب",
        "nav.meat": "اللحوم والدواجن",
        "nav.meatDesc": "طازجة ومجمدة",
        "nav.seafood": "المأكولات البحرية",
        "nav.seafoodDesc": "منتجات بحرية طازجة",
        "nav.shipChandling": "تموين السفن",
        "nav.shipChandlingDesc": "إمدادات السفن",
        "nav.logistics": "الخدمات اللوجستية",
        "nav.logisticsDesc": "حلول لوجستية شاملة",
        "nav.quality": "ضمان الجودة",
        "nav.qualityDesc": "عمليات معتمدة من ISO",
        "nav.consulting": "خدمات استشارية",
        "nav.consultingDesc": "استشارات فنية متخصصة",
        "nav.companyOverview": "نظرة عامة على الشركة",
        "nav.companyOverviewDesc": "قصتنا ورسالتنا",
        "nav.leadership": "فريق القيادة",
        "nav.leadershipDesc": "تعرف على المديرين التنفيذيين لدينا",
        "nav.certifications": "الشهادات",
        "nav.certificationsDesc": "معايير الجودة",
        "home.hero.title": "ام اتش كي للتجارة وتموين السفن",
        "home.hero.subtitle": "شريكك الموثوق في التوريد البحري والتجارة والحلول الصناعية",
        "home.hero.cta": "استكشف الحلول",
        "company.tagline": "التميز البحري",
        "home.certifications.title": "شهادات الجودة",
        "home.certifications.iso": "معتمد ISO 9001:2015",
        "home.certifications.alwaysFresh": "طازج دائماً",
        "home.certifications.halal": "100٪ حلال",
        "home.certifications.premium": "جودة ممتازة",
        "about.title": "عن MHK",
        "about.history": "ام اتش كي للتجارة وتموين السفن ش.ذ.م.م هي شركة تجارية ذات سمعة طيبة مقرها في الإمارات العربية المتحدة، متخصصة في تقديم منتجات وخدمات عالية الجودة للصناعة البحرية والمواد الصناعية والإنشائية والسلع الاستهلاكية والأغذية والمشروبات. منذ تأسيسها في عام 2014، التزمت شركتنا بالتميز والموثوقية ورضا العملاء.",
        "about.growth": "تأسست من قبل هاريهاراسودان جناناسيكاران، نمت شركتنا بشكل مطرد على مر السنين، وأثبتت نفسها كشريك موثوق لأصحاب السفن والمشغلين والموردين. مع أساس قوي في التجارة وتموين السفن، قمنا بتوسيع محفظتنا لتلبية الاحتياجات المتنوعة للقطاع البحري والتجارة العامة.",
        "about.certifications": "نظام إدارة الجودة ISO 9001:2015",
        "form.name": "الاسم",
        "form.email": "البريد الإلكتروني",
        "form.phone": "الهاتف",
        "form.company": "الشركة",
        "form.category": "فئة المنتج",
        "form.message": "الرسالة",
        "form.selectCategory": "اختر فئة",
        "form.required": "هذا الحقل مطلوب",
        "form.invalidEmail": "يرجى إدخال عنوان بريد إلكتروني صالح",
        "form.invalidPhone": "يرجى إدخال رقم هاتف صالح",
        "form.success": "شكراً لك! سنتواصل معك قريباً.",
        "form.error": "تعذر إرسال رسالتك. يرجى المحاولة مرة أخرى أو الاتصال بنا مباشرة.",
        "footer.quickLinks": "روابط سريعة",
        "footer.contactInfo": "معلومات الاتصال",
        "footer.copyright": "© 2024 ام اتش كي للتجارة وتموين السفن ش.ذ.م.م. جميع الحقوق محفوظة."
    }
};

// Current language
let currentLanguage = localStorage.getItem('language') || 'en';

// Initialize the website
document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM loaded, initializing...');
    initializeLanguage();
    initializeNavigation();
    initializeHeader();
    initializeVideoRotation();
    initializeContactForm();
    initializeSmoothScrolling();

    // Initialize AOS if available
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true,
            offset: 100
        });
    }
});

// Language functionality
function initializeLanguage() {
    // Set initial language
    setLanguage(currentLanguage);

    // Add event listener to language toggle button
    const langToggle = document.getElementById('langToggle');
    if (langToggle) {
        langToggle.addEventListener('click', function () {
            // Toggle between EN and AR
            const newLang = currentLanguage === 'en' ? 'ar' : 'en';
            setLanguage(newLang);
        });
    }

    // Legacy support for old lang-btn class (if any exist)
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const lang = this.getAttribute('data-lang');
            if (lang) {
                setLanguage(lang);
            }
        });
    });
}

function setLanguage(lang) {
    console.log('Setting language to:', lang);
    currentLanguage = lang;
    localStorage.setItem('language', lang);

    // Update HTML attributes
    document.documentElement.lang = lang;
    document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';

    // Add body class for language-specific styling
    document.body.classList.remove('lang-en', 'lang-ar');
    document.body.classList.add(`lang-${lang}`);

    // Update all translatable elements
    document.querySelectorAll('[data-key]').forEach(element => {
        const key = element.getAttribute('data-key');
        if (translations[lang] && translations[lang][key]) {
            element.textContent = translations[lang][key];
            console.log(`Updated ${key}: ${translations[lang][key]}`);
        }
    });

    // Update language toggle button display
    const currentLangSpan = document.getElementById('currentLang');
    if (currentLangSpan) {
        currentLangSpan.textContent = lang.toUpperCase();
    }

    // Update language button states (legacy support)
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('lang-active');
        if (btn.getAttribute('data-lang') === lang) {
            btn.classList.add('lang-active');
        }
    });

    // Force re-render for RTL changes
    if (lang === 'ar') {
        document.body.style.fontFamily = "'Cairo', 'Noto Sans Arabic', system-ui, sans-serif";
    } else {
        document.body.style.fontFamily = "'Inter', system-ui, sans-serif";
    }
}

// Navigation functionality
function initializeNavigation() {
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function () {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Close mobile menu when clicking on links
    document.querySelectorAll('#mobileMenu a').forEach(link => {
        link.addEventListener('click', function () {
            mobileMenu.classList.add('hidden');
        });
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function (event) {
        if (!mobileMenuBtn.contains(event.target) && !mobileMenu.contains(event.target)) {
            mobileMenu.classList.add('hidden');
        }
    });
}

// Header scroll effect
function initializeHeader() {
    const header = document.getElementById('header');
    const headerContainer = document.getElementById('headerContainer');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 0) {
            headerContainer.classList.add('shadow-xl');
            headerContainer.classList.remove('shadow-lg');
        } else {
            headerContainer.classList.add('shadow-lg');
            headerContainer.classList.remove('shadow-xl');
        }
    });
}

// Video and Image rotation functionality
function initializeVideoRotation() {
    const video = document.getElementById('heroVideo');
    const image = document.getElementById('heroImage');
    const videos = [
        'public/videos/hero-bg.mp4',
        'public/videos/hero-bg-3.mp4',
        'public/videos/hero-bg-4.mp4',
        'public/videos/hero-bg-5.mp4'
    ];

    let currentIndex = 0;
    let showingImage = true;
    let imageTimeout = null;

    function showImage() {
        // Fade out video, fade in image
        video.style.opacity = '0';
        image.style.opacity = '1';
        showingImage = true;

        // Show image for 3 seconds
        imageTimeout = setTimeout(() => {
            showVideo();
        }, 3000);
    }

    function showVideo() {
        showingImage = false;

        // Set video source
        video.src = videos[currentIndex];
        video.load();

        // Fade out image, fade in video
        image.style.opacity = '0';
        video.style.opacity = '1';

        // Play video
        video.play().catch(err => {
            console.error('Video play error:', err);
            // If video fails, show image instead
            showImage();
        });
    }

    function nextMedia() {
        if (showingImage) {
            // Currently showing image, next is video
            showVideo();
        } else {
            // Currently showing video, next is image
            currentIndex = (currentIndex + 1) % videos.length;
            showImage();
        }
    }

    if (video && image) {
        // Start with image
        showImage();

        // When video ends, show image
        video.addEventListener('ended', function () {
            nextMedia();
        });

        video.addEventListener('error', function () {
            console.error('Video error, showing image');
            showImage();
        });
    }
}

// Contact form functionality
function initializeContactForm() {
    const form = document.getElementById('contactForm');
    const messageDiv = document.getElementById('formMessage');

    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            // Get form data
            const formData = new FormData(form);
            const data = Object.fromEntries(formData);

            // Basic validation
            if (!validateForm(data)) {
                return;
            }

            // Show loading state
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            submitBtn.innerHTML = '<span class="loading"></span> Sending...';
            submitBtn.disabled = true;

            // Simulate form submission (replace with actual endpoint)
            setTimeout(() => {
                showMessage('success', translations[currentLanguage]['form.success']);
                form.reset();

                // Reset button
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            }, 2000);
        });
    }
}

function validateForm(data) {
    const messageDiv = document.getElementById('formMessage');

    // Required fields
    if (!data.name || !data.email || !data.message) {
        showMessage('error', translations[currentLanguage]['form.required']);
        return false;
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.email)) {
        showMessage('error', translations[currentLanguage]['form.invalidEmail']);
        return false;
    }

    return true;
}

function showMessage(type, message) {
    const messageDiv = document.getElementById('formMessage');
    messageDiv.className = `mt-4 p-4 rounded-lg message-${type}`;
    messageDiv.textContent = message;
    messageDiv.classList.remove('hidden');

    // Hide message after 5 seconds
    setTimeout(() => {
        messageDiv.classList.add('hidden');
    }, 5000);
}

// Smooth scrolling for anchor links
function initializeSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerHeight = document.getElementById('header').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function (entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in-up');
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.card-hover, .bg-white').forEach(el => {
        observer.observe(el);
    });
});

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Performance optimization
window.addEventListener('load', function () {
    // Preload next video
    const video = document.getElementById('heroVideo');
    if (video) {
        const nextVideo = document.createElement('video');
        nextVideo.src = 'public/videos/hero-bg-3.mp4';
        nextVideo.preload = 'metadata';
    }
});

// Error handling
window.addEventListener('error', function (e) {
    console.error('JavaScript error:', e.error);
});

// Service worker registration (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
        navigator.serviceWorker.register('/sw.js')
            .then(function (registration) {
                console.log('SW registered: ', registration);
            })
            .catch(function (registrationError) {
                console.log('SW registration failed: ', registrationError);
            });
    });
}