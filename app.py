# Import required libraries
import pickle
from flask import Flask, request, jsonify
import pandas as pd

# Load the pickled models
model1 = pickle.load(open('model1.pkl', 'rb'))
model2 = pickle.load(open('model2.pkl', 'rb'))

# Load the data frame from a CSV file
data_frame = pd.read_csv('data.csv')

# Create a Flask app
app = Flask(__name__)

# Define a function for making prediction 1
def predict1(data):
    # Preprocess the data as required
    # Select the required features from the data frame
    features = ['feature1', 'feature2', 'feature3']
    data = data_frame.loc[data_frame['id'] == data['id'], features].values
    # Make prediction using model 1
    pred = model1.predict(data)
    # Return the prediction
    return pred

# Define a function for making prediction 2
def predict2(data):
    # Preprocess the data as required
    # Select the required features from the data frame
    features = ['feature4', 'feature5', 'feature6']
    data = data_frame.loc[data_frame['id'] == data['id'], features].values
    # Make prediction using model 2
    pred = model2.predict(data)
    # Return the prediction
    return pred

# Define an endpoint for receiving data and making predictions
@app.route('/predict', methods=['POST'])
def get_prediction():
    # Get the data from the request
    data = request.get_json(force=True)
    # Check user input to determine which model to use
    if data['model'] == 'model1':
        prediction = predict1(data)
    elif data['model'] == 'model2':
        prediction = predict2(data)
    else:
        return jsonify({'error': 'Invalid model selected!'})
    # Return the prediction as a JSON object
    return jsonify({'prediction': prediction.tolist()})

# Define a home page
@app.route('/')
def home():
    return 'Welcome to my multi-pickle ML implementation using Flask!'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
