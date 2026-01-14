document.addEventListener('DOMContentLoaded', () => {
    // Create hamburger button
    const headerContainer = document.querySelector('.site-header .container');
    if (headerContainer) {
        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'mobile-menu-toggle';
        toggleBtn.innerHTML = '<span></span><span></span><span></span>';
        toggleBtn.setAttribute('aria-label', 'Toggle Navigation');

        // Insert before nav
        const nav = headerContainer.querySelector('.main-nav');
        if (nav) {
            headerContainer.insertBefore(toggleBtn, nav);

            toggleBtn.addEventListener('click', () => {
                nav.classList.toggle('active');
                toggleBtn.classList.toggle('active');
            });
        }
    }
});
