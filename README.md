# StockMarketPrediction-WebApplication
Prediction of Stock Market prices using Machine Learning Algorithms with Neural Network.  In this, Django FrameWork is used for deployment process. 
Steps involved in this project:
1) Data Extraction
2) Data Analysis
3) Data Preprocessing
4) Feature Selection
5) Model Building
6) Deployment in Local System
7) Making live using Heroku Cloud Platform

1) Data Extraction:
    In a better way, Yahoo services providing a perfect stock values in the basis of day to day live updates, using pandas_datareader library, pull the data from the yahoo website directly.
2) Data Analysis:
    Because of this is a Time Series Dataset, We can easily go through the time series plot and also a normal plot, from that easy to say whether the values are increasing or decreasing at the specific date.
    And also that, correlation between all variables is very high. It tends to multicollinearity problem. It will handle in the feature selection technique.
    Various data visualization analysis takes places to study the flow of the data.
3) Data Preprocessing:
    It is not difficult to preprocess this data, Because yahoo provides the perfect data
