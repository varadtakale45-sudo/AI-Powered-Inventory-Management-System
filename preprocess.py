import json
import numpy as np

FILE = "products.json"


def load_data():
    with open(FILE, "r") as f:
        products = json.load(f)

    X = []
    y = []

    for product in products:

        history = product["sales_history"]

        for i in range(len(history) - 1):
            X.append([history[i]])
            y.append(history[i + 1])

    return np.array(X), np.array(y)