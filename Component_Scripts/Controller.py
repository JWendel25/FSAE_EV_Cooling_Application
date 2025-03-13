class Controller():
    
    def __init__(self, Inlet_Temp_Min, Voltage_Max, Curent_Max, Power_Max, Average_Efficiency, Flow_Rate, Pressure_Drop):
        self.T_in = Inlet_Temp_Min                                              # [C] - Maximum Inlet Temperature
        self.V_max = Voltage_Max                                                # [V] - Maximum Voltage Possible
        self.I_max = Curent_Max                                                 # [A] - Maximum Current Possible
        if Power_Max != None : self.P_max = Power_Max                           # [W] - Maximum Power Possible
        else : self.P_max = self.V_max * self.I_max                             # [W] - Calculates Max Power from Max Voltage & Current if not directly passed
        self.Eff_avg = Average_Efficiency                                       # [-] - Average Efficiency (decimal format)
        self.Flow = Flow_Rate                                                   # [L/min] - Coolant Flow Rate corresponding to known Pressure Drop
        self.Head = Pressure_Drop                                               # [bar] - Coolant Pressure Drop through device corresponding to known Flow Rate
        # Calculated Properties
        self.Q_dot_gen_max = self.P_max * (1 - self.Eff)                        # [W] - Maximum Heat Generated (from Max Power)
        self.C = self.Head / (self.Flow ** 2)                                   # [-] - Pressure Drop Coefficient (from known point given in spec sheet)
    
    def Head_Loss(self, Flow):                                                  # Returns Pressure Drop [bar] for given Flow Rate [L/min]
        loss = self.C * (Flow ** 2)
        return loss