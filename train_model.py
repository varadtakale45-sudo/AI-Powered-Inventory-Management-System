from preprocess import load_data

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

X, y = load_data()

model = Sequential()

model.add(Dense(32, activation="relu", input_shape=(1,)))
model.add(Dense(16, activation="relu"))
model.add(Dense(1))

model.compile(
    optimizer="adam",
    loss="mse"
)

model.fit(
    X,
    y,
    epochs=300,
    verbose=1
)

model.save("inventory_model.keras")

print("Model trained successfully!")