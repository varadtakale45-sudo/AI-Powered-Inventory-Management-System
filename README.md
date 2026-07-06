# AI-Powered Inventory Management System

An intelligent inventory management system built with **Python, Flask, and TensorFlow** that predicts future product demand using machine learning and provides smart restocking recommendations. The application enables businesses to efficiently manage inventory through a user-friendly web interface with complete CRUD functionality.

---

## 🚀 Features

- Add, update, delete, and manage products
- Search products by name
- AI-powered demand prediction using TensorFlow
- Automatic stock status analysis
- Smart restock recommendations
- JSON-based data storage
- Responsive Flask web application
- Beginner-friendly project structure

---

## 🛠 Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Python
- Flask

**Machine Learning**
- TensorFlow / Keras

**Database**
- JSON

---

## 📂 Project Structure

```
AI-Powered Inventory Management System/
│
├── app.py                    # Flask application
├── train_model.py            # Train AI model
├── predict.py                # Demand prediction
├── preprocess.py             # Data preprocessing
├── model.py                  # Model architecture
├── inventory_model.keras     # Trained model
├── products.json             # Inventory database
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## ⚙️ How It Works

1. Add products with stock details and sales history.
2. Store inventory data in a JSON database.
3. Preprocess historical sales data.
4. Train a TensorFlow model.
5. Predict future product demand.
6. Compare predicted demand with available stock.
7. Display intelligent restocking recommendations.

---

## 🧠 Machine Learning Pipeline

```
Sales Data
      │
      ▼
Data Preprocessing
      │
      ▼
TensorFlow Model Training
      │
      ▼
Saved Keras Model
      │
      ▼
Demand Prediction
      │
      ▼
Restock Recommendation
```

---

## 📊 Functionalities

- Product Management (CRUD)
- Inventory Dashboard
- Sales Tracking
- Demand Prediction
- Stock Monitoring
- Search Products
- Restock Alerts

---

## 💻 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-Powered-Inventory-Management-System.git
cd AI-Powered-Inventory-Management-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train the model

```bash
python train_model.py
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Project Workflow

```
User
   │
   ▼
Inventory Dashboard
   │
   ▼
Add / Update Products
   │
   ▼
Store Data (JSON)
   │
   ▼
AI Prediction Model
   │
   ▼
Demand Forecast
   │
   ▼
Stock Analysis
   │
   ▼
Restock Recommendation
```

---

## 🎯 Skills Demonstrated

- Python Programming
- Flask Development
- TensorFlow
- Machine Learning
- Data Preprocessing
- CRUD Operations
- Inventory Management
- Web Development
- AI Integration

---

## 🔮 Future Improvements

- SQLite/MySQL database
- User authentication
- Barcode/QR code support
- Product image upload
- Sales analytics dashboard
- Email notifications
- Cloud deployment
- Multi-user access
- Multi-warehouse management
- LSTM-based forecasting

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star!
