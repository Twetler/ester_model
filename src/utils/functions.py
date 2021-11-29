import yaml
from src.experiments.experiments import Experiment
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def param_loader() -> list:
    with open('src/config/parameters.yaml') as file:
        parameters_list = yaml.load(file, Loader=yaml.FullLoader)
        return parameters_list


def experiment_loader() -> list:
    with open('src/config/experiments.yaml') as file:
        experiment_list = yaml.load(file, Loader=yaml.FullLoader)
        return experiment_list


def experiment_init(experiments) -> list:
    initialized_experiments = list()
    for name in experiments['experimental_data'].keys():
        conversion = experiments['experimental_data'][str(name)]
        experiment = Experiment(
            conversion_arr=conversion,
            experiment_name=name
        )
        initialized_experiments.append(experiment)
    return initialized_experiments


def plot_results(t, x_true, x_pred, name):
    # plt.plot(t, Ca, label='Ca_pred')
    plt.plot(t, x_pred, label='Pred')
    # plt.plot(t, Ce, label='Ce_pred')
    # plt.plot(t, Cw, label='Cw_pred')
    plt.plot(t, x_true, label='Real')
    plt.legend()
    plt.title(f'{name}')
    plt.xlabel('t (min)')
    plt.ylabel('Xb')
    plt.ylim(0, 1)
    plt.grid()
    plt.show()

    return 0


def plot_group_conversion(model, group: list, title: str):
    for experiment in model.experiments:
        if experiment.name in group:
            plt.plot(experiment.time, experiment.conversion, label=experiment.name)
    plt.legend()
    plt.title(title)
    plt.xlabel('t (min)')
    plt.ylabel('X')
    plt.ylim(0, 1)
    plt.grid()
    plt.show()


def converter(input_arr, C0, to='X'):
    """
    Converts array from concentration into conversion and likewise
        Parameters:
        to (str): To concentration ('C') or conversion ('X')
        C0 (float): Initial concentration (mol/L)
        concentration_arr (array): Array containing the current concentration

        Returns:
        conversion_arr: Array containing converted conversion array
       """
    final_arr = list()
    if to == 'C':
        for element in input_arr:
            x = element
            final_arr.append(
                C0 * (1 - x)
            )
    if to == 'X':
        for element in input_arr:
            C = element
            final_arr.append(
                (C0 - C) / C0
            )

    return final_arr


def plot3d(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(x, y, z)
    plt.xlabel("A")
    plt.ylabel("B")
    ax.set_zlabel("1/MSE")
    ax.view_init(elev=10, azim=45)

    plt.show()

    return 0


def plot_selected_profiles(model, exp_group, A, B):
    for experiment in model.experiments:
        C0 = [experiment.ca_0, experiment.cb_0, experiment.ce_0, experiment.cw_0]

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
