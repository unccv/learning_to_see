# Support Functions For Learning To See Series
# Welch Labs

import numpy as np

def computeConfusionMatrix(y, yHat, verbose = True):
    
    #Make sure data is 1d, not 2d numpy arrays
    if y.ndim == 2:
        y = y[:,0]
        
    if yHat.ndim == 2:
        yHat = yHat[:,0]

    FN =  np.sum(np.logical_and(y==1, yHat==0))
    FP =  np.sum(np.logical_and(y==0, yHat==1))
    TP = np.sum(np.logical_and(y==1, yHat==1))
    TN = np.sum(np.logical_and(y==0, yHat==0))
    
    cm = np.array([[TP, FN], [FP, TN]])
    
    if (TP + FN != 0):
        recall = float(TP)/(TP+FN)
    else:
        recall = 0
        
    if (TP+FP != 0):
        precision = float(TP)/(TP+FP)
    else:
        precision = 0
    accuracy = float(TP+TN)/len(y)
    
    if verbose:
        print('Confusion Matrix:')
        print(cm)
        print('Recall (TPR) = ' + str(round(recall,3))  + \
            ' (Portion of fingers that we "caught")')
        print('Precision (PPV) = ' + str(round(precision,3)) + \
            '(Portion of predicted finger pixels that were actually finger pixels)')
        print('Accuracy = ' + str(round(accuracy,3)))
    
    return cm, accuracy, recall, precision