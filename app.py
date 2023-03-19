import pickle
import pandas as pd
from flask import Flask, request, jsonify


app = Flask(__name__)

# Load pickle files for both models
tesla_model = pickle.load(open("modelForTesla1day.pkl", "rb"))
meta_model = pickle.load(open("modelForMeta1day.pkl", "rb"))
google_model = pickle.load(open("modelForGoogle1Day.pkl", "rb"))
gm_modle = pickle.load(open("modelForGM1day.pkl", "rb"))
apple_modle = pickle.load(open("modelForApple1Day.pkl", "rb"))

# Load the input data from a csv file
tesla_data = pd.read_csv("Tesla dataset for 1day.csv")
tesla_data.set_index('Date')
meta_data = pd.read_csv("Meta dataframe for 1day.csv")
meta_data.set_index('Date')
google_data = pd.read_csv("Google dataframe for 1day.csv")
google_data.set_index('Date')
gm_data = pd.read_csv("Gm dataset for 1day.csv")
gm_data.set_index('Date')
apple_data = pd.read_csv("apple dataframe for 1day.csv")
apple_data.set_index('Date')



# Define a route for processing the user input and making a prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input from the form
    user_input = request.form['input']

    # Determine which model to use based on the user input
    if user_input == 'model_1':
        model = model_1
    elif user_input == 'model_2':
        model = model_2
    else:
        return jsonify({'error': 'Invalid input. Please try again.'})

    # Make a prediction using the selected model and the input data
    prediction = model.predict(input_data)

    # Get the last element of the prediction array
    result = prediction[-1]

    # If the result is 1, display "BUY", otherwise display "SELL"
    if result == 1:
        return jsonify({'result': 'BUY'})
    else:
        return jsonify({'result': 'SELL'})

if __name__ == '__main__':
    app.run(debug=True)
