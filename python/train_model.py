import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("temperature_data.csv")
X, y = data[['temp']], data['label']
model = LogisticRegression().fit(X, y)
joblib.dump(model, '../models/ml_model.pkl')
