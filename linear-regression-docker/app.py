# app.py

from sklearn.linear_model import LinearRegression
import numpy as np

# Example dataset (X = input, y = output)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Make a prediction
prediction = model.predict([[6]])
print(f"Prediction for input 6 is: {prediction[0]}")
