import pandas as pd

def clean_data(df):
    """change 2""
    df = df.dropna(subset=['customer_id'])
    df = df.fillna(0)
    return df