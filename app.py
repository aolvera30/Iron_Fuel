from flask import Flask, request, jsonify, render_template, url_for, redirect
from macro_logic import calculate_macros  # Import your macro calculation function
import json
import logging

app = Flask(__name__, static_folder='static')

# Configure logging to see debug information in the console
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return render_template('welcome.html')  # Serve the welcome page

@app.route('/input', methods=['GET', 'POST'])
def user_input():
    if request.method == 'GET':
        return render_template('user_input.html')  # Serve the user input form
    elif request.method == 'POST':
        return redirect('/overview')

@app.route('/overview')
def macro_overview():
    return render_template('macro_overview.html')  # Serve the macros overview page

# API endpoint to calculate macros
@app.route('/api/calculate_macros', methods=['POST'])
def calculate_macros_api():
    try:
        # Collect user input from JSON request
        data = request.get_json()
        app.logger.info(f"Received data: {data}")

        goal = data.get('goal')
        weight = data.get('weight')
        height_feet = data.get('height_feet')
        height_inches = data.get('height_inches')
        age = data.get('age')
        gender = data.get('gender')
        activity_level = data.get('activity_level')

        # Ensure all required fields are provided
        if not all([goal, weight, height_feet, height_inches, age, gender, activity_level]):
            return jsonify({"error": "Missing form fields. Please provide all required inputs."}), 400

        # Calculate macros using your macro logic function
        macros = calculate_macros(
            weight_lbs=weight,
            height_feet=height_feet,
            height_inches=height_inches,
            age=age,
            gender=gender,
            activity_level=activity_level,
            goal=goal
        )

        # Log calculated macros
        app.logger.info(f"Calculated Macros: {macros}")

        # Return the calculated macros as a JSON response
        return jsonify(macros)

    except Exception as e:
        app.logger.error(f"Error during macro calculation: {str(e)}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)


