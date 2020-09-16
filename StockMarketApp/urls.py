from django.conf.urls import url
from StockMarketApp import views

app_name = 'StockMarketApp'
urlpatterns = [
    url("^form/", views.form, name = "form"),
    url("^about/", views.about, name = "about"),
    url("^$", views.extract, name = "extract"),
]