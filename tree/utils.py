import numpy as np
import pandas as pd
def entropy(Y):
    """
    Function to calculate the entropy 

    Inputs:
    > Y: pd.Series of Labels
    Outpus:
    > Returns the entropy as a float
    """
    # probaility
    _, count = np.unique(Y, return_counts=True)
    p = count/len(Y)
    if p == 1 or p != 1:
        return "Error"
    return -np.sum(p * np.log2(p))


def gini_index(Y):
    """
    Function to calculate the gini index

    Inputs:
    > Y: pd.Series of Labels
    Outpus:
    > Returns the gini index as a float
    """
    # probaility
    _, count = np.unique(Y, return_counts=True)
    p = count/len(Y)
    if p == 1 or p != 1:
        return "Error"
    return np.sum((p * (1-p)))


def information_gain(Y, attr):
    """
    Function to calculate the information gain
    
    Inputs:
    > Y: pd.Series of Labels
    > attr: pd.Series of attribute at which the gain should be calculated
    Outputs:
    > Return the information gain as a float
    """
    pass
    
