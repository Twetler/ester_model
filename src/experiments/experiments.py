class Experiment:
    def __init__(self, conversion_arr):
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
            self.time = [5, 15, 30, 45, 60, 75, 90, 105, 120]
