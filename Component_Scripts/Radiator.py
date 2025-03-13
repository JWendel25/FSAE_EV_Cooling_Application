class Radiator():
    
    def __init__(self, Efficiency):
        self.Eff = Efficiency                                                   # eta-NTU Method efficeincy
        self.Q_dot = None
    
    def Q_dot(self,                                                             # Returns Heat transfered [W] between coolint & air
              T_coolant_i, m_dot_coolant, c_p_coolant,                          # Coolant Properties: Inlet Temp [C], Flow Rate [kg/s], Specific Heat [J/kg*C]
              T_air_i, m_dot_air, c_p_air):                                     # Air Properties: Inlet Temp [C], Flow Rate [kg/s], Specific Heat [J/kg*C]
        
        Q_dot_max = m_dot_air * c_p_air * (T_coolant_i - T_air_i)
        self.Q_dot = Q_dot_max * self.Eff
        return self.Q_dot
    
    def T_exit(self,                                                            # Returns Outlet Temperature [C] of fluid after passing though radiator
               T_i, m_dot, c_p):                                                # Fluid Properties: Inlet Temp [C], Flow Rate [kg/s], Specific Heat [J/kg*C]
        
        T_e = T_i + (self.Q_dot / (m_dot * c_p))
        return T_e
        # May want to house in actual main? May not want to store Q in self, but in main?