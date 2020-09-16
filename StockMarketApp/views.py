from django.shortcuts import render
from django.http import HttpResponse
from StockMarketApp.forms import UserForm
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Flatten 
# Create your views here.

def formfinal(request):
    return render(request, "formfinal.html")
def form(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return formfinal(request)

    return render(request, "form.html", context = {'form' : form})

def about(request):
    return render(request, "about.html")
            
def index(request):

    return render(request, "index.html",)

def extract(request):
    try:
        company = request.GET['company']
        company = str(company)
        sdate = str(request.GET['sdate'])
        edate = str(request.GET['edate'])
        global df
        df = web.DataReader(company, "yahoo" , start = sdate, end = edate)
        df = df.reset_index()
        columns = df.columns
        return render(request, "stock.html", context = {"company" : company, "columns" : columns})
    except:
        return render(request, "error.html")
def corr(request):
    fig = plt.figure(figsize = (20,20))
    sns.heatmap(df.corr(), annot = True)
    buf = io.BytesIO()
    plt.savefig(buf, format = 'png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type = 'image/png')
    canvas = FigureCanvasAgg(fig)
    return response

def adjplot(request):

    fig = plt.figure(figsize= (20,20))
    plt.plot(df['Date'], df['Adj Close'])
    plt.xlabel("date")
    plt.ylabel("Adj Close")
    plt.title("Adj Close price history")
    buf = io.BytesIO()
    plt.savefig(buf, format = 'png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type = 'image/png')
    canvas = FigureCanvasAgg(fig)
    return response

def model(request):
    try:
        if request.POST['test_data']:
            test_numbers = int(request.POST['test_data'])
            epoch = int(request.POST['epochs'])
            org = len(df['Adj Close']) - test_numbers
            Traindata = df.iloc[0:org]
            Testdata = df.iloc[org:]
        elif request.FILES['file_data']:
            test_data = request.FILES['file_data']
            epoch = int(request.POST['epochs'])
            Traindata = df
            Testdata = pd.DataFrame(test_data)

        Train_values = Traindata['Adj Close']
        sc = MinMaxScaler(feature_range = (0,1))
        training_set_scaled = sc.fit_transform(pd.DataFrame(Train_values))
        #RNN model

        #creating a datastructure with 60 timesteps and 1 output
        X_train = []
        Y_train = []
        for i in range(60, len(training_set_scaled)):
            X_train.append(training_set_scaled[i-60:i,0])
            Y_train.append(training_set_scaled[i,0])
        X_train, Y_train = np.array(X_train), np.array(Y_train)

        #reshapping

        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1],1)) #batch_size, time_steps, input dim

        #initializing the model
        regressor = Sequential()
        ##########################

        #add the first LSTM layer and some Dropout regularisation

        regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1],1)))
        regressor.add(Dropout(0.2))

        #adding a second LSTM layer and some dropout regularisation

        regressor.add(LSTM(units = 50, return_sequences = True))
        regressor.add(Dropout(0.2))

        #adding a third LSTM layer and some dropout regularisation

        regressor.add(LSTM(units = 50, return_sequences = True))
        regressor.add(Dropout(0.2))

        #adding a fourth LSTM layer and some dropout regularisation

        regressor.add(LSTM(units = 50, return_sequences = True))
        regressor.add(Dropout(0.2))

        #Adding the output layer

        regressor.add(Flatten())
        regressor.add(Dense(units = 1))

        #compiling the RNN

        regressor.compile(optimizer = "adam", loss = "mean_squared_error")

        #fitting the RNN to the training set

        regressor.fit(X_train, Y_train, epochs = epoch)

        #prediction
        Train_values = pd.DataFrame(Train_values) 
        global Test_values
        Test_values = pd.DataFrame(Testdata['Adj Close'])
        df_total = pd.concat((Train_values['Adj Close'], Test_values['Adj Close']), axis = 0)
        inputs = df_total[len(df_total) - len(Test_values) - 60:].values
        inputs = inputs.reshape(-1,1)
        inputs = sc.fit_transform(inputs)

        X_test = []
        for i in range(60,len(inputs)):
            X_test.append(inputs[i-60:i,0])
        X_test = np.array(X_test)

        X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))
        global Adj_price
        Adj_price = regressor.predict(X_test) 
        Adj_price = sc.inverse_transform(Adj_price) #predicted price

        return render(request, "predict.html", context = {"final_value" : Adj_price})
    except:
       return render(request, "error2.html")
def pplot(request):
    fig = plt.figure(figsize = (20,20))
    plt.plot(Adj_price)
    plt.title("Predicted Stock Values")
    buf = io.BytesIO()
    plt.savefig(buf, format = 'png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type = 'image/png')
    canvas = FigureCanvasAgg(fig)
    return response
