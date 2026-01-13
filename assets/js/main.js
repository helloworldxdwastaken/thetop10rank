// RANKIN - MAIN JAVASCRIPT

// Simple search functionality
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        const searchButton = searchInput.nextElementSibling;
        
        searchButton.addEventListener('click', function(e) {
            e.preventDefault();
            const query = searchInput.value.trim();
            if (query) {
                window.location.href = `/search/?q=${encodeURIComponent(query)}`;
            }
        });
        
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                const query = searchInput.value.trim();
                if (query) {
                    window.location.href = `/search/?q=${encodeURIComponent(query)}`;
                }
            }
        });
    }
});

// Mobile nav toggle (if needed in future)
// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href.length > 1) {
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// Add loading state to external links
document.querySelectorAll('a[target="_blank"]').forEach(link => {
    link.addEventListener('click', function() {
        this.style.opacity = '0.6';
    });
});

// Table sorting (for ranking tables)
function sortTable(table, column, asc = true) {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    
    rows.sort((a, b) => {
        const aVal = a.children[column].textContent.trim();
        const bVal = b.children[column].textContent.trim();
        
        // Try numeric comparison first
        const aNum = parseFloat(aVal.replace(/[^0-9.-]/g, ''));
        const bNum = parseFloat(bVal.replace(/[^0-9.-]/g, ''));
        
        if (!isNaN(aNum) && !isNaN(bNum)) {
            return asc ? aNum - bNum : bNum - aNum;
        }
        
        // Fallback to string comparison
        return asc ? aVal.localeCompare(bVal) : bVal.localeCompare(aVal);
    });
    
    rows.forEach(row => tbody.appendChild(row));
}

// Initialize table sorting on click (optional enhancement)
document.querySelectorAll('.ranking-table th').forEach((th, index) => {
    th.style.cursor = 'pointer';
    th.title = 'Click to sort';
    
    let asc = true;
    th.addEventListener('click', function() {
        const table = this.closest('table');
        sortTable(table, index, asc);
        asc = !asc;
        
        // Visual feedback
        document.querySelectorAll('.ranking-table th').forEach(h => h.style.fontWeight = '600');
        this.style.fontWeight = '700';
    });
});

