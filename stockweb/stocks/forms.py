from django import forms

class TickerForm(forms.Form):
    ticker = forms.CharField(label='Ticker', max_length=5)

class GraphForm(forms.Form):
    graphticker = forms.CharField(label='Chart Ticker', max_length=5)