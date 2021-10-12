from utils.functions import param_loader


class TModel:
    def __init__(self, experiments_list: list):
        self.experiments = list()
        self.exps_list = ['S9_70_1', 'S9_80_1', 'S9_70_3', 'S9_80_3',
                          'ASP_70_1', 'ASP_80_1', 'ASP_70_3', 'ASP_80_3',
                          'RL_70_1', 'RL_80_1', 'RL_70_3', 'RL_80_3']
        for exp in experiments_list:
            if exp.name in self.exps_list:
                self.experiments.append(exp)

        def run(self):
        # Reads only the experiments being used
        all_params = param_loader()
