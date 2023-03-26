from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from . import fmp
from . import financedata
from . import functions
from . import chartdata
from . import allannual
# Create your views here.
def index(request):
    if request.method == 'POST':#from index.html if form submitted
        form = forms.TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)#this redirects to a ticker.html but names is by the ticker symbol entered into form
    else:
        form = forms.TickerForm()#from index.html if page refreshed
    return render(request, 'index.html', {'form': form})

def ticker(request, tid):#view for ticker.html
    
    latest10K_date = functions.get_annual_date(tid)    
    finance_df = financedata.get_finance_data(tid,latest10K_date)
    finance_df = finance_df.to_html() 
    chart_json = chartdata.get_chart_data(tid,latest10K_date)
    all_annual =  allannual.get_all_annual(tid,latest10K_date)

    context ={}
    context['date'] = latest10K_date
    context['ticker'] = tid
    context['quote'] = fmp.get_quote(tid)
    context['table'] = finance_df
    context['chart_json'] = chart_json
    context['all_annual'] = all_annual
    return render(request, 'ticker.html', context)

