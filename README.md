# Customer Churn Prediction using Machine Learning

## 📌 Project Overview

Customer churn prediction helps businesses identify customers who are likely to stop using their services.
This project uses machine learning to predict whether a customer will churn based on different features such as tenure, monthly charges, total charges, and other customer attributes.

The model is deployed using a backend API built with Flask, allowing predictions to be generated from user input through a web interface.

---

## 🚀 Features

* Predicts whether a customer will churn or not
* Machine learning model trained on churn dataset
* Backend API built using Flask
* User-friendly web interface
* End-to-end machine learning deployment project

---

## 🧠 Machine Learning Model

The model is trained using supervised learning techniques from the field of Machine Learning.

Steps involved:

* Data preprocessing
* Feature encoding
* Model training
* Model evaluation
* Model deployment

The trained model is saved and loaded during prediction.

---

## 🛠 Technologies Used

* Python
* Pandas
* Scikit-learn
* Flask
* HTML, CSS, JavaScript
* Joblib

---

## 📂 Project Structure

```
customer-churn-prediction
│
├── app.py                     # Flask backend API
├── Tel_Churn.csv              # Processed dataset used for training
├── Original_Dataset.csv       # Original raw dataset
├── model.sav                  # Trained machine learning model
├── columns.pkl                # Feature columns used during training
├── index.html                 # Frontend UI
├── Procfile                   # Deployment configuration
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation

```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/customer-churn-prediction.git
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Application

```
python app.py
```

The application will start on:

```
http://127.0.0.1:8000
```

---

## 🔮 How Prediction Works

1. User enters customer details in the UI
2. Data is sent to the Flask API
3. The trained model processes the input
4. The API returns the churn prediction
5. Result is displayed to the user

---

## 📊 Dataset

The model was trained using a customer churn dataset containing customer service information such as tenure, billing details, and service usage.

---

## 🎯 Future Improvements

* Add more advanced models
* Improve UI design
* Deploy the application on a cloud platform
* Add data visualization dashboard

---

## 👩‍💻 Author

**Anshika Sahu**
B.Tech AIML Student
Kalinga University
