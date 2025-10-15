from flask import Flask, render_template, request
from diet_core import get_diet_recommendation # Import your diet recommendation function
from flask import session, redirect, url_for

app = Flask(__name__)
app.secret_key = "your-unique-secret-key"

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')  # Or home.html

# Diet Planner route (GET + POST)
@app.route('/diet_planner', methods=['GET', 'POST'])
def diet_planner():
    if request.method == 'POST':
        # Collect form data
        data = {
            "age": int(request.form['age']),
            "gender": request.form['gender'],
            "weight": float(request.form['weight']),
            "height": float(request.form['height']),
            "activity": request.form['activity'],
            "goal": request.form['goal'],
            "preference": request.form['preference'],
            "allergen": request.form['allergen']
        }

        # Generate recommendation and store in session
        session['recommendation'] = get_diet_recommendation(data)

        # Redirect to avoid resubmission on refresh
        return redirect(url_for('diet_planner'))

    # GET request: retrieve recommendation from session if it exists
    recommendation = session.pop('recommendation', None)

    return render_template('diet_planner.html', recommendation=recommendation)


# Other pages
@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/ask_me')
def ask_me():
    return render_template('ask_me.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
