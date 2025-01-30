import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

# Создаем модель и обучаем её на всех файлах в папке train
model = LinearRegression()

for filename in os.listdir('data/train'):
    if filename.endswith('.csv'):
        file_path = os.path.join('data/train', filename)
        data = pd.read_csv(file_path)
        X = data[['x']]
        y = data['y']
        model.fit(X, y)

# Сохраняем модель
joblib.dump(model, 'trained_model.pkl')

print("Model training completed.")