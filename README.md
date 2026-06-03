# 🌍 Global Mobility Application Analyzer (Visa Approval Prediction System)

An end-to-end Machine Learning and MLOps project that predicts whether a visa application is likely to be **Certified** or **Denied** using historical immigration application data.

The project combines **Machine Learning, MLOps, Cloud Deployment, CI/CD Automation, and FastAPI** to build a production-ready visa approval prediction system.

---

## 📌 Project Overview

Visa approval decisions depend on multiple applicant and employer-related factors such as:

* Education Level
* Work Experience
* Prevailing Wage
* Company Size
* Company Age
* Region of Employment
* Job Training Requirements
* Employment Type

Manually evaluating large numbers of visa applications can be time-consuming and difficult to scale.

This project leverages Machine Learning to automate the prediction process and provide real-time visa approval predictions through a web application.

---

## 🎯 Objectives

* Predict whether a visa application will be **Certified** or **Denied**
* Automate visa application screening
* Build a complete ML pipeline from data ingestion to deployment
* Implement MLOps practices for model monitoring and deployment
* Deploy the application on AWS Cloud
* Enable real-time predictions through a FastAPI web application

---

## 🛠️ Technologies Used

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* CatBoost

### MLOps

* Evidently AI
* Docker
* GitHub Actions
* AWS S3
* AWS EC2
* AWS ECR

### Database

* MongoDB
* PyMongo

### Deployment

* FastAPI
* Uvicorn

### Cloud Services

* Amazon S3
* Amazon EC2
* Amazon ECR

---

## 📊 Dataset

**Dataset Source:**

[EasyVisa Dataset (Kaggle)](https://www.kaggle.com/datasets/moro23/easyvisa-dataset?utm_source=chatgpt.com)

### Dataset Information

* Total Records: **25,480**
* Features: **12**
* Target Variable: **Case Status**

  * Certified
  * Denied

### Key Features

* Continent
* Education of Employee
* Has Job Experience
* Requires Job Training
* Number of Employees
* Region of Employment
* Prevailing Wage
* Unit of Wage
* Full Time Position
* Year of Establishment

---

## 🔄 End-to-End Workflow

1. Historical Visa Data Collection
2. Data Ingestion from MongoDB
3. Exploratory Data Analysis (EDA)
4. Data Validation
5. Data Drift Detection using Evidently AI
6. Data Preprocessing
7. Feature Engineering
8. Data Transformation Pipeline
9. Model Training
10. Hyperparameter Tuning
11. Model Evaluation
12. Model Pusher
13. AWS S3 Model Storage
14. FastAPI Deployment
15. Real-Time Prediction Pipeline

---

## ⚙️ Feature Engineering

The following preprocessing and feature engineering techniques were implemented:

* Missing Value Handling
* Categorical Encoding
* Duplicate Removal
* Feature Scaling
* Company Age Feature Creation
* Yeo-Johnson Power Transformation
* Class Imbalance Handling using SMOTE-ENN
* Automated Transformation Pipelines using ColumnTransformer

---

## 🤖 Models Trained

The following models were trained and evaluated:

* Logistic Regression
* Random Forest Classifier
* AdaBoost Classifier
* Gradient Boosting Classifier
* Decision Tree Classifier
* K-Nearest Neighbors (KNN)
* Support Vector Classifier (SVC)
* XGBoost Classifier
* CatBoost Classifier

### Hyperparameter Tuning

* GridSearchCV
* 3-Fold Cross Validation

---

## 🏆 Best Model

**K-Nearest Neighbors (KNN)**

### Performance

* Accuracy: **94.53%**
* High Precision
* High Recall
* Strong Classification Performance

The model demonstrated excellent performance in distinguishing between certified and denied visa applications.

---

## ☁️ AWS & MLOps Architecture

### AWS S3

Used for:

* Model Storage
* Artifact Storage
* Production Model Management
* Model Versioning

### CI/CD Pipeline

Implemented using:

* GitHub Actions
* Docker
* AWS ECR
* AWS EC2

Deployment Process:

1. Push code to GitHub
2. GitHub Actions triggers workflow
3. Docker image is built
4. Image pushed to AWS ECR
5. EC2 pulls latest image
6. Application redeployed automatically

---

## 🌐 FastAPI Web Application

The web application allows users to:

* Enter visa application details
* Submit applicant information
* Receive real-time visa approval predictions
* Trigger model retraining directly from the UI

### Prediction Flow

User Input → Prediction Pipeline → Trained Model → Approval Prediction

Output:

* Visa Approved
* Visa Not Approved

---

## 🏗️ System Architecture

### System Architecture Diagram

> *(Insert System Architecture Screenshot Here)*

```text
MongoDB
   ↓
Data Ingestion
   ↓
Data Validation
   ↓
Drift Detection
   ↓
Feature Engineering
   ↓
Data Transformation
   ↓
Model Training
   ↓
Model Evaluation
   ↓
AWS S3
   ↓
FastAPI Application
   ↓
User Predictions
```

---

## 📸 Application Screenshots

### User Interface

> *(Insert Home Page Screenshot Here)*

### Prediction Result

> *(Insert Prediction Output Screenshot Here)*

---

## 🚧 Challenges Faced

* Handling class imbalance using SMOTE-ENN
* Schema validation failures during data validation
* NumPy 2.0 compatibility issues with Evidently AI
* AWS S3 integration and model upload errors
* Deployment and Docker configuration issues
* AWS credential and environment variable management
* CI/CD pipeline debugging and automation challenges

---

## 📈 Project Outcomes

* Successfully built a complete Visa Approval Prediction System
* Developed an end-to-end Machine Learning pipeline
* Implemented industry-level MLOps workflows
* Automated training, evaluation, deployment, and monitoring
* Deployed the application on AWS Cloud
* Achieved high prediction performance with KNN
* Enabled scalable and real-time predictions

---

## 👨‍💻 Team Members

### Chandrajyothi Parambi Biju

Machine Learning Intern

### Fidha Manaph

Machine Learning Intern

---

## 📄 License

This project is developed for educational and learning purposes as part of a Machine Learning and MLOps internship project.
