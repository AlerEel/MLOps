import numpy as np
import pandas as pd
import os

# Создаем директории для хранения данных
os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)

def create_data(n_samples=100, noise=False):
    x = np.linspace(0, 10, n_samples)
    y = np.sin(x) + np.random.normal(0, 0.1, n_samples) if noise else np.sin(x)
    return pd.DataFrame({'x': x, 'y': y})

# Создаем тренировочные данные
train_data_normal = create_data(n_samples=100, noise=False)
train_data_noise = create_data(n_samples=100, noise=True)
train_data_normal.to_csv('train/train_normal.csv', index=False)
train_data_noise.to_csv('train/train_noise.csv', index=False)

# Создаем тестовые данные
test_data_normal = create_data(n_samples=50, noise=False)
test_data_noise = create_data(n_samples=50, noise=True)
test_data_normal.to_csv('test/test_normal.csv', index=False)
test_data_noise.to_csv('test/test_noise.csv', index=False)

print("Data creation completed.")