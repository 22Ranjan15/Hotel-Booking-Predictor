import os
import joblib
import numpy as np
from flask import Flask, render_template, request
from config.paths_config import MODEL_OUTPUT_PATH

app = Flask(__name__)

# Add error handling for model loading
try:
    loaded_model = joblib.load(MODEL_OUTPUT_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    loaded_model = None

## Route for a home page
@app.route('/')
def index():
    return render_template('home.html') 

# Route for Prediction Page
@app.route('/predict', methods=['GET', 'POST'])
def make_prediction():
    prediction = None # Initialize prediction
    error = None      # Initialize error

    if request.method == 'POST':
        try:
            # Get form data
            lead_time = int(request.form["lead_time"])
            no_of_special_requests = int(request.form["no_of_special_requests"])
            avg_price_per_room = float(request.form["avg_price_per_room"])
            arrival_month = int(request.form["arrival_month"])
            arrival_date = int(request.form["arrival_date"])
            market_segment_type = int(request.form["market_segment_type"])
            no_of_week_nights = int(request.form["no_of_week_nights"])
            no_of_weekend_nights = int(request.form["no_of_weekend_nights"])
            type_of_meal_plan = int(request.form["type_of_meal_plan"])
            room_type = int(request.form["room_type"])

            # Create feature array
            features = np.array([
                [
                    lead_time, no_of_special_requests, avg_price_per_room,
                    arrival_month, arrival_date, market_segment_type, no_of_week_nights,
                    no_of_weekend_nights, type_of_meal_plan, room_type
                ]
            ])

            # Check if model is loaded properly
            if loaded_model is not None:
                prediction = loaded_model.predict(features)[0]
            else:
                error = "Model not properly loaded"
                
        except Exception as e:
            error = f"Error processing request: {str(e)}"
    
    return render_template('index.html', prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


