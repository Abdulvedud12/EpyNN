#EpyNN/nnlive/mnist_database/settings.py


dataset = {
    'N_SAMPLES': 5000,
    'dataset_name': 'mnist_database',
    'dataset_save': True,
    'dtrain_relative': 2,
    'dtest_relative': 1,
    'dval_relative': 1,
    'batch_number': 5,
}


config = {
    'experiment_name': 'MNIST_DATABASE',
    'logs_frequency': 1,
    'logs_frequency_display': 5,
    'model_save': True,
    'plot_display': True,
    'plot_save': False,
    'directory_clear': True,
    'dataset_target': 1,
    'metrics_target': 'accuracy',
    'metrics_list': ['accuracy','CE','CCE','MSE','MAE','RMSLE','KLD'],
    'metrics_plot': ['accuracy','CCE']
}


hPars = {
    'training_epochs': 1000,
    'learning_rate': 0.1,
    'schedule_mode': 'exp_decay',
    'decay_k': 0.001,
    'cycling_n': 1,
    'descent_d': 1,

    'regularization_l2': 0,
    'regularization_l1': 0,

    'softmax_temperature': 1,
    'ELU_alpha': 0.01,
    'LRELU_alpha': 1,
    'min_epsilon': 1e-9,
}
