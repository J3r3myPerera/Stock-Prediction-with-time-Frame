# Import necessary libraries
from flask import Flask, request, jsonify
import requests
import pickle
import numpy as np

# Create Flask app
app = Flask(__name__)

# Define routes for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_input = data['user_input']
    target_url = data['target_url']

    if user_input == 'model1':
        with open('model1.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('dataset1.pkl', 'rb') as f:
            dataset = pickle.load(f)
    elif user_input == 'model2':
        with open('model2.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('dataset2.pkl', 'rb') as f:
            dataset = pickle.load(f)
    else:
        return jsonify({'message': 'Invalid user input'})

    X_test = np.array(data['X_test'])
    y_pred = model.predict(X_test)

    # Send prediction to target URL
    response = requests.post(target_url, json={'y_pred': y_pred.tolist()})
    return response.content

# Run app
if __name__ == '__main__':
    app.run(debug=True)
