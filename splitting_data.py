import pandas as pd

def split_data(data):
    """
    Function splits data based on data type, either categorical or numerical.
    """
    
    categorical = data.select_dtypes(include=['object', 'bool'])
    numerical = data.select_dtypes(exclude=['object', 'bool'])

    return categorical, numerical