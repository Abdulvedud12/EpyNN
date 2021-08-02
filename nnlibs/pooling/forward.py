# EpyNN/nnlibs/pooling/forward.py
# Related third party imports
import numpy as np


def initialize_forward(layer, A):
    """Forward cache initialization.

    :param layer: An instance of pooling layer.
    :type layer: :class:`nnlibs.pooling.models.Pooling`

    :param A: Output of forward propagation from previous layer
    :type A: :class:`numpy.ndarray`

    :return: Input of forward propagation for current layer
    :rtype: :class:`numpy.ndarray`

    :return:
    :rtype: :class:`numpy.ndarray`
    """
    X = layer.fc['X'] = A

    Z = np.empty(layer.fs['Z'])

    return X, Z


def pooling_forward(layer, A):
    """Forward propagate signal to next layer.
    """
    # (1) Initialize cache
    X, Z = initialize_forward(layer, A)

    #
    for m in range(layer.d['m']):
        # Loop through image rows
        for h in range(layer.d['oh']):
            ih1 = h * layer.d['s']
            ih2 = ih1 + layer.d['w']
            # Loop through row columns
            for w in range(layer.d['ow']):
                iw1 = w * layer.d['s']
                iw2 = iw1 + layer.d['w']
                #
                for n in range(layer.d['n']):
                    X = layer.fc['X'][m, ih1:ih2, iw1:iw2, n]
                    Z[m, h, w, n] = layer.pool(X)

    return Z   # To next layer
