class Experiment:
    def __init__(self, conversion_arr, experiment_name):
        self.name = experiment_name
        self.time = [5, 15, 30, 45, 60, 75, 90, 105, 120]
        self.volume = 0.35
        self.ca_0 = 2.703 / self.volume
        self.cb_0 = 1.802 / self.volume
        self.ce_0 = 0
        self.cw_0 = 1e-9 / self.volume
        if len(conversion_arr) > 9:
            # Then it has additional information
            self.has_additional_info = True
            self.conversion = conversion_arr[0:9]
            self.temperature = conversion_arr[9]
            self.h_ions_per_mass = conversion_arr[10]
            self.catalyst_conc = conversion_arr[11]
            self.ion_exchange_cap = conversion_arr[12]
        else:
            self.has_additional_info = False
            self.conversion = conversion_arr

    def __str__(self):
        if self.has_additional_info:
            return print(
                'Experiment Name: ', self.name,
                '\n Volume: ', self.volume,
                '\n Time Array: ', self.time,
                '\n Conversions: ', self.conversion,
                '\n Temperature: ', self.temperature,
                '\n H Ions Per Mass: ', self.h_ions_per_mass,
                '\n Catalyst Concentration: ', self.catalyst_conc,
                '\n Ion Exchange Capacity: ', self.ion_exchange_cap
                )
        else:
            return print(
                'Experiment Name: ', self.name,
                '\n Time Array: ', self.time,
                '\n Conversions: ', self.conversion
                )


