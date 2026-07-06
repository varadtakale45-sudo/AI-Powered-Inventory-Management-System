import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


X = np.array([
    [100, 20],
    [80, 15],
    [60, 12],
    [50, 10],
    [40, 8],
    [30, 6],
    [20, 5],
    [15, 4],
    [10, 3],
    [5, 2]
], dtype=float)

# Expected Demand
y = np.array([
    22,
    17,
    14,
    12,
    10,
    8,
    6,
    5,
    4,
    3
], dtype=float)


model = Sequential([
    Dense(8, activation="relu", input_shape=(2,)),
    Dense(8, activation="relu"),
    Dense(1)
])

model.compile(
    optimizer="adam",
    loss="mse"
)

# Train the model
model.fit(
    X,
    y,
    epochs=300,
    verbose=0
)


def predict_demand(stock, sales):
    data = np.array([[stock, sales]], dtype=float)

    prediction = model.predict(
        data,
        verbose=0
    )[0][0]

    prediction = max(1, int(round(prediction)))

    return prediction