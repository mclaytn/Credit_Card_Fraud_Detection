# Imported Libraries
import pandas as pd
import numpy as np
# from sklearn.linear_model import LinearRegression, LogisticRegression

# Read dataset
credit_df = pd.read_csv('fraudTest.csv')

# Prepping Dataset
def prep_data(credit_df: pd.DataFrame) -> (np.ndarray):
    x = credit_df.iloc[:, 2:30].values
    y = credit_df.Class.values
    return x, y

# Plotting Dataset
    



