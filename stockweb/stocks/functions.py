import requests
from pathlib import Path
import os
import json
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
#### Holds functions to retreive data ###
api = "c0125052bc240a2359979dc2de79eb99"
def get_annual_date(symbol):
    #finds dates for latest annual 10K and quarter 10Q reports
    check10K = requests.get(f"https://financialmodelingprep.com/api/v3/sec_filings/{symbol}?type=10-K&page=0&apikey={api}")
    check10K = check10K.json()
    check10K = check10K[0]['acceptedDate']
    latest10K_date = check10K[0:10]
    return latest10K_date

def get_quarter_date(symbol):
    check10Q = requests.get(f"https://financialmodelingprep.com/api/v3/sec_filings/{symbol}?type=10-Q&page=0&apikey={api}")
    check10Q = check10Q.json()
    check10Q = check10Q[0]['acceptedDate']
    latest10Q_date = check10Q[0:10]
    return latest10Q_date

def get_annual_income(symbol,latest10K_date):
     #verifies if latest annualincome 10K has been downloaded, else downloads latest
    filePathannualincome =  (f"E:/astockwebsite/{symbol}{latest10K_date}annual/{symbol}{latest10K_date}annualincome.json")
    if os.path.isfile(filePathannualincome):
        with open(f"{filePathannualincome}", 'r') as f:
            annual_income = json.load(f)            
        print('Annual income File already exists, returning file to you')
        return annual_income           
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10K_date}annual").mkdir(parents=True, exist_ok=True)
        income_response = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{symbol}?period=annual&limit=20&apikey={api}")
        with open(filePathannualincome, 'a') as fp:
            fp.write(income_response.text)
        with open(f"{filePathannualincome}", 'r') as f:
            annual_income = json.load(f)
        print('Annual income File does not exist, will create file and return to you.')
        return annual_income
def get_annual_balance(symbol,latest10K_date):    
    #verifies if latest annual balance 10K has been downloaded, else downloads latest
    filePathannualbalance =  (f"E:/astockwebsite/{symbol}{latest10K_date}annual/{symbol}{latest10K_date}annualbalance.json")
    if os.path.isfile(filePathannualbalance):
        with open(f"{filePathannualbalance}", 'r') as f:
            annual_balance = json.load(f)
        print('Annual balance File already exists, returning file to you')
        return annual_balance
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10K_date}annual").mkdir(parents=True, exist_ok=True)
        balance_response = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{symbol}?period=annual&limit=20&apikey={api}")
        with open(filePathannualbalance, 'a') as fp:
            fp.write(balance_response.text)
        with open(f"{filePathannualbalance}", 'r') as f:
            annual_balance = json.load(f)
        print('Annual balance File does not exist, will create file and return to you.')
        return annual_balance
def get_annual_cashflow(symbol,latest10K_date):    
    #verifies if latest annual cashflow 10K has been downloaded, else downloads latest
    filePathannualcashflow =  (f"E:/astockwebsite/{symbol}{latest10K_date}annual/{symbol}{latest10K_date}annualcashflow.json")
    if os.path.isfile(filePathannualcashflow):
        with open(f"{filePathannualcashflow}", 'r') as f:
            annual_cashflow= json.load(f)
        print('Annual cashflow File already exists, returning file to you')
        return annual_cashflow           
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10K_date}annual").mkdir(parents=True, exist_ok=True)
        cashflow_response = requests.get(f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{symbol}?period=annual&limit=20&apikey={api}")
        with open(filePathannualcashflow, 'a') as fp:
            fp.write(cashflow_response.text)
        with open(f"{filePathannualcashflow}", 'r') as f:
            annual_cashflow = json.load(f)
        print('Annual cashflow File does not exist, will create file and return to you.')
        return annual_cashflow
def get_annual_keymetrics(symbol,latest10K_date):    
    #verifies if latest annual keymetrics 10K has been downloaded, else downloads latest
    filePathannualkeymetrics=  (f"E:/astockwebsite/{symbol}{latest10K_date}annual/{symbol}{latest10K_date}annualkeymetrics.json")
    if os.path.isfile(filePathannualkeymetrics):
        with open(f"{filePathannualkeymetrics}", 'r') as f:
            annual_keymetrics= json.load(f)
        print('Annual keymetrics File already exists, returning file to you')
        return annual_keymetrics
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10K_date}annual").mkdir(parents=True, exist_ok=True)
        key_metrics_response = requests.get(f"https://financialmodelingprep.com/api/v3/key-metrics/{symbol}?limit=20&apikey={api}")
        with open(filePathannualkeymetrics, 'a') as fp:
            fp.write(key_metrics_response.text)
        with open(f"{filePathannualkeymetrics}", 'r') as f:
            annual_keymetrics = json.load(f)
        print('Annual keymetrics File does not exist, will create file and return to you.')
        return annual_keymetrics
def get_annual_enterprisevalue(symbol,latest10K_date):    
    #verifies if latest annual enterprisevalue 10K has been downloaded, else downloads latest
    filePathannualenterprisevalue=  (f"E:/astockwebsite/{symbol}{latest10K_date}annual/{symbol}{latest10K_date}annualenterprisevalue.json")
    if os.path.isfile(filePathannualenterprisevalue):
        with open(f"{filePathannualenterprisevalue}", 'r') as f:
            annual_enterprisevalue= json.load(f)
        print('Annual enterprisevalue File already exists, returning file to you')
        return annual_enterprisevalue
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10K_date}annual").mkdir(parents=True, exist_ok=True)
        enterprise_value_response = requests.get(f"https://financialmodelingprep.com/api/v3/enterprise-values/{symbol}?limit=20&apikey={api}")
        with open(filePathannualenterprisevalue, 'a') as fp:
            fp.write(enterprise_value_response.text)
        with open(f"{filePathannualenterprisevalue}", 'r') as f:
            annual_enterprisevalue = json.load(f)
        print('Annual enterprisevalue File does not exist, will create file and return to you.')
        return annual_enterprisevalue
def get_annual_ratios(symbol,latest10K_date):        
    #verifies if latest annual financialratios 10K has been downloaded, else downloads latest
    filePathannualfinancialratios=  (f"E:/astockwebsite/{symbol}{latest10K_date}annual/{symbol}{latest10K_date}annualfinancialratios.json")
    if os.path.isfile(filePathannualfinancialratios):
        with open(f"{filePathannualfinancialratios}", 'r') as f:
            annual_financialratios= json.load(f)
        print('Annual financialratios File already exists, returning file to you')
        return annual_financialratios           
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10K_date}annual").mkdir(parents=True, exist_ok=True)
        financial_ratio_response = requests.get(f"https://financialmodelingprep.com/api/v3/ratios/{symbol}?limit=20&apikey={api}")
        with open(filePathannualfinancialratios, 'a') as fp:
            fp.write(financial_ratio_response.text)
        with open(f"{filePathannualfinancialratios}", 'r') as f:
            annual_financialratios = json.load(f)
        print('Annual financialratios File does not exist, will create file and return to you.')
        return annual_financialratios
    
def get_weekly_price(symbol):
    now = datetime.today()
    today = now.strftime('%Y-%m-%d')
    twentyyearsago = (now + relativedelta(years=-20)).strftime('%Y-%m-%d')
    response = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?from={twentyyearsago}&to={today}&apikey={api}")
    response = response.json()
    response = response['historical']
    price_df = pd.DataFrame.from_dict(response)
    price_df.set_index('date', inplace=True)
    price_df = price_df.set_index(pd.to_datetime(price_df.index))
    logic = {'open'  : 'first','high'  : 'max','low'   : 'min','close' : 'last','volume': 'sum'}
    price_df = price_df.resample('W').apply(logic)
    price_df.index = price_df.index - pd.tseries.frequencies.to_offset("6D")
    return price_df


