import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data[['x', 'y']])
    data[['x', 'y']] = data_scaled
    return data

# Обрабатываем все файлы в папке train
for filename in os.listdir('train'):
    if filename.endswith('.csv'):
        file_path = os.path.join('train', filename)
        processed_data = preprocess_data(file_path)
        processed_data.to_csv(file_path, index=False)

# Обрабатываем все файлы в папке test
for filename in os.listdir('test'):
    if filename.endswith('.csv'):
        file_path = os.path.join('test', filename)
        processed_data = preprocess_data(file_path)
        processed_data.to_csv(file_path, index=False)

print("Data preprocessing completed.")