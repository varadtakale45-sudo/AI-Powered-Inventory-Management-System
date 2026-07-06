from flask import Flask, render_template, request, redirect
import json
import os
from predict import predict_next_sale

app = Flask(__name__)

FILE = "products.json"

def load_products():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_products(products):
    with open(FILE, "w") as f:
        json.dump(products, f, indent=4)

@app.route("/")
def home():

    products = load_products()

    search = request.args.get("search")

    if search:
        products = [
            p for p in products
            if search.lower() in p["name"].lower()
        ]

    for product in products:

        last_sale = product["sales_history"][-1]

        prediction = predict_next_sale(last_sale)

        product["last_sale"] = last_sale
        product["prediction"] = prediction

        if product["stock"] < prediction:
            product["status"] = "Restock Needed"
        else:
            product["status"] = "Stock OK"

    return render_template(
        "index.html",
        products=products
    )

@app.route("/add", methods=["POST"])
def add():

    products = load_products()

    new_sale = int(request.form["sales"])

    new_product = {
        "id": len(products) + 1,
        "name": request.form["name"],
        "category": request.form["category"],
        "stock": int(request.form["stock"]),
        "price": float(request.form["price"]),
        "sales_history": [new_sale]
    }

    products.append(new_product)

    save_products(products)

    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):

    products = load_products()

    products = [p for p in products if p["id"] != id]

    save_products(products)

    return redirect("/")

@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    products = load_products()

    for product in products:

        if product["id"] == id:

            product["name"] = request.form["name"]
            product["category"] = request.form["category"]
            product["stock"] = int(request.form["stock"])
            product["price"] = float(request.form["price"])

            new_sale = int(request.form["sales"])

            product["sales_history"].append(new_sale)

            break

    save_products(products)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)