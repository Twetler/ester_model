from model.models import ModelGroup
from src.utils.functions import *
import numpy as np
from scipy.integrate import solve_ivp
from sklearn.metrics import mean_squared_error as mse
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    all_experiments = experiment_init(experiments=experiment_loader())
    model_A = ModelGroup(experiments_list=all_experiments)
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

    params = all_params['reaction_parameters']
    Keq = params['equilibrium_k']
    Ead = params['direct_activation_energy']
    R = params['k_boltz']

    A_list = list()
    B_list = list()
    sqerror = list()
    conc_profile = list()

    for A in A_range:
        for B in B_range:
            for experiment in model_A.experiments:
                C0 = [experiment.ca_0, experiment.cb_0, experiment.ce_0, experiment.cw_0]
                print(f'Running experiment {experiment.name} with:\n' +
                      f'A: {A}\n' +
                      f'B: {B}')
                sol = solve_ivp(fun=experiment.model_proposal,
                                t_span=[0, 120],
                                y0=C0,
                                method='RK45',
                                args=(A,
                                      B,
                                      experiment.temperature,
                                      experiment.catalyst_conc,
                                      experiment.ion_exchange_cap,
                                      experiment.h_ions_per_mass,
                                      Keq,
                                      Ead,
                                      R
                                      ),
                                t_eval=experiment.time
                                )
                C = sol['y']

                conc_profile.append(C)
                plot_results(sol, experiment.conc_profileB)
                msqerror = mse(y_true=experiment.time,
                               y_pred=sol['y'][3])  # sol[][3] means Cw
                # print(f'MSE: {msqerror} \n')

                sqerror.append(msqerror)  # Generating results in array
                A_list.append(A)
                B_list.append(B)

    print('end')
