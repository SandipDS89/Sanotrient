from flask import Flask, request, jsonify
from diet_core import load_dataset, calculate_targets, filter_foods, generate_complete_meal_plan

app = Flask(__name__)

# Load dataset once
foods_df = load_dataset("meal_dataset.csv")

@app.route("/recommend", methods=["POST"])
def recommend():
    user = request.json
    targets = calculate_targets(user)
    filtered = filter_foods(foods_df, user)
    meal_plan, nutrition = generate_complete_meal_plan(filtered, targets, user)

    return jsonify({"targets": targets, "plan": meal_plan, "nutrition": nutrition})

if __name__ == "__main__":
    app.run(debug=True)
