from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/input', methods=['GET', 'POST'])
def process_input():
    if request.method == 'POST':
        goal = request.form['goal']
        # For now, just print the goal. Later, we can use it to customize plans.
        print(f"Primary Fitness Goal: {goal}")
        # After receiving the input, you can redirect to the next page.
        return render_template('meal_plan.html', goal=goal)
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
