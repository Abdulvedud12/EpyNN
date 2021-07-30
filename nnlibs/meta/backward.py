# EpyNN/nnlibs/meta/backward.py


def model_backward(model, dA):
    """.

    :param A:
    :type A:
    :return:
    :rtype:
    """
    for layer in reversed(model.layers):

        dA = layer.backward(dA)

        layer.compute_gradients()
        layer.update_parameters()

    return None
