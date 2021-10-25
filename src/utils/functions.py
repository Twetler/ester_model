import yaml
from src.experiments.experiments import Experiment
import matplotlib.pyplot as plt


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


def plot_results(sol):
    t = sol['t']
    Ca = sol['y'][0]
    Cb = sol['y'][1]
    Ce = sol['y'][2]
    Cw = sol['y'][3]

    plt.plot(t, Ca, label='A')
    plt.plot(t, Cb, label='B')
    plt.plot(t, Ce, label='E')
    plt.plot(t, Cw, label='W')
    plt.legend()
    plt.title('Perfil de reação de esterificação C(t) ')
    plt.xlabel('t (min)')
    plt.ylabel('C (mol/L)')
    plt.show()

    return 0

