import pandas as pd
from . import functions

def get_all_quarter(symbol,latest10Q_date):
    global cash
    global balance
    global income
    
    
    # Retrieve quarter income statement
    income = functions.get_quarter_income(symbol,latest10Q_date)
   
    # Retrieve quarter balance sheet
    balance = functions.get_quarter_balance(symbol,latest10Q_date)
            
    # Retrieve quarter cash flow statement
    cash = functions.get_quarter_cashflow(symbol,latest10Q_date)
            
    # Retrieve quarter key metrics
    keymetrics = functions.get_quarter_keymetrics(symbol,latest10Q_date)
    
    # Retrieve quarter enterprise value
    enterprisevalue = functions.get_quarter_enterprisevalue(symbol,latest10Q_date)
        
    # Retrieve quarter ratios
    ratios = functions.get_quarter_ratios(symbol,latest10Q_date)
       
    # Convert JSON files to pandas dataframes
    income_df = pd.DataFrame(income).round(2)
    balance_df = pd.DataFrame(balance).round(2)
    cash_df = pd.DataFrame(cash).round(2)
    keymetrics_df = pd.DataFrame(keymetrics).round(2)
    enterprisevalue_df = pd.DataFrame(enterprisevalue).round(2)
    ratios_df = pd.DataFrame(ratios).round(2)
    
    # Merge dataframes using date as index
    merged_df = income_df.merge(balance_df, on='date', suffixes=('', '_balance'))
    merged_df = merged_df.merge(cash_df, on='date', suffixes=('', '_cash'))
    merged_df = merged_df.merge(keymetrics_df, on='date', suffixes=('', '_keymetrics'))
    merged_df = merged_df.merge(enterprisevalue_df, on='date', suffixes=('', '_enterprisevalue'))
    merged_df = merged_df.merge(ratios_df, on='date', suffixes=('', '_ratios'))

    # Remove duplicate columns with suffix '_balance', '_cash', '_keymetrics', '_enterprisevalue', '_ratios'
    cols_to_drop = [col for col in merged_df.columns if col.endswith(('_balance', '_cash', '_keymetrics', '_enterprisevalue', '_ratios'))]
    merged_df = merged_df.drop(cols_to_drop, axis=1)
    #merged_df['dividend'] = abs((merged_df.dividendsPaid / merged_df.numberOfShares).round(2))
    merged_df = merged_df.iloc[::-1]
    merged_df = merged_df.fillna(0)
    all_quarter = merged_df.to_dict(orient='records')
    return all_quarter