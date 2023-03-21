import pickle
import pandas as pd
from flask import Flask, request, jsonify


app = Flask(__name__)

# Load pickle files for the models
#Models for one day
tesla_model1 = pickle.load(open("modelForTesla1day.pkl", "rb"))
meta_model1 = pickle.load(open("modelForMeta1day.pkl", "rb"))
google_model1 = pickle.load(open("modelForGoogle1Day.pkl", "rb"))
gm_modle1 = pickle.load(open("modelForGM1day.pkl", "rb"))
apple_modle1 = pickle.load(open("modelForApple1Day.pkl", "rb"))

#Models for 1week
apple_model1wk = pickle.load(open("modelfor1weekApple.pkl", rb))
gm_model1wk = pickle.load(open("modelfor1weekGM.pkl", rb))
google_model1wk = pickle.load(open("modelfor1weekGoole.pkl", rb))
meta_model1wk = pickle.load(open("modelfor1weekMeta.pkl", rb))
tesla_model1wk = pickle.load(open("modelForTesla1wk.pkl", rb))

#Models for 2weeks
apple_model2wk = pickle.load(open("ModelForApple2Weeks.pkl", rb))
gm_model2wk = pickle.load(open("ModelFor2weeksGM.pkl", rb))
google_model2wk = pickle.load(open("ModelFor2WeeksGoogle.pkl", rb))
meta_model2wk = pickle.load(open("ModelFor2WeeksGoogle.pkl", rb))
tesla_model2wk = pickle.load(open("modelFor2WeeksTesla.pkl", rb))


#Models for 3weeks
apple_model3wk = pickle.load(open("modelForApple3Weeks.pkl", rb))
gm_model3wk = pickle.load(open("modelForGm3Weeks.pkl", rb))
google_model3wk = pickle.load(open("modelForGoogleFor3Weeks.pkl", rb))
meta_model3wk = pickle.load(open("modelForMeta3Weeks.pkl", rb))
tesla_model3wk = pickle.load(open("modelForTesla3weeks.pkl", rb))


#Models for 1 month
apple_model1mo = pickle.load(open("ModelFor1MonthApple.pkl", rb))
gm_model1mo = pickle.load(open("ModelForGm1Month.pkl", rb))
google_model1mo = pickle.load(open("modelForGoogle1Month.pkl", rb))
# meta_model1mo = pickle.load(open("modelForApple3Weeks.pkl", rb))
tesla_model1mo = pickle.load(open("modelForTesla1Month.pkl", rb))


#models for 3months
apple_model3mo = pickle.load(open("modelForApple3Months.pkl", rb))
gm_model3mo = pickle.load(open("modelForGm3Months.pkl", rb))
google_model3mo = pickle.load(open("modelForGoogle3months.pkl", rb))
meta_model3mo = pickle.load(open("modelForMeta3Months.pkl", rb))
tesla_model3mo = pickle.load(open("modelForTesla3Months.pkl", rb))

#models for 6 months
# apple_model3mo = pickle.load(open("modelForTesla3Months.pkl", rb))
gm_model6mo = pickle.load(open("modelForGM6moths.pkl", rb))
google_model6mo = pickle.load(open("modelForGoogle6months.pkl", rb))
meta_model6mo = pickle.load(open("modelForMeta6months.pkl", rb))
tesla_model6mo = pickle.load(open("modelForTesla6months.pkl", rb))

#models for 9 months


# Load the input data from a csv file
tesla_data1 = pd.read_csv("Tesla dataset for 1day.csv")
tesla_data1.set_index('Date')
meta_data1 = pd.read_csv("Meta dataframe for 1day.csv")
meta_data1.set_index('Date')
google_data1 = pd.read_csv("Google dataframe for 1day.csv")
google_data1.set_index('Date')
gm_data1 = pd.read_csv("Gm dataset for 1day.csv")
gm_data1.set_index('Date')
apple_data1 = pd.read_csv("apple dataframe for 1day.csv")
apple_data1.set_index('Date')

#dataframes for 1week
apple_data1wk = pd.read_csv("apple1wkDataframe.csv")
apple_data1wk.set_index('Date')
gm_data1wk = pd.read_csv("aGeneralMotors1wkDataFrame.csv")
gm_data1wk.set_index('Date')
google_data1wk = pd.read_csv("google1wkDataframe.csv")
google_data1wk.set_index('Date')
meta_data1wk = pd.read_csv("meta1wkDataFrame.csv")
meta_data1wk.set_index('Date')
tesla_data1wk = pd.read_csv("tesla1wkDataFrame.csv")
tesla_data1wk.set_index('Date')

#datasets for 2weeks
apple_data2wk = pd.read_csv("Apple Dataframe for 2 weeks.csv")
apple_data2wk.set_index('Date')
gm_data2wk = pd.read_csv("GM dataset for2weeks.csv")
gm_data2wk.set_index('Date')
google_data2wk = pd.read_csv("GoogleDataFrame2weeks.csv")
google_data2wk.set_index('Date')
meta_data2wk = pd.read_csv("Meta DataFrame for 2 weeks.csv")
meta_data2wk.set_index('Date')
tesla_data2wk = pd.read_csv("TeslaDataFrameFor2week.csv")
tesla_data2wk.set_index('Date')

#datasets for 3weeks
apple_data3wk = pd.read_csv("Apple Dataframe for 3 weeks.csv")
apple_data3wk.set_index('Date')
gm_data3wk = pd.read_csv("GM dtaframe for 3 weeks.csv")
gm_data3wk.set_index('Date')
google_data3wk = pd.read_csv("Google dataframe for 3 weeks.csv")
google_data3wk.set_index('Date')
meta_data3wk = pd.read_csv("Meta dataFrame for 3 weeks.csv")
meta_data3wk.set_index('Date')
tesla_data3wk = pd.read_csv("Tesla dataframe for 3 weeks.csv")
tesla_data3wk.set_index('Date')

#datsets for 1month
apple_data1mo = pd.read_csv("Apple datset for 1 month.csv")
apple_data1mo.set_index('Date')
gm_data1mo = pd.read_csv("GM dataset for 1 month.csv")
gm_data1mo.set_index('Date')
google_data1mo = pd.read_csv("Gogole dataset for 1month.csv")
google_data1mo.set_index('Date')
# meta_data1mo = pd.read_csv("Apple Dataframe for 3 weeks.csv")
# meta_data1mo.set_index('Date')
tesla_data1mo = pd.read_csv("Tesla dataset for 1 month.csv")
tesla_data1mo.set_index('Date')

#datasets for 3months
apple_data3mo = pd.read_csv("apple dataFrame for 3 months.csv")
apple_data3mo.set_index('Date')
gm_data3mo = pd.read_csv("GM dataset for 3months.csv")
gm_data3mo.set_index('Date')
google_data3mo = pd.read_csv("google dataset for 3 months.csv")
google_data3mo.set_index('Date')
meta_data3mo = pd.read_csv("meta DataFrame for 3 months.csv")
meta_data3mo.set_index('Date')
tesla_data3mo = pd.read_csv("Tesla dataframe for 3 months.csv")
tesla_data3mo.set_index('Date')

#datasets for 6months
# apple_data6mo = pd.read_csv("apple dataFrame for 3 months.csv")
# apple_data6mo.set_index('Date')
gm_data6mo = pd.read_csv("GM dataset for 6months.csv")
gm_data6mo.set_index('Date')
google_data6mo = pd.read_csv("Google dataset for 6months.csv")
google_data6mo.set_index('Date')
meta_data6mo = pd.read_csv("meta dataset for 6 months.csv")
meta_data6mo.set_index('Date')
tesla_data6mo = pd.read_csv("Tesla dataset for 6months.csv")
tesla_data6mo.set_index('Date')


# Define a route for processing the user input and making a prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input from the form
    data = request.get_json()
    user_input = data['user_input']
    target_url = data['target_url']
    # user_input = request.form['input']

    # Determine which model to use based on the user input
    if user_input == 'tesla_model':
        model = tesla_model1
        prediction = model.predict(tesla_data1[new_predictors])
    elif user_input == 'meta_model':
        model = meta_model1
        prediction = model.predict(meta_data1[new_predictors])
    elif user_input == 'google_model':
        model = google_model1
        prediction = model.predict(google_data1[new_predictors])
    elif user_input == 'gm_modle':
        model = gm_modle1
        prediction = model.predict(gm_data1[new_predictors])
    elif user_input == 'apple_modle':
        model = apple_modle1
        prediction = model.predict(apple_data1[new_predictors])
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
