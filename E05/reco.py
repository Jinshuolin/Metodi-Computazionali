import numpy as np

class Hit:
    def __init__ (self, idm, ids, time):
        self.id_modulo = idm
        self.id_sensore = ids
        self.time_stamp = time
    def __gt__(self, other):
        return self.time > other.time
    def __lt__ (self, other):
        return self.time < other.time
    def __eq__ (self, other):
        return self.time_stamp == other.time_stamp and self.id_modulo == other.id_modulo and self.id_sensore == other.id_sensore
    
    
    
