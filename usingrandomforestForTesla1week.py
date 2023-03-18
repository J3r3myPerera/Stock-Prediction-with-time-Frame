# -*- coding: utf-8 -*-
"""UsingRandomForest for Tesla 1week.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ImPksfGi_nZNm5-4Vhy5uK5Ae6M0bl81
"""

#installing the yfinance
!pip install yfinance

#import yfinance
import yfinance as yf

#Getting the data set from yfinance
df = yf.download('TSLA', start ='2010-06-29', interval = '1wk')
df

#checking the index
df.index

#Visualizing the data
import matplotlib.pyplot as plt
plt.style.use('bmh')
plt.figure(figsize=(16,8))
plt.title('Tesla Stock Price')
plt.xlabel('Year')
plt.ylabel('Close price USD($)')
plt.plot(df['Close'])
plt.show()
#df.plot.line(y="Close", use_index=True)

#Remving the columns of the dividends and the stock spilts as we dont need them 
 #del df["Dividends"]
 #del df["Stock Splits"]

#Shifting the data and making a new column to show tomorrows price
df["weekAgo"] = df["Close"].shift(-1) 
df

#If the opeing price of the day after was higher than the prevois date show it in the target as 1 or 0
df["Target"] = (df["weekAgo"] > df["Close"]).astype(int)
df

length = len(df.index)
train_len = length * 0.7
print(train_len)
test_len = length * 0.3
print(test_len)

#Building the model with the random forest
 from sklearn.ensemble import RandomForestClassifier
#Changing hte estimators and the samples to check the precision score
 model = RandomForestClassifier(n_estimators=200, min_samples_split=100, random_state=1)
 train = df.iloc[:-199] 
 test = df.iloc[-199:]
 predictors = ["Close", "Volume", "Open", "High", "Low"]
 model.fit(train[predictors], train["Target"])

#Taking the precision score
 from sklearn.metrics import precision_score
 preds = model.predict(test[predictors])
 preds

test[predictors]

#Time series
import pandas as pd
preds = pd.Series(preds, index=test.index)
preds

#Checking on the precision score
precision_score(test["Target"], preds)
#for n_estimators=200, min_samples_split=100, random_state=1: 0.5692307692307692

test["Target"].value_counts()

#preparing to plot the data
combined = pd.concat([test["Target"], preds], axis = 1)

combined.plot()

print(test[predictors])

print(train[predictors])

#Creating a training model 
def predict(train, test, predictors, model):
  model.fit(train[predictors], train["Target"])
  preds = model.predict(test[predictors])
  preds = pd.Series(preds, index=test.index, name="Predictions")
  combined = pd.concat([test["Target"], preds], axis = 1)
  return combined

#df = df.dropna

#df

#Building the backtesting model
def backtest(data, model, predictors, start=250, step=21):#training the model for a year and then moving forward from year to year
  all_predictions =[]

  for i in range(start, data.shape[0], step):
    train = data.iloc[0:i].copy()
    test = data.iloc[i:(i+step)].copy()
    predictions = predict(train, test, predictors, model)
    all_predictions.append(predictions)
  return pd.concat(all_predictions)

#Build up the predictions using the backtesting
predictions = backtest(df, model, predictors)
#predictions = model.predict(df)

#Checking on what was the prediction that the market went up or down
predictions["Predictions"].value_counts()

predictions["Predictions"].value_counts()/ predictions.shape[0]

#Checking the precision score on how the modle performed
precision_score(predictions["Target"], predictions["Predictions"])
#(data, model, predictors, start=250, step=21): 0.5129174543163201

#Checking on how actaully how the model performed on the days that we were predicting
predictions["Target"].value_counts()/ predictions.shape[0]

print(predictions["Predictions"])

horizons = [5,21,48,63,250] #Mean close price for a number of days, starting from 2 days behind upuntil one year
new_predictors = []

for horizon in horizons:
  rolling_averages = df.rolling(horizon).mean()#calculate the rolling avarage on the above

  ratio_column = f"Close_Ratio_{horizon}"
  df[ratio_column] = df["Close"] / rolling_averages["Close"]

  trend_column = f"Trend_{horizon}"#Looking a trend on how the stock performed 
  df[trend_column] = df.shift(1).rolling(horizon).sum()["Target"]

  new_predictors += [ratio_column, trend_column]

df

#get rid of the columns with no values 
df = df.dropna()
df

model = RandomForestClassifier(n_estimators=250, min_samples_split=50, random_state=1)

def predict(train, test, predictors, model):
  model.fit(train[predictors], train["Target"])
  preds = model.predict_proba(test[predictors])[:,1]#change it to a probability so that it will return if its a one or a zero
  preds[preds >=.6] = 1 #If there's a probabilty of 60% that the price will go up it will return a 1
  preds[preds < .6] = 0 #If there's a probabitlity less than 60% the price will go down it will return a zero
  preds = pd.Series(preds, index=test.index, name="Predictions")
  combined = pd.concat([test["Target"], preds], axis = 1)
  return combined

predictions = backtest(df, model, new_predictors)

df[new_predictors]

predictions

#Checking on the value counts
predictions["Predictions"].value_counts()

precision_score(predictions["Target"], predictions["Predictions"])

#Checking on how actaully how the model performed on the days that we were predicting
predictions["Target"].value_counts()/ predictions.shape[0]

predictions

import pickle

pickle.dump(model,open('UsingRandomForest.pkl','wb'))

model = pickle.load(open('UsingRandomForest.pkl','rb'))
preds = model.predict(df[new_predictors])
preds

new_predictors

df[new_predictors]

#Storing the new dataset
df.to_csv('my_data.csv', index = True)

