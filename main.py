from model.models import TModel
from src.utils.functions import *
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

if __name__ == '__main__':
    all_experiments = experiment_init(experiments=experiment_loader())
    model_A = TModel(experiments_list=all_experiments)
    all_params = param_loader()

    A_range = np.linspace(
        start=all_params['iterational_parameters']['lower_A_bound'],
        stop=all_params['iterational_parameters']['upper_A_bound'],
        num=all_params['iterational_parameters']['steps']
        )
    B_range = np.linspace(
        start=all_params['iterational_parameters']['lower_B_bound'],
        stop=all_params['iterational_parameters']['upper_B_bound'],
        num=all_params['iterational_parameters']['steps']
        )

    for A in A_range:
        for B in B_range:
            for experiment in model_A.experiments:
                C0 = [experiment.ca_0, experiment.cb_0, experiment.ce_0, experiment.cw_0]
                experiment.model_proposal(t, C, A, B,
                                          experiment.temperature,
                                          experiment.catalyst_conc,
                                          experiment.ion_exchange_cap,
                                          experiment.h_ions_per_mass)
                sol =
    print('end')
