# from utils.functions import param_loader
# from utils.functions import converter
import math
import numpy as np


class Experiment:
    def __init__(self, conversion_arr, experiment_name):

        self.name = experiment_name
        self.time = [5, 15, 30, 45, 60, 75, 90, 105, 120]
        self.volume = 0.35
        self.ca_0 = 2.703 / self.volume
        self.cb_0 = 1.802 / self.volume
        self.ce_0 = 0
        self.cw_0 = 1e-9 / self.volume
        self.conc_profileB = []

        if len(conversion_arr) > 9:
            # Then it has additional information
            self.has_additional_info = True
            self.conversion = np.asarray(conversion_arr[0:9])
            self.temperature = float(conversion_arr[9])
            self.h_ions_per_mass = float(conversion_arr[10])
            self.catalyst_conc = conversion_arr[11] / self.volume
            self.ion_exchange_cap = conversion_arr[12]
        else:
            self.has_additional_info = False
            self.conversion = conversion_arr

    # def __str__(self):
    #     if self.has_additional_info:
    #         return print(
    #             'Experiment Name: ', self.name,
    #             '\n Volume: ', self.volume,
    #             '\n Time Array: ', self.time,
    #             '\n Conversions: ', self.conversion,
    #             '\n Temperature: ', self.temperature,
    #             '\n H Ions Per Mass: ', self.h_ions_per_mass,
    #             '\n Catalyst Concentration: ', self.catalyst_conc,
    #             '\n Ion Exchange Capacity:', self.ion_exchange_cap,
    #             '\n'
    #         )
    #     else:
    #         return print(
    #             'Experiment Name: ', self.name,
    #             '\n Time Array: ', self.time,
    #             '\n Conversions: ', self.conversion
    #         )

    @staticmethod
    def model_proposal(t, C, A, B, T, Ccat, CTIres, CTIacid, Keq, Ead, R):

        Ca = C[0]
        Cb = C[1]
        Ce = C[2]
        Cw = C[3]

        dCadt = -(B * Ccat * CTIres + Ccat * CTIacid * A) * math.exp(-Ead / (R * T)) * (Ca * Cb - Ce * Cw / Keq)
        dCbdt = -(B * Ccat * CTIres + Ccat * CTIacid * A) * math.exp(-Ead / (R * T)) * (Ca * Cb - Ce * Cw / Keq)
        dCedt = (B * Ccat * CTIres + Ccat * CTIacid * A) * math.exp(-Ead / (R * T)) * (Ca * Cb - Ce * Cw / Keq)
        dCwdt = (B * Ccat * CTIres + Ccat * CTIacid * A) * math.exp(-Ead / (R * T)) * (Ca * Cb - Ce * Cw / Keq)

        return dCadt, dCbdt, dCedt, dCwdt
