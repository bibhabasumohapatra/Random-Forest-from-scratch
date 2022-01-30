import numpy as np
import pandas as pd

def accuracy(y_hat, y):
    """
    Function to calculate the accuracy

    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the accuracy as float
    """
    """
    The following assert checks if sizes of y_hat and y are equal.
    Students are required to add appropriate assert checks at places to
    ensure that the function does not fail in corner cases.
    """
    assert(y_hat.size == y.size)
    count = 0
    for element in range(len(y)):
        if y[element] == y_hat[element]:
            count+=1
    return count/len(y)
    

def precision(y_hat, y, cls):
    """
    Function to calculate the precision

    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    > cls: The class chosen
    Output:
    > Returns the precision as float
    """
    TP, FP, TN, FN = 0
    for i in range(len(y)):
        if y_hat[i]==y_hat[i]==cls:
           TP += 1
        if y_hat[i]==cls and y_hat[i]!=y_hat[i]:
           FP += 1
        if y_hat[i]==y_hat[i]!=cls:
           TN += 1
        if y_hat[i]!=cls and y_hat[i]!=y_hat[i]:
           FN += 1
    return TP/(TP+FP)

def recall(y_hat, y, cls):
    """
    Function to calculate the recall

    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    > cls: The class chosen
    Output:
    > Returns the recall as float
    """
    TP, FP, TN, FN = 0
    for i in range(len(y)):
        if y_hat[i]==y_hat[i]==1:
           TP += 1
        if y_hat[i]==cls and y_hat[i]!=y_hat[i]:
           FP += 1
        if y_hat[i]==y_hat[i]==0:
           TN += 1
        if y_hat[i]!=cls and y_hat[i]!=y_hat[i]:
           FN += 1
    return TP/(TP+FN)
   

def rmse(y_hat, y):
    """
    Function to calculate the root-mean-squared-error(rmse)

    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the rmse as float
    """
    squared_errors = np.pow(y_hat - y, 2)
    sum_of_squared_errors = np.sum(squared_errors)
    return sum_of_squared_errors/ len(y)

def mae(y_hat, y):
    """
    Function to calculate the mean-absolute-error(mae)

    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the mae as float
    """
    absolute_errors = np.abs(y_hat - y)
    sum_of_absolute_errors = np.sum(absolute_errors)
    return sum_of_absolute_errors/len(y)
    
