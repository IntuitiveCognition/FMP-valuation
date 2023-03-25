import pandas as pd
import requests
import json



api = "c0125052bc240a2359979dc2de79eb99"


def get_quote(ticker):
    
    response = requests.get(f"https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey={api}")
    response = response.json()
    quote_df = pd.DataFrame(response)
    return response[0]