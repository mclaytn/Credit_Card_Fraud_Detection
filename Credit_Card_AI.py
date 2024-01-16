# Imported Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# from sklearn.linear_model import LinearRegression, LogisticRegression

# Read dataset
credit_df = pd.read_csv('fraudTest.csv')

# Prepping Dataset
def prep_data(credit_df: pd.DataFrame) -> (np.ndarray):
    x = credit_df.iloc[:, 2:30].values
    y = credit_df.__class__.values
    return x, y

# Plotting Dataset
def plot_data(x: np.ndarray, y: np.ndarray):
      plt.scatter(x[y == 0, 0], x[y == 0, 1], label="Exhibit #0", alpha=0.5, linewidth=0.15)
      plt.scatter(x[y == 1, 0], x[y == 1, 1], label="Exhibit #1", alpha=0.5, linewidth=0.15, c='r')
      plt.legend()
      return plt.show()
x, y = prep_data(credit_df)
plot_data(x, y)
