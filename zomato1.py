import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# Load the dataset
zomato = pd.read_csv(r"try\tasks\zomato.csv", encoding='latin1', engine='python', on_bad_lines='warn')
print(zomato.head())
print(zomato.info())
print(zomato.isnull().sum())
print(zomato.shape)
print(zomato.columns)
print(zomato.describe())
print(zomato.duplicated().sum())
print(zomato.duplicated().sum())
zomato.drop_duplicates(inplace=True)