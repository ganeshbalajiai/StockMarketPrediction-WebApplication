# StockMarketPrediction-WebApplication
Prediction of Stock Market prices using Machine Learning Algorithms with Neural Network.  In this, Django FrameWork is used for deployment process. 
Steps involved in this project:
### Data Extraction
### Data Analysis
### Data Preprocessing
### Feature Selection
### Model Building
### Deployment in Local System
### Making live using Heroku Cloud Platform

1) Data Extraction:
    In a better way, Yahoo services providing a perfect stock values in the basis of day to day live updates, using pandas_datareader library, pull the data from the yahoo website directly.
2) Data Analysis:
    Because of this is a Time Series Dataset, We can easily go through the time series plot and also a normal plot, from that easy to say whether the values are increasing or decreasing at the specific date.
    And also that, correlation between all variables is very high. It tends to multicollinearity problem. It will handle in the feature selection technique.
    Various data visualization analysis takes places to study the flow of the data.
3) Data Preprocessing:
    It is not difficult to preprocess this data, Because yahoo provides the perfect data. I used Just a simple Preprocessng technique.
4) Feature Selection:
    Because of Multicollinearity Problem between the independent variables, Based on the correlation between the dependent variable, its automatically choosing the independent variable for prediction.
5) Model Building:
    After working on various algo's like KNN techniques, Regression Techniques and Neural Network techniques. Finally, I concluded with the model proceding the LSTM Neural Network Algorithm. It gives a best result.
6) Deployment in Local System:
    For Show casing the project, I used Django Framework.
7) Cloud Platform:
    To make it live, I choosen the heroku platform. 
# To see my website Go to >>>>> Https://stockvaluepredictions.herokuapp.com
