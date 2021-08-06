# EpyNN/nnlibs/network/hyperparameters.py
# Related third party imports
import numpy as np

# Local application/library specific imports
from nnlibs.commons.schedule import schedule_functions


def model_hyperparameters(model):
    """Schedule learning rate for each layer in model.

    :param model: An instance of EpyNN network.
    :type model: :class:`nnlibs.network.models.EpyNN`
    """
    for layer in model.layers:

        if layer.se_hPars == None:
            se_hPars = layer.se_hPars = model.se_hPars
        else:
            se_hPars = layer.se_hPars

        layer.se_hPars, layer.lrate = schedule_lrate(se_hPars, model.epochs)

    return None


def schedule_lrate(se_hPars, training_epochs):
    """Learning rate schedule.

    :param se_hPars: Hyperparameters settings for layer
    :type se_hPars: dict

    :param training_epochs: Number of training epochs for model
    :type training_epochs: int

    :return: Updated settings for layer hyperparameters
    :rtype: dict

    :return: Scheduled learning rate for layer
    :rtype: list
    """

    e = se_hPars['epochs'] = training_epochs
    lr = se_hPars['learning_rate']
    epc = se_hPars['cycle_epochs']
    d = se_hPars['cycle_descent']
    k = se_hPars['decay_k']

    se_hPars['cycle_number'] = n = 1 if not epc else e // epc

    # Default decay
    if k == 0:
        # 0.005% of initial lr for last epoch in cycle
        k = se_hPars['decay_k'] = 10 / epc

    hPars = (e, lr, n, k, d, epc)

    lrate = schedule_functions(se_hPars['schedule'], hPars)

    return se_hPars, lrate