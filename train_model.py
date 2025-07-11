import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv('PM2.5.csv')
X = df[['outdoor_pm25', 'air_purifier', 'activity', 'open_window']]
y = df['PM25_exceed']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, 'rf_model.pkl')
print("Model saved!")