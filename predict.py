import numpy as np
from tensorflow.keras.models import load_model

model = load_model("inventory_model.keras")


def predict_next_sale(last_sale):

    prediction = model.predict(
        np.array([[last_sale]]),
        verbose=0
    )

    return round(float(prediction[0][0]), 2)