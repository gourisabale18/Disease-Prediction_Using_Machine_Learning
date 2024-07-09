## Disease Prediction System using Machine Learning

This project aims to provide disease prediction results by making use of symptoms seen by patients to in order to improve existing healthcare system efficiency.

In this project, we have developed machine learning model for multi-disease prediction by peforming data preprocessing, splitting into train-test sets, and feature selection from the Columbia hospital dataset.

We have trained ML model using Gaussian Naive Bayes classifier to predict 50 diseases from 132 symptoms, storing results in MySQL.

We used Python Django framework for application development and MySQL to store data at backend. 

We have also integrated a location finder service for nearest hospital recommendations based on predictions. 

## Tech Stack Used:
1. Python Django Web Application framework
2. MySQL/PostgreSQL
3. Tomcat Web Server/ XAMPP
4. Classification ML models
5. HTML, CSS, Javascript, AJAX

## Installation Steps:

1. Clone the project repository using this link:
https://github.com/gouri-sabale-123/Disease_Prediction_And_Drug_Recommendation_Using_Machine_Learning.git
2. Setup XAMPP Server on localhost by following the XAMPP installation guidelines:
https://www.apachefriends.org/download.html
3. Execute healthcare_db.sql script present in project folder into MYSQL DB
It is available at http://localhost/phpmyadmin/
4. Once the script is executed successfully, start Apache and MYSQL from XAMPP
5. Install Anaconda Python using following link:
https://docs.anaconda.com/free/anaconda/install/index.html
6. Start anaconda command prompt and run it as administrator
7. Navigate to the project folder cloned on your local system where you will see
manage.py
8. Run following command in anaconda command prompt
python runserver manage.py
