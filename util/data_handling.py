# Support Functions For Learning To See Series
# Welch Labs

import numpy as np

def extractFeatures(imageDict, whichImage = 'image1bit', dist = 4):
    '''
    Extract 9 by 9 grid and finger/not finger label from imageDict.
    '''
    img = imageDict[whichImage]

    featuresList = []
    target = np.zeros(imageDict['numPointsInBox'])
    counter = 0

    for i in np.arange(imageDict['boxEdges'][2], imageDict['boxEdges'][3]):
        for j in np.arange(imageDict['boxEdges'][0], imageDict['boxEdges'][1]):
            f = img[i-dist:i+dist+1, j-dist:j+dist+1]

            fVec = f.ravel()
            featuresList.append(fVec)

            #Check and see if this is a finger pixel or not:
            if np.max(np.sum(imageDict['allFingerPoints'] == [i, j], 1)) == 2:
                target[counter] = 1

            counter = counter +1
            
    features = np.vstack((featuresList))
    
    return features, target

def extractExamplesFromList(imageList, whichImage = 'image1bit', dist = 4):
    '''
    Extract indivudual examples from list of imageDicts
    '''

    allFeaturesList = []
    allTargetList = []

    for i, imageDict in enumerate(imageList):
        features, target = extractFeatures(imageDict, whichImage = whichImage, dist = dist)
        allFeaturesList.append(features)
        allTargetList.append(target)

    x = np.vstack((allFeaturesList))
    y = np.hstack((allTargetList))
    
    return x, y

def findUniqueRowsAndCount(a):
    '''Find and count unique rows in numpy array'''

    b = np.ascontiguousarray(a).view(np.dtype((np.void, a.dtype.itemsize * a.shape[1])))
    _, idx, counts = np.unique(b, return_index=True, return_counts = True)
    
    aUnique = a[idx].astype('int')
    
    return aUnique, idx, counts

    import matplotlib.colors as mcolors