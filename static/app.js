// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", () => {
    // Get the form element by its ID
    const form = document.getElementById("inputForm");

    // Add an event listener to handle form submission
    form.addEventListener("submit", async (event) => {
        event.preventDefault(); // Prevent the default form submission

        // Collect form data
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        try {
            // Send a POST request to the /api/calculate_macros endpoint
            const response = await fetch("/api/calculate_macros", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            console.log("Response:", response);

            if (response.ok) {
                // Get the HTML response and replace the current document
                const html = await response.text();

                console.log("HTML:", html);

                document.open(); // Open a new document context
                document.write(html); // Replace the current page with the new content
                document.close(); // Close the document context
            } else {
                // Handle errors (e.g., missing fields or server issues)
                const errorData = await response.json();
                alert(errorData.error || "An error occurred while calculating macros.");
            }
        } catch (error) {
            console.error("Error submitting form:", error);
            alert("An unexpected error occurred. Please try again.");
        }
    });
});


