from model.models import ModelGroup
from src.utils.functions import *
import numpy as np
# from scipy.integrate import solve_ivp
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import accuracy_score
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
    group_sqerror = list()
    all_sqerrors = list()
    conc_profile = list()
    experiment_label = list()
    run_id = list()
    active_run = 0
    len_total = len(A_range) * len(B_range) * len(model_A.experiments)

    for A in A_range:
        for B in B_range:

            A = 3.36e6
            B = 157.9

            group_sqerror = 0
            for experiment in model_A.experiments:
                active_run += 1
                C0 = [experiment.ca_0, experiment.cb_0, experiment.ce_0, experiment.cw_0]

                # print(f'Running experiment {experiment.name} with:\n' +
                #       f'A: {A}\n' +
                #       f'B: {B}')
                experiment.conc_profileB = converter(
                    input_arr=experiment.conversion,
                    C0=experiment.cb_0,
                    to='C'
                )
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

                pred_conversion = converter(sol['y'][1], experiment.cb_0, to='X')
                conc_profile.append(C)
                plot_results(experiment.time, experiment.conversion, pred_conversion, name=experiment.name)
                exp_msqerror = mse(
                    y_true=experiment.conversion,
                    y_pred=pred_conversion  # sol[][1] means Cb
                )
                print(f'Running : {active_run * 100 / len_total}% ')
                run_id.append(active_run)
                A_list.append(A)
                B_list.append(B)
                all_sqerrors.append(exp_msqerror)
                experiment_label.append(experiment.name)

            # A_list.append(A)
            # B_list.append(B)
            # all_sqerrors.append(group_sqerror)

    results_dataframe = pd.DataFrame(
        zip(
            run_id,
            A_list,
            B_list,
            all_sqerrors,
            experiment_label
        )
        , columns=['id', 'A', 'B', 'MSE', 'experiment']
    )
    results_overview = results_dataframe.groupby(
        by=['A', 'B']
    ).sum().sort_values(
        by=['MSE']
    ).reset_index()

    plot3d(
        np.asarray(results_overview['A']),
        np.asarray(results_overview['B']),
        np.power(
            np.asarray(results_overview['MSE']), -1
        )
    )
    results_overview[['A', 'B', 'id', 'MSE']].to_csv(path_or_buf='src/runs/run13.csv')

    print('end')
# plot_group_conversion(model_A, ['ASP_70_1', 'ASP_80_1', 'ASP_70_3', 'ASP_80_3'], 'Conversão para o grupo ASP')
