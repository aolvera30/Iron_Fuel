from flask import Flask, render_template, request, session
from macro_logic import calculate_macros
import logging
import json
import os
from datetime import timedelta

app = Flask(__name__, static_folder='static')
app.secret_key = os.urandom(24)  # Secure secret key
app.permanent_session_lifetime = timedelta(minutes=30)

# Configure logging to see debug information in the console
logging.basicConfig(level=logging.INFO)

# Load the Food Chart from a JSON file
with open('data/food_chart.json', 'r') as f:
    app.config['FOOD_CHART'] = json.load(f)


@app.route('/')
def home():
    """Welcome page route."""
    return render_template('index.html')


@app.route('/input', methods=['GET', 'POST'])
def user_input():
    """User input page route."""
    if request.method == 'GET':
        # Render the input form
        return render_template('input.html')

    elif request.method == 'POST':
        try:
            # Collect form data
            form_data = request.form
            goal = form_data.get('goal')
            weight = form_data.get('weight')
            height_feet = form_data.get('height_feet')
            height_inches = form_data.get('height_inches')
            age = form_data.get('age')
            gender = form_data.get('gender')
            activity_level = form_data.get('activity_level')

            # Validate inputs
            if not all([goal, weight, height_feet, height_inches, age, gender, activity_level]):
                return render_template('input.html', error="Please fill out all fields.")

            # Calculate macros
            macros = calculate_macros(
                weight_lbs=float(weight),
                height_feet=int(height_feet),
                height_inches=int(height_inches),
                age=int(age),
                gender=gender,
                activity_level=activity_level,
                goal=goal
            )

            # Store macros in session
            session['macros'] = macros

            # Redirect to the overview page
            return render_template('overview.html', macros=macros, food_chart=app.config['FOOD_CHART'])

        except Exception as e:
            logging.error(f"Error in /input POST: {e}")
            return render_template('input.html', error="An unexpected error occurred.")


@app.route('/overview', methods=['GET'])
def macro_overview():
    """Overview page route."""
    # Retrieve macros from session
    macros = session.get('macros')

    # If no macros found, redirect to input page with an error
    if not macros:
        return render_template('input.html', error="Please submit your details first.")

    # Retrieve food chart
    food_chart = app.config['FOOD_CHART']

    # Render the overview page
    return render_template('overview.html', macros=macros, food_chart=food_chart)


if __name__ == '__main__':
    app.run(debug=True)




