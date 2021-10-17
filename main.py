from model.models import TModel
from src.utils.functions import *
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    all_experiments = experiment_init(experiments=experiment_loader())
    model_A = TModel(experiments_list=all_experiments)
    all_params = param_loader()

    A_range = np.linspace(
        start=float(all_params['iterational_parameters']['lower_A_bound']),
        stop=float(all_params['iterational_parameters']['upper_A_bound']),
        num=int(all_params['iterational_parameters']['steps'])
    )
    B_range = np.linspace(
        start=float(all_params['iterational_parameters']['lower_B_bound']),
        stop=float(all_params['iterational_parameters']['upper_B_bound']),
        num=int(all_params['iterational_parameters']['steps'])
    )

    for A in A_range:
        for B in B_range:
            for experiment in model_A.experiments:
                C0 = [experiment.ca_0, experiment.cb_0, experiment.ce_0, experiment.cw_0]
                print(f'Running experiment {experiment.name} with:' +
                      '')
                solve_ivp()
                experiment.model_proposal(t=experiment.time,
                                          C=C0,
                                          A=A,
                                          B=B,

                                          T=experiment.temperature,
                                          Ccat=experiment.catalyst_conc,
                                          CTIres=experiment.ion_exchange_cap,
                                          CTIacid=experiment.h_ions_per_mass)
    print('end')
model_proposal(t, C, A, B, T, Ccat, CTIres, CTIacid)
