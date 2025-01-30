import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
import os

# Загружаем модель
model = joblib.load('trained_model.pkl')

# Проверяем модель на всех файлах в папке test
for filename in os.listdir('data/test'):
    if filename.endswith('.csv'):
        file_path = os.path.join('data/test', filename)
        data = pd.read_csv(file_path)
        X = data[['x']]
        y_true = data['y']
        y_pred = model.predict(X)
        mse = mean_squared_error(y_true, y_pred)
        print(f"File: {filename}, MSE: {mse}")

print("Model testing completed.")