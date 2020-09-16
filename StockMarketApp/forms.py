from django import forms
from StockMarketApp.models import userinfo

class UserForm(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = '__all__'