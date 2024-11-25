from flask import Flask, render_template, request
from macro_logic import calculate_macros

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/input', methods=['GET', 'POST'])
def process_input():
    if request.method == 'POST':
        goal = request.form['goal']
        weight = float(request.form['weight'])
        height_feet = int(request.form['height_feet'])
        height_inches = int(request.form['height_inches'])
        age = int(request.form['age'])
        gender = request.form['gender']
        activity_level = request.form['activity_level']

        # Calculate macros based on user input
        macros = calculate_macros(weight_lbs=weight, height_feet=height_feet, height_inches=height_inches, age=age, gender=gender, activity_level=activity_level, goal=goal)

        # Add some rounding to the output values
        macros['calories'] = round(macros.get('calories', 0))
        macros['protein_grams'] = round(macros.get('protein_grams', 0))
        macros['carbs_grams'] = round(macros.get('carbs_grams', 0))
        macros['fat_grams'] = round(macros.get('fat_grams', 0))

        # Render the results page with the calculated macros
        return render_template('display_macros.html', macros=macros)

    return render_template('input.html')

@app.route('/food_chart', methods=['GET', 'POST'])
def food_chart():
    if request.method == 'POST':
        selected_proteins = request.form.getlist('protein')
        selected_carbs = request.form.getlist('carb')
        selected_fats = request.form.getlist('fat')
        selected_vegetables = request.form.getlist('vegetable')

        # Render the meal plan page with selected preferences
        return render_template('meal_plan.html', proteins=selected_proteins, carbs=selected_carbs, fats=selected_fats, vegetables=selected_vegetables)

    return render_template('food_chart.html')

if __name__ == '__main__':
    app.run(debug=True)
