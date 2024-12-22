from flask import Flask, request, render_template
import pickle
from datetime import datetime
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained models and preprocessing objects
model = pickle.load(open('model/model.pkl', 'rb'))  # Trained model
preprocessing = pickle.load(open('model/preprocessing.pkl', 'rb'))

@app.route('/')
def home():
    return "<h2> Go to /predict </h2>"  # HTML form for user input

@app.route('/predict', methods=['POST','GET'])
def predict():
    try:
        # Get form data
        Airline = request.form.get('airline')
        Class = request.form.get('class')
        Source = request.form.get('source')
        Destination = request.form.get('destination')
        Total_stops = int(request.form.get('totalStops'))
        Date = request.form.get('date')

        # Parse date and extract features
        input_date = datetime.strptime(Date, "%Y-%m-%d")
        Days_left = (input_date - datetime.today()).days
        Month = input_date.month
        Day = input_date.day

        # Create a dictionary of form data
        feature_dict = {'Airline': Airline, 'Class': Class, 'Source': Source, 'Destination': Destination, 'Total_stops': Total_stops, 'Days_left': Days_left, 'Month': Month, 'Day': Day}
        final_features = pd.DataFrame([feature_dict])

        # Preprocess the data
        final_features = preprocessing.transform(final_features)

        # Make prediction   
        predicted_price = model.predict(final_features)
        return render_template('form.html', Predicted_price=f"The predicted fare is: ₹{predicted_price[0]:.2f}")

    except Exception as e:
        return render_template('form.html', Predicted_price=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
