import pandas as pd

df = pd.read_csv('data.csv')
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

df.to_csv('data.csv', index=False)
print(f"✅ Missing ages filled with mean: {mean_age}")
