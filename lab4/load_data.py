import catboost.datasets
import pandas as pd

# Загружаем датасет
train_df, _ = catboost.datasets.titanic()

# Сохраняем только нужные колонки
df = train_df[['Pclass', 'Sex', 'Age']]

# Сохраняем
df.to_csv('data.csv', index=False)
print("Data saved to data.csv")