import pandas as pd

df = pd.read_csv('data.csv')
df = pd.get_dummies(df, columns=['Sex'], drop_first=True)

df.to_csv('data.csv', index=False)
print("✅ Applied one-hot encoding to Sex column")