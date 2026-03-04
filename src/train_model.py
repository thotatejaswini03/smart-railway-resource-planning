import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("data/railway_data.csv")

# Feature engineering
df["Date"] = pd.to_datetime(df["Date"])
df["day_of_week"] = df["Date"].dt.dayofweek
df["month"] = df["Date"].dt.month

df["route"] = df["Source"] + "_" + df["Destination"]
df["route_encoded"] = df["route"].astype("category").cat.codes

X = df[["day_of_week","month","route_encoded","Holiday"]]
y = df["Passenger_Count"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = RandomForestRegressor()

model.fit(X_train,y_train)

joblib.dump(model,"models/demand_model.pkl")

print("Model trained and saved")