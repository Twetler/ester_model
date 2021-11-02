import yaml
from src.experiments.experiments import Experiment
import matplotlib.pyplot as plt
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


def plot_results(t, x_true, x_pred):
    # plt.plot(t, Ca, label='Ca_pred')
    plt.plot(t, x_pred, label='Cb_pred')
    # plt.plot(t, Ce, label='Ce_pred')
    # plt.plot(t, Cw, label='Cw_pred')
    plt.plot(t, x_true, label='Cb_real')
    plt.legend()
    plt.title('Conversão X(t) ')
    plt.xlabel('t (min)')
    plt.ylabel('X')
    plt.show()

    return 0


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
    ax.set_zlabel("MSE * -1")
    ax.view_init(-90, 10)

    plt.show()

    return 0

