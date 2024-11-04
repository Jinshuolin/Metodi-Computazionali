import reco as r
import numpy as np
import pandas as pd

p0 = pd.read_csv ("https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M0.csv")
p1 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M1.csv')
p2 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M2.csv')
p3 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M3.csv')


sensori0 = np.empty(0)
sensori1 = np.empty(0)
sensori2 = np.empty(0)
sensori3 = np.empty(0)
if len(p0) > len(p1):
    print ("Coso")
q = len(p0)
for i in range ( q):
    coso0 =r.Hit ( 0, p0['det_id'][i], p0['hit_time'][i])
    sensori0= np.append(sensori0, coso0)
    coso1 =r.Hit ( 1, p1['det_id'][i], p1['hit_time'][i])
    coso2 =r.Hit ( 2, p2['det_id'][i], p2['hit_time'][i])
    coso3 =r.Hit ( 3, p3['det_id'][i], p3['hit_time'][i])
    sensori1 = np.append(sensori1, coso1)
    sensori

    

