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

        def model_proposal(t, C, A, B, T, Ccat, CTIres, CTIacid):
            params = param_loader()['reaction_parameters']
            Keq = params['equilibrium_k']
            Ead = params['direct_activation_energy']
            R = params['k_boltz']

            Ca = C[0]
            Cb = C[1]
            Ce = C[2]
            Cw = C[3]

            dCadt = -(B * Ccat * CTIres + Ccat * CTIacid * A) * exp(-Ead / (R * T)) * (Ca * Cb - Ce * Cw / Keq)
            dCbdt = -(B * Ccat * CTIres + Ccat * CTIacid * A) * exp(-Ead / (R * T)) * (Ca * Cb - Ce * Cw / Keq)
            dCedt = (B * Ccat * CTIres + Ccat * CTIacid * A) * exp(-Ead / (R * T)) * (Ca * Cb - Ce * Cw / Keq)
            dCwdt = (B * Ccat * CTIres + Ccat * CTIacid * A) * exp(-Ead / (R * T)) * (Ca * Cb - Ce * Cw / Keq)

