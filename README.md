# Iron_Fuel Project

## Overview

Iron_Fuel is a Flask-based web application designed to help users calculate their daily macronutrient needs and create a simple meal plan tailored to their goals. ,by calculating their target calories, proteins, fats, and carbohydrates.

## Features

- **User Input Form:** Users provide personal data, such as weight, height, age, and activity level, through a simple form.
- **Macro Calculation:** Uses the Mifflin-St Jeor equation to estimate Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE), adjusting calorie goals based on user preferences.
- **Personalized Results:** Displays daily macronutrient targets for calories, protein, carbs, and fats.
- **Food Recommendations:** Suggests foods for proteins, complex carbs, fats, vegetables, and fruits.
- **REST API Endpoint:** Provides an API endpoint (`/api/calculate_macros`) for macro calculations via JSON requests.

## Project Structure

```
Iron_Fuel/
├── app.py                  # Flask application code
├── macro_logic.py          # Macro calculation logic module
├── static/                 # Static files (e.g., JS, CSS)
│   ├── app.js              # JavaScript for handling user input and API calls
├── templates/              # HTML templates
│   ├── welcome.html        # Home page for Iron_Fuel
│   ├── user_input.html     # Page where users enter their information
│   ├── macro_overview.html # Page displaying calculated macros
├── requirements.txt        # Project dependencies
```

## Setup and Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/aolvera30/Iron_Fuel.git
   ```

2. **Navigate into the project directory**

   ```bash
   cd Iron_Fuel
   ```

3. **Create a virtual environment and activate it**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask app**

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## API Endpoint

- **URL:** `/api/calculate_macros`
- **Method:** POST
- **Payload (JSON):**
  ```json
  {

      "goal": "lose_fat",

      "weight": 160,

      "height_feet": 5,

      "height_inches": 3,

      "age": 28,

      "gender": "female",

      "activity_level": "moderately_active"

  }
  ```
  **Response (JSON):**
  ```json
  {
      "food_chart": {
          "Complex Carbs": [
              "Brown / White Rice",
              "Quinoa",
              "Gluten Free Oats",
              "Red / White Potatoes",
              "Sweet Potatoes / Yams",
              "Oatmeal",
              "Caramel Rice Cakes",
              "Whole Wheat Pasta / Tortillas",
              "Cream of Rice / Grits",
              "Ezekiel Bread"
          ],
          "Fats": [
              "Peanut Butter",
              "Almond Butter",
              "Flax Seed Oil",
              "Olive Oil",
              "Macadamia Nut Oil",
              "Coconut Oil",
              "Fish Oil",
              "Pistachios",
              "Avocados",
              "Raw Almonds",
              "Walnuts"
          ],
          "Fruits": [
              "Blueberries",
              "Strawberries",
              "Raspberries",
              "Banana",
              "Apple",
              "Orange",
              "Watermelon",
              "Pineapple",
              "Grapes"
          ],
          "Proteins": [
              "Whole Eggs",
              "Egg Whites",
              "Extra Lean Ground Turkey",
              "Extra Lean Ground Beef",
              "Top Sirloin",
              "Turkey Breast",
              "Salmon / Tuna",
              "Tilapia / Halibut / Cod",
              "Scallops / Shrimp",
              "Chicken Breast",
              "Protein Shake"
          ],
          "Vegetables": [
              "Asparagus",
              "Spinach",
              "Broccoli",
              "Kale",
              "Green Peas",
              "Sweet Peas",
              "Cauliflower",
              "Green Beans",
              "Collard Greens",
              "Cucumbers",
              "Brussels Sprouts"
          ]
      },
      "macros": {
          "calories": 1709,
          "carbs": 175,
          "fats": 47,
          "protein": 145
      },
      "tips": [
          "- On rest days, choose lower glycemic carbs for energy and recovery.",
          "- Drink at least 2-3 liters of water daily to stay hydrated.",
          "- Consume high glycemic carbs post-workout to replenish energy.",
          "- Eat pre-workout meals 1-2 hours before training and post-workout meals within 30-60 minutes."
      ]
  }
  ```

## Technologies Used

- **Flask**: Web framework for building backend logic and routes.
- **HTML, CSS, JavaScript**: Frontend for user interaction.
- **Mifflin-St Jeor Equation**: For calculating BMR and caloric needs.

## Key Code Components

### Macro Calculation (`macro_logic.py`)

The `calculate_macros` function calculates the user's daily macronutrient needs based on user input (weight, height, age, gender, activity level, and goal). It uses the Mifflin-St Jeor equation to calculate BMR and adjusts it based on the activity level and goal.

### JavaScript Form Submission (`static/app.js`)

Handles form submissions by sending user data as a JSON payload to the `/api/calculate_macros` endpoint and dynamically updates the page with the calculated macronutrient information.

## Disclaimer

The calculated macronutrient values are estimates based on user input. Consult a nutritionist for personalized recommendations.

##

