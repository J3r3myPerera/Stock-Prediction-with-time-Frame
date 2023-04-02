# # Import necessary libraries
# from flask import Flask, request, jsonify
# import requests
# import pickle
# import numpy as np

# # Create Flask app
# app = Flask(__name__)

# # Define routes for prediction
# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     user_input = data['user_input']
#     target_url = data['target_url']

#     if user_input == 'model1':
#         with open('model1.pkl', 'rb') as f:
#             model = pickle.load(f)
#         with open('dataset1.pkl', 'rb') as f:
#             dataset = pickle.load(f)
#     elif user_input == 'model2':
#         with open('model2.pkl', 'rb') as f:
#             model = pickle.load(f)
#         with open('dataset2.pkl', 'rb') as f:
#             dataset = pickle.load(f)
#     else:
#         return jsonify({'message': 'Invalid user input'})

#     X_test = np.array(data['X_test'])
#     y_pred = model.predict(X_test)

#     # Send prediction to target URL
#     response = requests.post(target_url, json={'y_pred': y_pred.tolist()})
#     return response.content

# # Run app
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request

app2 = Flask(__name__)

@app2.route("/")
def Home():
    return render_template('Companies_and_Time_Duration.html')

@app2.route('/predict', methods=['POST'])
def predict():
    # Get the option value from the radio button
    option = request.form.get('option')

    # Get the value of the slider
    slider_value1 = request.form.get('slider')
    # slider_value2 = request.form.get('slider2')

    # Determine which model to use based on the user input
    if option == 'option2' and slider_data1 == 0:
        model = tesla_model1
        rediction = model.predict(tesla_data1)
    elif option == 'option4' and slider_data1 == 0:
        model = meta_model1
        prediction = model.predict(meta_data1)
        # prediction = model.predict(meta_data1[new_predictors])
    elif option == 'option3' and slider_data1 == 0:
        model = google_model1
        prediction = model.predict(google_data1)
            # prediction = model.predict(google_data1[new_predictors])
    elif option == 'option5' and slider_data1 == 0:
        model = gm_modle1
        prediction = model.predict(gm_data1)
        # prediction = model.predict(gm_data1[new_predictors])
    elif option == 'option1' and slider_data1 == 0:
        model = apple_modle1
        prediction = model.predict(apple_data1)

    # Return the prediction as a JSON response
    result = prediction[-1]
    if result == 1:
        # return jsonify({'result': 'BUY'})
         return render_template('Companies_and_Time_Duration.html', prediction_text='The signal is BUY!')
    else:
        return render_template('Companies_and_Time_Duration.html', prediction_text='The signal is SELL!')

    # return {'prediction': prediction}

if __name__ == '__main__':
    app2.run()
