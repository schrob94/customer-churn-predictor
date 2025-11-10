import pandas as pd

def clean_data(df):
    "final version"
    df = df.dropna(subset=['customer_id'])
    df = df.fillna(0)
    return df
