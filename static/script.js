document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const loadingElement = document.getElementById('loading');
    const predictButton = document.getElementById('predict-button');
    
    // Show loading indicator when form is submitted
    if (form) {
        form.addEventListener('submit', function() {
            if (form.checkValidity()) {
                loadingElement.classList.remove('hidden');
                predictButton.disabled = true;
            }
        });
    }
    
    // Adjust arrival date options based on selected month
    const arrivalMonth = document.getElementById('arrival_month');
    const arrivalDate = document.getElementById('arrival_date');
    
    if (arrivalMonth && arrivalDate) {
        arrivalMonth.addEventListener('change', function() {
            updateDaysInMonth(arrivalMonth.value);
        });
        
        // Initial days update
        updateDaysInMonth(arrivalMonth.value);
    }
    
    function updateDaysInMonth(month) {
        if (!month) return;
        
        const daysInMonth = getDaysInMonth(parseInt(month));
        
        // Store current selection if valid
        const currentSelection = arrivalDate.value;
        
        // Clear options except the first one
        while (arrivalDate.options.length > 1) {
            arrivalDate.remove(1);
        }
        
        // Add appropriate number of days
        for (let i = 1; i <= daysInMonth; i++) {
            const option = document.createElement('option');
            option.value = i;
            option.textContent = i;
            arrivalDate.appendChild(option);
        }
        
        // Restore selection if valid
        if (currentSelection && parseInt(currentSelection) <= daysInMonth) {
            arrivalDate.value = currentSelection;
        }
    }
    
    function getDaysInMonth(month) {
        // Assuming current year for leap year calculation
        const year = new Date().getFullYear();
        
        // Days in each month (1-based indexing)
        const daysPerMonth = [0, 31, isLeapYear(year) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        return daysPerMonth[month] || 31;
    }
    
    function isLeapYear(year) {
        return ((year % 4 === 0) && (year % 100 !== 0)) || (year % 400 === 0);
    }
    
    // Form validation enhancement
    const inputs = document.querySelectorAll('input[type="number"]');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            if (this.value < 0) {
                this.value = 0;
            }
        });
    });
});