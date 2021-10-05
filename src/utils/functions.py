import yaml
from src.experiments.experiments import Experiment


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

