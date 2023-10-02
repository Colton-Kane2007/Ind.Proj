import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE, SelectKBest, f_regression
from scipy import stats
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import\
DecisionTreeClassifier as DT
from sklearn import svm

def wrangle_league():
    '''
    wrangle_league takes a csv that the user has downloaded from 
    Kaggle and prepares it by changing letters to lowercase,
    setting gameid as index, engineering new categories for the difference in 
    kills and assists between blue and red team, and splitting the data into 
    3 pandas dataframes in order to train, validate, and test machine learning
    classification models on.
    '''
    df = pd.read_csv('/Users/colt/Downloads/high_diamond_ranked_10min.csv')
    df.columns = df.columns.str.lower()
    df = df.set_index('gameid')
    df['bluekilldiff'] = df.bluekills - df.redkills
    df['blueassistdiff'] = df.blueassists - df.redassists
    # Caching that dataframe to disk for later
    df.to_csv('league.csv')
    train, validate, test = train_val_test(df)
    return train, validate, test

def train_val_test(df):
    '''
    train_val_test takes in a dataframe and splits it in order to run machine learning models on.
    '''
    train_val, test = train_test_split(df,
                                  random_state=1349,
                                  train_size=0.8)
    train, validate = train_test_split(train_val,
                                  random_state=1349,
                                  train_size=0.7)
    return train, validate, test

def display_numeric_column_histograms(data_frame):
    """
    Display histograms for numeric columns in a DataFrame.
    """
    numeric_columns = data_frame.select_dtypes(exclude=["object", "category"]).columns.to_list()
    # Define any number of colors for the histogram bars
    colors = ["olive"]
    for i, column in enumerate(numeric_columns):
        # Create a histogram for each numeric column with two colors
        figure, axis = plt.subplots(figsize=(10, 3))
        sns.histplot(data_frame, x=column, ax=axis, color=colors[i % len(colors)])
        axis.set_title(f"Histogram of {column}")
        plt.show()