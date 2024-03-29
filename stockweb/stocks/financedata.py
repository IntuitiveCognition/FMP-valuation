import os
import pandas as pd
import requests
from . import functions 
# dataframe for 20year(main dataframe)


### https://www.youtube.com/watch?v=vcDfNvC6Ui4  hid api using setx via that youtube video

api = os.getenv("FMP_API_KEY")

def get_finance_data(symbol,latest10K_date):
    
    income = functions.get_annual_income(symbol,latest10K_date)
    income_df = pd.DataFrame(income)
    income_df.set_index('date', inplace=True)
    
    balance = functions.get_annual_balance(symbol,latest10K_date)
    balance_df = pd.DataFrame(balance)
    balance_df.set_index('date', inplace=True)
        
    cash = functions.get_annual_cashflow(symbol,latest10K_date)
    cash_df = pd.DataFrame(cash)
    cash_df.set_index('date', inplace=True)
        
    keymetrics = functions.get_annual_keymetrics(symbol,latest10K_date)
    key_metrics_df = pd.DataFrame(keymetrics)
    key_metrics_df.set_index('date', inplace=True)

    enterprisevalue = functions.get_annual_enterprisevalue(symbol,latest10K_date)
    enterprisevalue_df = pd.DataFrame(enterprisevalue)
    enterprisevalue_df.set_index('date', inplace=True)
    
    
    price_df = enterprisevalue_df[['stockPrice']]
    price_df = price_df.rename(columns={'stockPrice': 'Stock'})
    price_df.index = pd.to_datetime(price_df.index, format='%Y-%m-%d').year 
    price_df.index.names = ['Date'] 
    
    
    try:    
        historical_dividend_response = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/{symbol}?apikey={api}")
        historical_dividend_response = historical_dividend_response.json()
        historical_dividend_response = historical_dividend_response['historical']
        dividend_df = pd.DataFrame.from_dict(historical_dividend_response)
        dividend_df.set_index('date', inplace=True)
        yearly_dividend_df = dividend_df.drop(columns=['label', 'dividend', 'recordDate', 'paymentDate', 'declarationDate'])
        yearly_dividend_df = yearly_dividend_df.set_index(pd.to_datetime(yearly_dividend_df.index))
        count_df = yearly_dividend_df.resample('Y').count()
        #count_df = count_df[count_df['adjDividend'] > 3]
        sum_dividend_df = yearly_dividend_df.resample('Y').sum()
        div_merged_df=pd.merge(count_df, sum_dividend_df, how='inner', left_index=True, right_index=True)
        div_merged_df = div_merged_df.reindex(index=div_merged_df.index[::-1])
        historical_dividend_df = div_merged_df.rename(columns={'adjDividend_x': 'count', 'adjDividend_y': 'dividend'})

        historical_dividend_df['month'] = historical_dividend_df.index.map(lambda x: x.year) == 2023  #must add one to year to report divedend correctly!!!!!!!!
        historical_dividend_df = historical_dividend_df[historical_dividend_df['month'] == False]
        historical_dividend_df.index = pd.to_datetime(historical_dividend_df.index, format='%Y-%m-%d').year
        historical_dividend_df = historical_dividend_df.drop(columns=['month'])
        historical_dividend_df = historical_dividend_df.iloc[:20]
        historical_dividend_df = historical_dividend_df.reindex(index=historical_dividend_df.index[::-1])
    except:
        pass

    reduce_income_df = income_df[['revenue', 'ebitda','weightedAverageShsOut']]
    reduce_balance_df = balance_df[['shortTermDebt', 'longTermDebt', 'cashAndShortTermInvestments']]
    reduce_cash_df = cash_df[['operatingCashFlow', 'freeCashFlow']]
    reduce_key_metrics_df = key_metrics_df[['enterpriseValue', 'roic', 'payoutRatio', 'peRatio']] 

    #merging df's 
    #reduce_income_df, reduce_balance_df, reduce_cash_df, reduce_enterprise_value_df
    merge=pd.merge(reduce_income_df, reduce_balance_df, how='inner', left_index=True, right_index=True)
    merge2=pd.merge(reduce_cash_df, reduce_key_metrics_df, how='inner', left_index=True, right_index=True)
    merge3=pd.merge(merge, merge2, how='inner', left_index=True, right_index=True)
    merge3 = merge3.set_index(pd.to_datetime(merge3.index))
    merge3.index = pd.to_datetime(merge3.index, format='%Y-%m-%d').year
    merge4=pd.merge(merge3, price_df,  how='inner', left_index=True, right_index=True)

    try:
        final_df=merge4.join(historical_dividend_df, how='left')
    except:
        final_df = merge4
    try:
        final_df = final_df.reindex(index=final_df.index[::-1]) 
    except:
        final_df 

    final_df['rev%'] = (final_df['revenue'].div(final_df['revenue'].shift(1))-1)
    final_df['ebitda%'] = (final_df['ebitda'].div(final_df['ebitda'].shift(1))-1)
    final_df['weightedAverageShsOut%'] = (final_df['weightedAverageShsOut'].div(final_df['weightedAverageShsOut'].shift(1))-1)
    final_df['freeCashFlow%'] = (final_df['freeCashFlow'].div(final_df['freeCashFlow'].shift(1))-1)
    final_df['Stock%'] = (final_df['Stock'].div(final_df['Stock'].shift(1))-1)
    try:
        final_df['dividend%'] = (final_df['dividend'].div(final_df['dividend'].shift(1))-1)
    except:
        pass
    try:    
        final_df = final_df[['revenue', 'rev%', 'ebitda', 'ebitda%', 'roic', 'operatingCashFlow', 'freeCashFlow',
                        'freeCashFlow%', 'enterpriseValue', 'shortTermDebt', 'longTermDebt', 'cashAndShortTermInvestments', 
                        'weightedAverageShsOut', 'weightedAverageShsOut%', 'Stock', 'Stock%', 'payoutRatio', 'count',
                            'dividend', 'dividend%',]]
        final_df = final_df.rename(columns={'revenue':'Revenue', 'rev%':'R%', 'ebitda':'EBITDA', 'ebitda%':'E%', 'roic':'ROIC',
                                 'operatingCashFlow':'Op CF', 'freeCashFlow':'FCF', 'freeCashFlow%':'FCF%', 'enterpriseValue':'Enterprise Val',
                                 'shortTermDebt':'Short Debt', 'longTermDebt':'Long Debt', 'cashAndShortTermInvestments':'Cash & STI', 
                                 'weightedAverageShsOut':'Shares Out', 'weightedAverageShsOut%':'SO%', 'Stock':'Price', 'Stock%':'Price%',
                                 'payoutRatio':'PO Ratio', 'count':'Div Count', 'dividend':'Div', 'dividend%':'Div%'})
        format_dict = {'Revenue':'${0:,.0f}', 'R%': '{:.1%}', 'EBITDA': '${0:,.0f}', 'E%':'{:.1%}', 'ROIC': '{:.1%}', 'Op CF': '${0:,.0f}',
                'FCF':'${0:,.0f}', 'FCF%': '{:.1%}', 'Enterprise Val': '${0:,.0f}', 'Short Debt':'${0:,.0f}', 'Long Debt': '${0:,.0f}', 'Cash & STI': '${0:,.0f}',
                'Shares Out':'${0:,.0f}', 'SO%': '{:.1%}', 'Price': '${0:,.2f}', 'Price%':'{:.1%}', 'PO Ratio': '{:.1%}', 'Div Count': '{0:,.0f}',
                'Div':'${0:,.2f}', 'Div%': '{:.1%}'}
        styles = [
                #table properties
                dict(selector=" ", 
                     props=[("margin","0"),("font-family",'"Helvetica", "Arial", sans-serif'),("text-align", "right"),
                            ("border-collapse", "1px black solid !important"),("border","1px black solid !important"),("border", "2px solid #ccf"),("font-size","75%")]),

                #header color - optional
                dict(selector="thead",props=[("background-color","#FFE5B4")]),

                #background shading
                dict(selector="tbody tr:nth-child(even)",props=[("background-color", "#fff")]),
                dict(selector="tbody tr:nth-child(odd)",props=[("background-color", "#eee")]),

                #cell spacing
                dict(selector="td",props=[("padding", ".4em"),('border', '.5px lightgrey solid !important')]),

                #header cell properties
                dict(selector="th",props=[("font-size", "110%"),("text-align", "center"),('border', '1px black solid !important')]),
        ]
        final_df = final_df.style.format(format_dict)\
                                 .set_table_styles(styles)
    except:    
        final_df = final_df[['revenue', 'rev%', 'ebitda', 'ebitda%', 'roic', 'operatingCashFlow', 'freeCashFlow',
                        'freeCashFlow%', 'enterpriseValue', 'shortTermDebt', 'longTermDebt', 'cashAndShortTermInvestments', 
                        'weightedAverageShsOut', 'weightedAverageShsOut%', 'Stock', 'Stock%']]
        final_df = final_df.rename(columns={'revenue':'Revenue', 'rev%':'R%', 'ebitda':'EBITDA', 'ebitda%':'E%', 'roic':'ROIC',
                                 'operatingCashFlow':'Op CF', 'freeCashFlow':'FCF', 'freeCashFlow%':'FCF%', 'enterpriseValue':'Enterprise Val',
                                 'shortTermDebt':'Short Debt', 'longTermDebt':'Long Debt', 'cashAndShortTermInvestments':'Cash & STI', 
                                 'weightedAverageShsOut':'Shares Out', 'weightedAverageShsOut%':'SO%', 'Stock':'Price', 'Stock%':'Price%'})
        format_dict = {'Revenue':'${0:,.0f}', 'R%': '{:.1%}', 'EBITDA': '${0:,.0f}', 'E%':'{:.1%}', 'ROIC': '{:.1%}', 'Op CF': '${0:,.0f}',
               'FCF':'${0:,.0f}', 'FCF%': '{:.1%}', 'Enterprise Val': '${0:,.0f}', 'Short Debt':'${0:,.0f}', 'Long Debt': '${0:,.0f}', 'Cash & STI': '${0:,.0f}',
               'Shares Out':'${0:,.0f}', 'SO%': '{:.1%}', 'Price': '${0:,.2f}', 'Price%':'{:.1%}'}
        styles = [
            #table properties
            dict(selector=" ", 
                 props=[("margin","0"),("font-family",'"Helvetica", "Arial", sans-serif'),("text-align", "right"),
                        ("border-collapse", "1px black solid !important"),("border","1px black solid !important"),("border", "2px solid #ccf"),("font-size","75%")]),

            #header color - optional
            dict(selector="thead",props=[("background-color","#FFE5B4")]),

            #background shading
            dict(selector="tbody tr:nth-child(even)",props=[("background-color", "#fff")]),
            dict(selector="tbody tr:nth-child(odd)",props=[("background-color", "#eee")]),

            #cell spacing
            dict(selector="td",props=[("padding", ".4em"),('border', '.5px lightgrey solid !important')]),

            #header cell properties
            dict(selector="th",props=[("font-size", "110%"),("text-align", "center"),('border', '1px black solid !important')]),
        ]
        final_df = final_df.style.format(format_dict)\
                           .set_table_styles(styles)
    return final_df