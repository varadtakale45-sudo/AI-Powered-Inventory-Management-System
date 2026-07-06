# AI Smart Inventory Management System

An intelligent inventory management system that combines a **Flask** web application with a **TensorFlow** machine learning model to predict future product demand and automate restocking recommendations.

---

##  Overview

Traditional inventory systems rely on manual decision-making, making it hard to estimate future demand accurately. This project solves that by using AI to analyze historical sales data and forecast demand — reducing overstocking, understocking, and storage costs.

---

## Features

- Full **CRUD** operations for product management
- Lightweight **JSON**-based database
- **TensorFlow** neural network for demand forecasting
- Automatic **restock recommendations**
- **Flask** web interface — beginner-friendly and easy to use
- Modular code structure

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Machine Learning | TensorFlow |
| Database | JSON |
| Frontend | HTML, CSS, JavaScript |

---

## Project Structure

```
AI-Smart-Inventory/
│
├── app.py                  # Flask application entry point
├── train_model.py          # Model training script
├── predict.py              # Demand prediction script
├── preprocess.py           # Data preprocessing script
├── products.json           # JSON-based product database
├── inventory_model.keras   # Saved TensorFlow model
├── requirements.txt        # Python dependencies
└── templates/              # HTML templates
```

---

## System Workflow

```
User Input
    ↓
Add / Update Product
    ↓
products.json
    ↓
preprocess.py  →  Training Dataset
    ↓
train_model.py  →  TensorFlow Model
    ↓
inventory_model.keras
    ↓
predict.py  →  Demand Prediction
    ↓
Inventory Dashboard
```

---

## AI Methodology

The machine learning pipeline consists of the following stages:

1. **Data Collection** — Historical sales data per product stored in JSON
2. **Data Preprocessing** — Sales history converted into input-output pairs
3. **Model Training** — A feedforward neural network trained on the processed data
4. **Model Saving** — Trained model saved as `inventory_model.keras`
5. **Prediction** — Model predicts next week's demand from recent sales
6. **Decision Making** — Predicted demand vs. available stock triggers restock alerts

**Example:**

| Sales History | Predicted Demand |
|---|---|
| 12, 15, 18, 20, 22, 25 | **28 Units** |

---

## CRUD Operations

| Operation | Description |
|---|---|
| **Create** | Add new products to the inventory |
| **Read** | Display all inventory items on the dashboard |
| **Update** | Modify stock quantity and log new weekly sales |
| **Delete** | Remove products from inventory |

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/AI-Smart-Inventory.git
cd AI-Smart-Inventory
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Train the AI model**
```bash
python train_model.py
```

**4. Run the application**
```bash
python app.py
```

**5. Open your browser and visit**
```
http://127.0.0.1:5000
```

---

## Example Workflow

1. Add a product with stock quantity and sales history
2. Train the TensorFlow model
3. Open the inventory dashboard
4. AI predicts future demand
5. Update weekly sales as they occur
6. AI generates a new demand prediction
7. Restock products when recommended

---

## Skills Demonstrated

- Python Programming
- Flask Web Development
- TensorFlow Machine Learning
- Data Preprocessing
- JSON Data Handling
- CRUD Operations
- AI Model Deployment
- HTML / CSS / JavaScript
- Inventory Management Concepts

---

## Future Scope

- SQLite / MySQL database integration
- Barcode and QR code scanning
- User authentication
- Cloud deployment
- Email notifications for restock alerts
- Sales analytics dashboard
- Multiple warehouse support
- Product image upload
- LSTM model for improved time-series forecasting

---

## License

This project is licensed under the **MIT License**.

```