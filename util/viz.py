# Support Functions For Learning To See Series
# Welch Labs

import numpy as np
import matplotlib.pyplot as plt
from data_handling import extractFeatures
from image import makeGrayScale
from PIL import Image
import matplotlib.colors as mcolors
from metrics import computeConfusionMatrix

def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)

#Make red and blue colormaps:
c = mcolors.ColorConverter().to_rgb
bw = make_colormap([(1,1,1), (1,1,1), 0.33, c('blue'), c('blue'), 0.66, c('blue')])
rw = make_colormap([(1,1,1), (1,1,1), 0.33, c('red'), c('red'), 0.66, c('red')])
rwb = make_colormap([c('red'), c('red'), 0.33, (1,1,1), (1,1,1), 0.66, c('blue')])


def showMatches(rules, exampleIndices, data, fig, verbose = True):
    '''
    Visualize matches to simple rules.
    '''

    for i in range(len(exampleIndices)):
        ax = fig.add_subplot(1,len(exampleIndices), i+1)

        imageDict = data[exampleIndices[i]]

        X, y = extractFeatures(imageDict, whichImage = 'image1bit', dist = 4)
        im = makeGrayScale(imageDict)

        matchingIndices = np.array([], dtype = 'int')
        for rule in rules:
            difference = X - rule.ravel()
            mI = np.where(~difference.any(axis=1))[0]
            matchingIndices = np.concatenate((matchingIndices, mI))

        matchVec = np.zeros(X.shape[0])
        matchVec[matchingIndices] = 1

        matchImage = matchVec.reshape((imageDict['boxHeight'], imageDict['boxWidth']))

        #Paint with matches:
        im[:,:,0][matchImage==1] = 0
        im[:,:,1][matchImage==1] = 1
        im[:,:,2][matchImage==1] = 0

        ax.imshow(im, interpolation = 'none')
        ax.axis('off')
        if verbose:
            plt.title('Number of Matches = ' + str(sum(matchVec ==1)), fontsize = 14)


def testRules(rules, exampleIndices, data, fig, X, y, showLegend = True, color = 'Full'):
    ## Color options: Full, Green.
    
    for i in range(len(exampleIndices)):
        ax = fig.add_subplot(1,4,i+1)
        imageDict = data[exampleIndices[i]]

        X1, y1 = extractFeatures(imageDict, whichImage = 'image1bit', dist = 4)
        im = makeGrayScale(imageDict)

        matchingIndices = np.array([], dtype = 'int')
        
        # List
        if type(rules) is list:
            for rule in rules:
                diff = X1 - rule.ravel()
                mI = np.where(~diff.any(axis=1))[0]
                matchingIndices = np.concatenate((matchingIndices, mI))
        
        # Numpy Array        
        elif type(rules) is np.ndarray:
            for i in range(rules.shape[0]):
                diff = X1 - rules[i, :]
                mI = np.where(~diff.any(axis=1))[0]
                matchingIndices = np.concatenate((matchingIndices, mI))
            
        # function
        elif callable(rules):
            matchingIndices = np.where(rules(X1))[0]
            
        matchVec = np.zeros(X1.shape[0])
        matchVec[matchingIndices] = 1

        truePositives = np.logical_and(y1, matchVec)
        falsePositives = np.logical_and(np.logical_not(y1), matchVec)
        falseNegatives = np.logical_and(y1, np.logical_not(matchVec))

        if color == 'Full':
            fNImage = falseNegatives.reshape(imageDict['boxHeight'], imageDict['boxWidth'])

            #Paint with matches:
            im[:,:,0][fNImage==1] = 1
            im[:,:,1][fNImage==1] = 1
            im[:,:,2][fNImage==1] = 0

            tPImage = truePositives.reshape((imageDict['boxHeight'], imageDict['boxWidth']))

            #Paint with matches:
            im[:,:,0][tPImage==1] = 0
            im[:,:,1][tPImage==1] = 1
            im[:,:,2][tPImage==1] = 0

            fNImage = falsePositives.reshape((imageDict['boxHeight'], imageDict['boxWidth']))

            #Paint with matches:
            im[:,:,0][fNImage==1] = 1
            im[:,:,1][fNImage==1] = 0
            im[:,:,2][fNImage==1] = 0
            
        if color == 'Green':
            
            matchImage = matchVec.reshape((imageDict['boxHeight'], imageDict['boxWidth']))

            #Paint with matches:
            im[:,:,0][matchImage==1] = 0
            im[:,:,1][matchImage==1] = 1
            im[:,:,2][matchImage==1] = 0
            
        ax.imshow(im, interpolation = 'none')
        ax.axis('off')
            
    if showLegend:
        legend = Image.open('../graphics/legendOne.png', 'r')
        ax4 = fig.add_subplot(1,4,len(exampleIndices)+1)
        ax4.imshow(legend)
        ax4.axis('off');

    # Now, search for matches in all data:
    matchingIndices = np.array([], dtype = 'int')

    # List
    if type(rules) is list:
        for rule in rules:
            diff = X - rule.ravel()
            mI = np.where(~diff.any(axis=1))[0]
            matchingIndices = np.concatenate((matchingIndices, mI))

    # Numpy Array        
    elif type(rules) is np.ndarray:
        for i in range(rules.shape[0]):
            diff = X - rules[i, :]
            mI = np.where(~diff.any(axis=1))[0]
            matchingIndices = np.concatenate((matchingIndices, mI))

    # function
    elif callable(rules):
        matchingIndices = np.where(rules(X))[0]
        
    yHat = np.zeros(X.shape[0])
    yHat[matchingIndices] = 1

    cm, accuracy, recall, precision = computeConfusionMatrix(y, yHat, verbose = True)

def testLogicalRules(exampleIndices, data, fig, X, y, rule):
    legend = Image.open('../graphics/legendOne.png', 'r')

    for i in range(len(exampleIndices)):
        ax = fig.add_subplot(1,4,i+1)
        imageDict = data[exampleIndices[i]]

        X1, y1 = extractFeatures(imageDict, whichImage = 'image1bit', dist = 4)

        im = makeGrayScale(imageDict)
        yImage = y1.reshape(imageDict['boxHeight'], imageDict['boxWidth'])

        #Paint with matches:
        im[:,:,0][yImage==1] = 1
        im[:,:,1][yImage==1] = 1
        im[:,:,2][yImage==1] = 0

        yHat = rule(X1)

        truePositives = np.logical_and(y1, yHat)
        falsePositives = np.logical_and(np.logical_not(y1), yHat)

        tPImage = truePositives.reshape((imageDict['boxHeight'], imageDict['boxWidth']))

        #Paint with matches:
        im[:,:,0][tPImage==1] = 0
        im[:,:,1][tPImage==1] = 1
        im[:,:,2][tPImage==1] = 0

        fNImage = falsePositives.reshape((imageDict['boxHeight'], imageDict['boxWidth']))

        #Paint with matches:
        im[:,:,0][fNImage==1] = 1
        im[:,:,1][fNImage==1] = 0
        im[:,:,2][fNImage==1] = 0

        ax.imshow(im, interpolation = 'none')
        ax.axis('off')

    ax4 = fig.add_subplot(1,4,len(exampleIndices)+1)
    ax4.imshow(legend)
    ax4.axis('off');

    yHat = rule(X)

    cm, accuracy, recall, precision = computeConfusionMatrix(y, yHat, verbose = True)


