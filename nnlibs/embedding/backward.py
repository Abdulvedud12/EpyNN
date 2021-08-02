# EpyNN/nnlibs/embedding/backward.py


def initialize_backward(layer, dA):
    """Backward cache initialization.

    :param layer: An instance of embedding layer.
    :type layer: :class:`nnlibs.embedding.models.Embedding`

    :param dA: Output of backward propagation from next layer
    :type dA: :class:`numpy.ndarray`

    :return: Input of backward propagation for current layer
    :rtype: :class:`numpy.ndarray`
    """
    dX = layer.bc['dX'] = dA

    return dX


def embedding_backward(layer, dA):
    """Backward propagate signal to previous layer.
    """
    dX = initialize_backward(layer, dA)

    dA = layer.bc['dA'] = dX

    return dA    # To previous layer
