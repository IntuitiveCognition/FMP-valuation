import requests
from pathlib import Path
import os
import json
import pandas as pd
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


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
def get_quarter_income(symbol,latest10Q_date):
    #verifies if latest quarter income  has been downloaded, else downloads latest
    filePathincome =  (f"E:/astockwebsite/{symbol}{latest10Q_date}quarter/{symbol}{latest10Q_date}quarterincome.json")
    if os.path.isfile(filePathincome):
        with open(f"{filePathincome}", 'r') as f:
            quarter_income = json.load(f)
        print('Quater income value File already exists, returning file to you')
        return quarter_income
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10Q_date}quarter").mkdir(parents=True, exist_ok=True)
        income_response = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{symbol}?period=quarter&limit=80&apikey={api}")
        with open(filePathincome, 'a') as fp:
            fp.write(income_response.text)
        with open(f"{filePathincome}", 'r') as f:
            quarter_income = json.load(f)
        print('Quarter income value File does not exist, will create file and return to you.')
        return quarter_income    
def get_quarter_balance(symbol,latest10Q_date):
    #verifies if latest quarter balance  has been downloaded, else downloads latest
    filePathbalance =  (f"E:/astockwebsite/{symbol}{latest10Q_date}quarter/{symbol}{latest10Q_date}quarterbalance.json")
    if os.path.isfile(filePathbalance):
        with open(f"{filePathbalance}", 'r') as f:
            quarter_balance = json.load(f)
        print('Quater balance value File already exists, returning file to you')
        return quarter_balance
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10Q_date}quarter").mkdir(parents=True, exist_ok=True)
        balance_response = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{symbol}?period=quarter&limit=80&apikey={api}")
        with open(filePathbalance, 'a') as fp:
            fp.write(balance_response.text)
        with open(f"{filePathbalance}", 'r') as f:
            quarter_balance = json.load(f)
        print('Quarter balance value File does not exist, will create file and return to you.')
        return quarter_balance
def get_quarter_cashflow(symbol,latest10Q_date):
    #verifies if latest quarter cashflow  has been downloaded, else downloads latest
    filePathcashflow =  (f"E:/astockwebsite/{symbol}{latest10Q_date}quarter/{symbol}{latest10Q_date}quartercashflow.json")
    if os.path.isfile(filePathcashflow):
        with open(f"{filePathcashflow}", 'r') as f:
            quarter_cashflow = json.load(f)
        print('Quater cashflow value File already exists, returning file to you')
        return quarter_cashflow
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10Q_date}quarter").mkdir(parents=True, exist_ok=True)
        cashflow_response = requests.get(f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{symbol}?period=quarter&limit=80&apikey={api}")
        with open(filePathcashflow, 'a') as fp:
            fp.write(cashflow_response.text)
        with open(f"{filePathcashflow}", 'r') as f:
            quarter_cashflow = json.load(f)
        print('Quarter cashflow value File does not exist, will create file and return to you.')
        return quarter_cashflow
def get_quarter_keymetrics(symbol,latest10Q_date): 
    #verifies if latest quarter keymetrics  has been downloaded, else downloads latest
    filePathkeymetrics =  (f"E:/astockwebsite/{symbol}{latest10Q_date}quarter/{symbol}{latest10Q_date}quarterkeymetrics.json")
    if os.path.isfile(filePathkeymetrics):
        with open(f"{filePathkeymetrics}", 'r') as f:
            quarter_keymetrics = json.load(f)
        print('Quater enterprise value File already exists, returning file to you')
        return quarter_keymetrics
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10Q_date}quarter").mkdir(parents=True, exist_ok=True)
        keymetrics_response = requests.get(f"https://financialmodelingprep.com/api/v3/key-metrics/{symbol}?period=quarter&limit=80&apikey={api}")
        with open(filePathkeymetrics, 'a') as fp:
            fp.write(keymetrics_response.text)
        with open(f"{filePathkeymetrics}", 'r') as f:
            quarter_keymetrics = json.load(f)
        print('Quarter keymetrics value File does not exist, will create file and return to you.')
        return quarter_keymetrics
def get_quarter_enterprisevalue(symbol,latest10Q_date):
    #verifies if latest quarter enterprisevalue  has been downloaded, else downloads latest
    filePathenterprisevalue =  (f"E:/astockwebsite/{symbol}{latest10Q_date}quarter/{symbol}{latest10Q_date}quarterenterprisevalue.json")
    if os.path.isfile(filePathenterprisevalue):
        with open(f"{filePathenterprisevalue}", 'r') as f:
            quarter_enterprisevalue = json.load(f)
        print('Quater enterprise value File already exists, returning file to you')
        return quarter_enterprisevalue
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10Q_date}quarter").mkdir(parents=True, exist_ok=True)
        enterprisevalue_response = requests.get(f"https://financialmodelingprep.com/api/v3/enterprise-values/{symbol}?period=quarter&limit=80&apikey={api}")
        with open(filePathenterprisevalue, 'a') as fp:
            fp.write(enterprisevalue_response.text)
        with open(f"{filePathenterprisevalue}", 'r') as f:
            quarter_enterprisevalue = json.load(f)
        print('Quarter enterprise value File does not exist, will create file and return to you.')
        return quarter_enterprisevalue
def get_quarter_ratios(symbol,latest10Q_date):
    #verifies if latest quarter ratio  has been downloaded, else downloads latest
    filePathratio =  (f"E:/astockwebsite/{symbol}{latest10Q_date}quarter/{symbol}{latest10Q_date}quarterratio.json")
    if os.path.isfile(filePathratio):
        with open(f"{filePathratio}", 'r') as f:
            quarter_ratio = json.load(f)
        print('Quater ratio value File already exists, returning file to you')
        return quarter_ratio
    else:    
        Path(f"E:/astockwebsite/{symbol}{latest10Q_date}quarter").mkdir(parents=True, exist_ok=True)
        ratio_response = requests.get(f"https://financialmodelingprep.com/api/v3/ratios/{symbol}?period=quarter&limit=80&apikey={api}")
        with open(filePathratio, 'a') as fp:
            fp.write(ratio_response.text)
        with open(f"{filePathratio}", 'r') as f:
            quarter_ratio = json.load(f)
        print('Quarter enterprise value File does not exist, will create file and return to you.')
        return quarter_ratio

    
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
    price_df = price_df.reset_index().rename(columns={'index': 'date'})
    price_df['date'] = price_df['date'].dt.strftime('%Y-%m-%d')
    #price_df.index = price_df.index - pd.tseries.frequencies.to_offset("6D")
    price_df = price_df.to_dict(orient='records')
    return price_df

def get_nasdaq_yearly_est(symbol):
    global data
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    #verifies if latest quarter ratio  has been downloaded, else downloads latest
    filePath =  (f"E:/astockwebsite/{symbol}/{symbol}{today}nasdaq/{symbol}{today}nasdaq.json")
    if os.path.isfile(filePath):
        with open(f"{filePath}", 'r') as f:
            nasdaq = json.load(f)
        print('Nasdaq EPS Estimate File already exists, returning file to you')
        
    else:    
        Path(f"E:/astockwebsite/{symbol}/{symbol}{today}nasdaq").mkdir(parents=True, exist_ok=True)
        service = Service('./chromedriver')
        driver = webdriver.Chrome(service=service)
        url = f'https://www.nasdaq.com/market-activity/stocks/{symbol}/earnings'
        driver.get(url)
        table = driver.find_element('xpath', '//table[@class="earnings-forecast__table"]')
        headers = [th.text for th in table.find_elements('xpath', './thead//th')]
        data = []
        for row in table.find_elements('xpath', './tbody//tr'):
            row_data = [td.text for td in row.find_elements('xpath', './/th|.//td')]
            data.append(row_data)

        driver.quit()
        df = pd.DataFrame(data, columns=headers)
        result = []
        for index, row in df.iterrows():
            futureeps = row['Consensus EPS* Forecast']
            date_str = str(row['Fiscal Year End'])
            year = ''.join(filter(str.isdigit, date_str))
            if year:
                result.append({'date': year, 'futureeps': float(futureeps)})
        with open(filePath, 'a') as fp:
            json.dump(result, fp)
        with open(f"{filePath}", 'r') as f:
            nasdaq = json.load(f)
        print('Nasdaq EPS Estimate File does not exist, will create file and return to you.')
    # Takes 4 year data points and turns it into 16 quarterly points equally spaced
    new_data = []
    for d in nasdaq:
        year = int(d['date'])
        date_str = f"{year}-12-31"
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        new_data.append({'date': date.strftime('%Y-%m-%d'), 'futureeps': d['futureeps']})

        for i in range(1, 53):
            prev_date = date - timedelta(days=7*i)
            prev_eps = d['futureeps'] - (d['futureeps'] - new_data[-1]['futureeps'])/52.0*i
            new_data.append({'date': prev_date.strftime('%Y-%m-%d'), 'futureeps': prev_eps})

    data = sorted(new_data, key=lambda x: x['date'])
    indices = [i for i, d in enumerate(data) if d['date'].endswith('-12-31')]

    # Loop through the indices, updating the values in between
    for i in range(len(indices)-1):
        start_index = indices[i]
        end_index = indices[i+1]
        start_value = data[start_index]['futureeps']
        end_value = data[end_index]['futureeps']
        num_values = end_index - start_index - 1
        if num_values > 0:
            step = (end_value - start_value) / (num_values + 1)
        else:
            step = 0

        # Fix erroneous jump in the last week of each year
        for j in range(1, num_values+1):
            if data[start_index+j]['date'].endswith('-12-31'):
                continue
            data[start_index+j]['futureeps'] = round(start_value + j*step, 2)
    return data
