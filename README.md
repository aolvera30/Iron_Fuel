# Iron_Fuel

**Iron_Fuel** is a Flask-based web application built with Python, designed to help users calculate macronutrients and receive food recommendations. It emphasizes a clean, modular design with separate structures for CSS styling and HTML templates, ensuring maintainability and scalability.



## Features

1. **Macro Calculation**: Users can input their details (weight, height, age, activity level, etc.) and get calculated macros (calories, protein, carbs, fats).
2. **Recommended Foods**: Displays a list of recommended food categories (Proteins, Complex Carbs, Fats, Vegetables, Fruits) for better dietary planning.

## Folder Structure

```
IRON_FUEL/
├── app.py                # Main Flask application
├── macro_logic.py        # Macro calculation logic
├── data/
│   └── food_chart.json   # Static JSON file with recommended foods
├── static/
│   └── css/
│       ├── index.css     # CSS for the home page
│       ├── input.css     # CSS for the input page
│       ├── overview.css  # CSS for the overview page
├── templates/
│   ├── index.html        # Welcome page
│   ├── input.html        # User input form
│   ├── overview.html     # Macro overview page
├── requirements.txt      # List of Python dependencies
├── README.md             # Project information
└── .gitignore            # Ignored files for version control
```

## Routes

1. `/`  
   - **Description**: Displays the welcome page with a brief description of the tool.  
   - **Methods**: `GET`

2. `/input`  
   - **Description**: Allows users to input their details for macro calculation.  
   - **Methods**: `GET`, `POST`

3. `/overview`  
   - **Description**: Shows the calculated macros and the recommended food categories.  
   - **Methods**: `GET`


