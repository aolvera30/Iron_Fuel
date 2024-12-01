document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('inputForm');
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            // Collect form data
            const formData = {
                goal: document.getElementById('goal').value,
                weight: parseFloat(document.getElementById('weight').value),
                height_feet: parseInt(document.getElementById('height_feet').value),
                height_inches: parseInt(document.getElementById('height_inches').value),
                age: parseInt(document.getElementById('age').value),
                gender: document.getElementById('gender').value,
                activity_level: document.getElementById('activity_level').value
            };

            // Send data to backend API
            fetch('/api/calculate_macros', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    // Update the Macros Overview page with the response data
                    document.getElementById('calories').textContent = data.calories;
                    document.getElementById('protein').textContent = data.protein_grams;
                    document.getElementById('carbs').textContent = data.carbs_grams;
                    document.getElementById('fats').textContent = data.fat_grams;

                    // Redirect to the macro overview page after successfully getting the data
                    window.location.href = "/overview";
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while processing your request. Please try again.');
            });
        });
    }
});


