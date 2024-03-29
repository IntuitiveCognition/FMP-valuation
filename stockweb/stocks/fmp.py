import os
import pandas as pd
import requests
import json



api = os.getenv("FMP_API_KEY")

def get_quote(ticker):
    
    response = requests.get(f"https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey={api}")
    response = response.json()
    quote_df = pd.DataFrame(response)
    return response[0]