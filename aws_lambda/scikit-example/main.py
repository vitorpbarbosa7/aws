from statistics import mean
from venv import create
from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
import joblib
import time

data = pd.read_parquet('data/data.parquet')

data = data.sample(frac = 0.3)

X = data.drop('target', axis = 1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)

def create_model():
    model = Pipeline([
        ('scaler',StandardScaler()),
        ('feature_selector', SelectKBest(score_func=f_regression, k=8)),
        ('regressor', SVR(C=10, epsilon=0.1, gamma=1.0, kernel='rbf'))
    ])

    return model

model = create_model()

print('start first training')
model.fit(X_train, y_train)

y_pred_test = model.predict(X_test)
print(mean_squared_error(y_test, y_pred_test))

print('train on all dataset')
all_data_model = create_model()

all_data_model.fit(X, y)

joblib.dump(all_data_model, 'models/all_data_model.pkl')