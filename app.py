from flask import Flask, render_template, request
import json
from macro_logic import calculate_macros  
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return render_template('welcome.html')  

@app.route('/input', methods=['GET', 'POST'])
def process_input():
    if request.method == 'POST':
        try:
            # Collect user input
            goal = request.form.get('goal')
            weight = request.form.get('weight', type=float)
            height_feet = request.form.get('height_feet', type=int)
            height_inches = request.form.get('height_inches', type=int)
            age = request.form.get('age', type=int)
            gender = request.form.get('gender')
            activity_level = request.form.get('activity_level')

            if not all([goal, weight, height_feet, height_inches, age, gender, activity_level]):
                return "Missing form fields. Please provide all required inputs.", 400

            # Calculate macros
            macros = calculate_macros(
                weight_lbs=weight,
                height_feet=height_feet,
                height_inches=height_inches,
                age=age,
                gender=gender,
                activity_level=activity_level,
                goal=goal
            )

            # Round macros for display
            macros['calories'] = round(macros.get('calories', 0))
            macros['protein_grams'] = round(macros.get('protein_grams', 0))
            macros['carbs_grams'] = round(macros.get('carbs_grams', 0))
            macros['fat_grams'] = round(macros.get('fat_grams', 0))

            # Load food chart from JSON
            try:
                with open('food_chart.json') as file:
                    food_chart = json.load(file)
            except FileNotFoundError:
                return "Error: 'food_chart.json' not found.", 500

            # Render the overview with macros and food chart
            return render_template(
                'macro_overview.html',
                macros=macros,
                food_chart=food_chart
            )

        except Exception as e:
            # Log any exceptions that occur
            logging.error(f"Error during processing: {str(e)}")
            return f"An error occurred: {e}", 500

    # If GET request, show the input form
    return render_template('user_input.html')

if __name__ == '__main__':
    app.run(debug=True)

