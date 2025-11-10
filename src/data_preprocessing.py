import pandas as pd

def clean_data(df):
    """other modification"""
    """Remove rows with missing customer IDs and fill NaNs."""
    df = df.dropna(subset=['customer_id'])
    df = df.fillna(0)
    return df