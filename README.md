# RougeBank Fintech App
A new approach to banking technology that's fast, accurate and more agile🚀. 
Get your loan applocations approved faster and have the flexibility to learn from your customers as you grow. I present to you, ROugeBank loan app, a progressive web application powered by artifical intelligence to deliver loan applications faster. 

## Technology Stack
This application is developed in Python3. The stack is divided into three components:
1. Machine learning using python sikcit-learn 
2. Django web framework for backend development
3. HTML and CSS for frontend development

### Data Source
The dataset used in this project is taken from Kaggle and can be found at [a link](https://www.kaggle.com/ninzaami/loan-predication)

### Machine Learning:
The machine learning pipeline is divided into two python notebooks. The first is the data wrangling notebook which contains the data ingestion, exploratory data analysis, visualization and preprocessing. The libraries in this notebook are listed below.

* pandas 
* numpy
* matplotlib
* seaborn
* imbalanced-learn (must use pytorch or tensorflow backend for compatibility)
* pickle

The second notebook includes the algorithm training, hyperparameter tuning and evaluation. The libraries used in this notebook are the following:

* sklearn
* keras (must use pytorch or tensorflow backend for compatibility)


The last notebook is the production data test, a randomly synthesized dataset is fed into the model to test for validation before production.


### Web Development:
I use Django restframework to develop the backend. I follow the documentation found here [a link](https://docs.djangoproject.com/en/3.0/)  which is very well written to build the application. 
