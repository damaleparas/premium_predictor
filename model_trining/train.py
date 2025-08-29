import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_csv("insurance.csv")

X = data[["age","sex","bmi","children","smoker","region"]]
Y = data["charges"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

model = RandomForestRegressor(n_estimators=100,random_state=42,n_jobs=-1)

model.fit(X_train,y_train)
y_pred = model.predict(X_test)


with open('rf_model_1.pkl', 'wb') as file:
    pickle.dump(model, file)

