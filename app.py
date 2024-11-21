from flask import Flask, render_template, request
from macro_logic import calculate_macros

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/input', methods=['GET', 'POST'])
def process_input():
    if request.method == 'POST':
        # Safely get form inputs
        goal = request.form.get('goal')
        weight = float(request.form.get('weight', 0))
        height_feet = int(request.form.get('height_feet', 0))
        height_inches = int(request.form.get('height_inches', 0))
        age = int(request.form.get('age', 0))
        gender = request.form.get('gender')
        activity_level = request.form.get('activity_level')
        
        # Ensure all required fields are filled out
        if not (goal and weight and height_feet and height_inches and age and gender and activity_level):
            return render_template('input.html', error="Please fill out all the fields.")

        # Calculate macros based on user input
        macros = calculate_macros(
            weight_lbs=weight, 
            height_feet=height_feet, 
            height_inches=height_inches, 
            age=age, 
            gender=gender, 
            activity_level=activity_level, 
            goal=goal
        )
        
        # Render the results page with the calculated macros
        return render_template('display_macros.html', macros=macros)

    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)

