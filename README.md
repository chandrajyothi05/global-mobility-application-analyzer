# 🌍 Global Mobility Application Analyzer (Visa Approval Prediction System)

An end-to-end **Machine Learning and MLOps project** that predicts whether a visa application is likely to be **Certified** or **Denied** using historical immigration application data.

The project integrates **Machine Learning, MLOps, Cloud Deployment, CI/CD Automation, and FastAPI** to deliver a production-ready visa approval prediction system capable of making real-time predictions.

---

## 📌 Project Overview

Visa approval decisions depend on several applicant and employer-related factors, including:

* Education Level
* Work Experience
* Prevailing Wage
* Company Size
* Company Age
* Region of Employment
* Job Training Requirements
* Employment Type

Manually evaluating thousands of visa applications can be time-consuming and difficult to scale. This project leverages Machine Learning to automate the screening process and provide accurate, real-time visa approval predictions through a web application.

---

## 🎯 Objectives

* Predict whether a visa application will be **Certified** or **Denied**
* Automate the visa application screening process
* Build a complete ML pipeline from data ingestion to deployment
* Implement MLOps practices for monitoring and model management
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

### Dataset Source

* EasyVisa Dataset (Kaggle)

### Dataset Information

* **Total Records:** 25,480
* **Features:** 12
* **Target Variable:** Case Status

#### Target Classes

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
* Full-Time Position
* Year of Establishment

---

## 🔄 End-to-End Workflow

```text
Historical Visa Data
        ↓
Data Ingestion (MongoDB)
        ↓
Data Validation
        ↓
Data Drift Detection
        ↓
Feature Engineering
        ↓
Data Transformation
        ↓
Model Training
        ↓
Hyperparameter Tuning
        ↓
Model Evaluation
        ↓
Model Pusher
        ↓
AWS S3 Model Storage
        ↓
FastAPI Deployment
        ↓
Real-Time Predictions
```

---

## ⚙️ Feature Engineering

The following preprocessing and feature engineering techniques were implemented:

* Missing Value Handling
* Duplicate Removal
* Categorical Encoding
* Feature Scaling
* Company Age Feature Creation
* Yeo-Johnson Power Transformation
* Class Imbalance Handling using SMOTE-ENN
* Automated Transformation Pipelines using ColumnTransformer

---

## 🤖 Models Trained

The following machine learning models were trained and evaluated:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* AdaBoost Classifier
* Gradient Boosting Classifier
* K-Nearest Neighbors (KNN)
* Support Vector Classifier (SVC)
* XGBoost Classifier
* CatBoost Classifier

### Hyperparameter Tuning

* GridSearchCV
* 3-Fold Cross Validation

---

## 🏆 Best Performing Model

### K-Nearest Neighbors (KNN)

| Metric   | Score  |
| -------- | ------ |
| Accuracy | 94.53% |

### Performance Highlights

* High Precision
* High Recall
* Strong Classification Performance
* Effective distinction between Certified and Denied applications

---

## ☁️ AWS & MLOps Architecture

### AWS S3

Used for:

* Model Storage
* Artifact Storage
* Model Versioning
* Production Model Management

### CI/CD Pipeline

Implemented using:

* GitHub Actions
* Docker
* AWS ECR
* AWS EC2

### Deployment Workflow

```text
Developer Pushes Code
          ↓
GitHub Actions Triggered
          ↓
Docker Image Built
          ↓
Image Pushed to AWS ECR
          ↓
EC2 Pulls Latest Image
          ↓
Application Redeployed
```

---

## 🌐 FastAPI Web Application

The application allows users to:

* Enter visa application details
* Submit applicant information
* Receive real-time visa approval predictions
* Trigger model retraining directly from the UI

### Prediction Flow

```text
User Input
     ↓
Prediction Pipeline
     ↓
Trained Model
     ↓
Approval Prediction
```

### Output

* ✅ Visa Approved
* ❌ Visa Not Approved

---

## 🏗️ System Architecture
###System Architecture Diagram
<img width="1619" height="972" alt="image" src="https://github.com/user-attachments/assets/b30116df-b5ae-43f6-94ea-c028c3d5d6db" />

```text
MongoDB
   ↓
Data Ingestion
   ↓
Data Validation
   ↓
Data Drift Detection
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

<img width="1600" height="593" alt="image" src="https://github.com/user-attachments/assets/e148305a-1317-4c9b-a544-3673ecb3ad6b" />
<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/62d2384e-4a87-4e92-a5c0-07687f47192e" />
<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/7a7249d4-c0c8-4d94-917f-8d529734a1b5" />
<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/79efe9b2-9caf-42f4-89ac-2bcc014ea243" />
<img width="1600" height="634" alt="image" src="https://github.com/user-attachments/assets/74a59112-42be-4809-a892-3423ef5f39e5" />
<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/448b6e98-c1f1-46ad-946f-02d4f13a906f" />
<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/cbe8773c-a571-4d8f-a037-88e5fa091a09" />
<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/52cb64f6-9780-4f65-85cc-f253aff4776c" />
<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/a485fbe4-4815-488d-a33a-1e532fe3cd8a" />


---

## 🚧 Challenges Faced

During development and deployment, several challenges were encountered:

* Handling class imbalance using SMOTE-ENN
* Schema validation failures during data validation
* NumPy 2.0 compatibility issues with Evidently AI
* AWS S3 integration and artifact upload errors
* Docker configuration and deployment issues
* AWS credentials and environment variable management
* CI/CD pipeline debugging and automation challenges

---

## 📈 Project Outcomes

* Successfully built a complete Visa Approval Prediction System
* Developed an end-to-end Machine Learning pipeline
* Implemented industry-level MLOps workflows
* Automated training, evaluation, deployment, and monitoring
* Deployed the application on AWS Cloud
* Achieved high prediction performance using KNN
* Enabled scalable and real-time visa approval predictions

---

## 👨‍💻 Team Members

### 👤 Fidha Manaph

**Machine Learning Intern**

### 👤 Chandrajyothi Parambi Biju

**Machine Learning Intern**

---

## ⭐ Acknowledgements

This project was developed as part of a Machine Learning internship, with a focus on applying real-world MLOps practices, cloud deployment, CI/CD automation, and production-ready machine learning workflows.

We would like to express our sincere gratitude to Skoliko for providing us with the opportunity to work on this project and for guiding us throughout the internship. The mentorship, technical support, and industry exposure provided by the Skoliko team played a significant role in helping us successfully design, develop, and deploy this end-to-end machine learning solution.

---

### 🔗 Repository Structure

```text
├── artifact/
├── config/
├── logs/
├── notebooks/
├── src/
├── templates/
├── static/
├── .github/workflows/
├── Dockerfile
├── requirements.txt
├── app.py
├── main.py
└── README.md
```

to run:
1. clone repo:
```bash
git clone https://github.com/fidhamanaph/Global-Mobility-Application-Analyzer
```

2. navigate to project:
```bash
cd Global-Mobility-Application-Analyzer/
```

3. create and activate virtual environment:
```bash
conda create -n application python=3.8 -y
conda activate application 
```

4. install required dependencies:
```bash
pip install -r requirements.txt
```

##export the environment variable
```bash
export MONGODB_URL="mongodb+srv://fidhamanaph:imthiyaz1@cluster0.9ounu25.mongodb.net/?appName=Cluster0"

GIT export AWS_ACCESS_KEY=<AWS_ACCESS_KEY_ID>

export
AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY_ID>

529845836660.dkr.ecr.us-east-1.amazonaws.com/visarepo
```

