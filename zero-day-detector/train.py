import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

data = pd.read_csv("data/normal_traffic.csv")
features = data[["length", "proto", "ttl", "entropy"]]

model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
model.fit(features)

with open("models/zero_day_model.pkl", "wb") as f:
    pickle.dump(model, f)
