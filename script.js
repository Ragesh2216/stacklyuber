document.addEventListener('DOMContentLoaded', () => {

    /* =========================================
       1. START SCREEN ANIMATION
       ========================================= */
    const startScreen = document.getElementById('start-screen');

    // Only run splash screen if it exists on the page
    if (startScreen) {
        // Hide scrollbar during splash
        document.body.style.overflow = 'hidden';

        // Wait for animations to finish (approx 3.0s total)
        setTimeout(() => {
            startScreen.classList.add('hidden');
            document.body.style.overflow = ''; // Restore scrolling

            // Optional: remove from DOM to clean up
            setTimeout(() => {
                if (startScreen.parentNode) {
                    startScreen.parentNode.removeChild(startScreen);
                }
            }, 600); // Wait for fade transition
        }, 3000);
    }


    /* =========================================
       2. MOBILE NAVIGATION MENU
       ========================================= */
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenuOverlay = document.querySelector('.mobile-menu-overlay');

    if (mobileMenuBtn && mobileMenuOverlay) {
        mobileMenuBtn.addEventListener('click', () => {
            const isOpen = mobileMenuBtn.classList.contains('open');

            if (isOpen) {
                // Close menu
                mobileMenuBtn.classList.remove('open');
                mobileMenuOverlay.classList.remove('open');
                // Restore body scroll unless start screen is showing
                if (!startScreen || startScreen.classList.contains('hidden')) {
                    document.body.style.overflow = '';
                }
            } else {
                // Open menu
                mobileMenuBtn.classList.add('open');
                mobileMenuOverlay.classList.add('open');
                // Prevent body scroll behind menu
                document.body.style.overflow = 'hidden';
            }
        });
    }

    /* =========================================
       3. HEADER SCROLL EFFECT
       ========================================= */
    const header = document.querySelector('.header');
    let lastScrollItem = 0;

    if (header) {
        window.addEventListener('scroll', () => {
            let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

            // Scrolled past top
            if (currentScroll > 50) {
                header.classList.add('scrolled-up');
            } else {
                header.classList.remove('scrolled-up');
            }

            // Optional: Hide on scroll down, show on scroll up
            /*
            if (currentScroll > lastScrollItem && currentScroll > header.offsetHeight) {
                // Scroll down
                header.classList.add('scrolled-down');
            } else {
                // Scroll up
                header.classList.remove('scrolled-down');
            }
            */
            lastScrollItem = currentScroll <= 0 ? 0 : currentScroll; // For Mobile or negative scrolling
        }, false);
    }

    /* =========================================
       4. SCROLL ANIMATIONS (Intersection Observer)
       ========================================= */
    const animElements = document.querySelectorAll('.animate-on-scroll');

    if (animElements.length > 0) {
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.15 // Trigger when 15% of element is visible
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target); // Stop observing once animated
                }
            });
        }, observerOptions);

        animElements.forEach(el => {
            observer.observe(el);
        });
    }

    /* =========================================
       5. UNIVERSAL 404 BUTTON ROUTING
       ========================================= */
    // Find any buttons or links specifically marked to go to 404
    // Or attach generically to .btn that aren't navigation

    const actionButtons = document.querySelectorAll('.route-404, .btn:not(.nav-link):not([href^="mailto"]):not([href^="tel"]):not([type="submit"])');

    actionButtons.forEach(btn => {
        // Only attach if it doesn't already have an explicit href inside the site structure that shouldn't open 404
        const href = btn.getAttribute('href');
        if (!href || href === '#' || btn.tagName === 'BUTTON') {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                // Add a small delay for click animation if needed
                setTimeout(() => {
                    window.location.href = '404.html';
                }, 150);
            });
        }
    });

});
