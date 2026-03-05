🧠 AI-Driven Fitness Intelligence System

An AI-powered fitness intelligence platform that predicts body fat percentage using physiological and lifestyle data through machine learning models.

The system analyzes body measurements and activity patterns to generate data-driven body composition insights using advanced regression algorithms.

## 🚀 Live Application

<p align="center">

<a href="https://ai-driven-fitness-intelligence-systemgit-xt9iwnappfn2qmgudqduc.streamlit.app">

<img src="https://img.shields.io/badge/Launch-AI%20Fitness%20Coach-success?style=for-the-badge&logo=streamlit">

</a>

</p>

Use the deployed application to predict body fat percentage in real-time by entering your physiological details.

📊 Project Overview

The AI-Driven Fitness Intelligence System leverages machine learning to estimate body fat percentage using anthropometric measurements and lifestyle indicators.

The platform combines:

Data preprocessing

Feature engineering

Machine learning modeling

Model evaluation

Interactive AI deployment

This system demonstrates how machine learning can transform raw physiological data into actionable fitness insights.

🧠 Machine Learning Models

Two regression models were trained and compared to determine the most effective predictor.

Models Implemented

1️⃣ Multiple Linear Regression

2️⃣ XGBoost Regressor

📈 Model Performance Comparison
Model	R² Score
Multiple Linear Regression	0.9890
XGBoost Regressor	0.9954
Final Model Selection

Although Multiple Linear Regression performed well, XGBoost achieved a higher R² score, capturing nonlinear relationships between body measurements and body fat percentage more effectively.

Therefore, XGBoost was selected as the final production model for deployment.

📂 Dataset

The dataset contains physiological and lifestyle attributes such as:

Age

Height (cm)

Weight (kg)

Waist circumference

Neck circumference

Hip circumference

Sleep hours

Weekly workouts

Daily calorie intake

These attributes are widely used in body composition estimation models and health analytics systems.

⚙️ Machine Learning Pipeline

The project follows a structured ML workflow:

1️⃣ Data Preprocessing

Handling missing values

Outlier treatment

Feature scaling

Encoding categorical variables

2️⃣ Feature Engineering

Selection of physiologically relevant variables

Correlation analysis

3️⃣ Model Training

Multiple Linear Regression

XGBoost Regressor

4️⃣ Model Evaluation

R² Score comparison

Model performance analysis

5️⃣ Deployment

The final trained model is deployed using Streamlit, enabling real-time body fat prediction via an interactive web interface.

🖥️ Web Application

The application allows users to input fitness data and receive instant AI predictions.

User Inputs

Age

Gender

Height

Weight

Activity level

Waist / Neck / Hip measurements

Sleep hours

Workout frequency

Daily calorie intake

Output

✔ Estimated Body Fat Percentage

🛠️ Tech Stack
Programming

Python

Machine Learning

Scikit-Learn

XGBoost

NumPy

Pandas

Data Visualization

Matplotlib

Seaborn

Deployment

Streamlit

GitHub

Streamlit Cloud

📁 Project Structure
AI-Driven-Fitness-Intelligence-System
│
├── app.py
├── gym_ai_bodyfat_model.pkl
├── requirements.txt
├── dataset.csv
├── notebooks
│
└── README.md
▶️ Installation & Setup

Clone the repository

git clone https://github.com/parthTyagi-tech/AI-Driven-Fitness-Intelligence-System.git

Move into the project directory

cd AI-Driven-Fitness-Intelligence-System

Install dependencies

pip install -r requirements.txt

Run the Streamlit application

streamlit run app.py
🎯 Key Highlights

✔ End-to-end Machine Learning pipeline
✔ Model comparison and evaluation
✔ High-performance XGBoost regression model
✔ Interactive AI fitness prediction web application
✔ Deployed and accessible via Streamlit Cloud

🔮 Future Improvements

Potential improvements include:

AI-based diet recommendation engine

Workout recommendation system

Body fat category classification

Integration with wearable fitness devices

Personalized calorie planning

👨‍💻 Author

Parth Tyagi

Machine Learning Enthusiast | Data Science | AI Systems

GitHub
https://github.com/parthTyagi-tech

⭐ If you found this project useful, consider starring the repository.
