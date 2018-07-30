# Support Functions For Learning To See Series
# Welch Labs

import matplotlib.colors as mcolors
import numpy as np

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

def makeGrayScale(imageDict):
    '''Create a grayscale image with 3 identical channels'''

    im = np.zeros((imageDict['boxHeight'], imageDict['boxWidth'], 3))
    im[:,:,0] = 1./255*imageDict['image'][imageDict['boxEdges'][2]:imageDict['boxEdges'][3], \
                                       imageDict['boxEdges'][0]:imageDict['boxEdges'][1]] 
    im[:,:,1] = 1./255*imageDict['image'][imageDict['boxEdges'][2]:imageDict['boxEdges'][3], \
                                       imageDict['boxEdges'][0]:imageDict['boxEdges'][1]]
    im[:,:,2] = 1./255*imageDict['image'][imageDict['boxEdges'][2]:imageDict['boxEdges'][3], \
                                       imageDict['boxEdges'][0]:imageDict['boxEdges'][1]]
    
    return im