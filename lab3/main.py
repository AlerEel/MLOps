from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Загрузка данных
iris = load_iris()
X, y = iris.data, iris.target

# Разделение данных на тренировочные и тестовые
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Сохранение модели
joblib.dump(model, "iris_model.pkl")

# Проверка точности
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")