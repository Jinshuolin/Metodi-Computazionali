import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

p0 = pd.read_csv ('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M0.csv')
p1 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M1.csv')
p2 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M2.csv')
p3 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M3.csv')

#Produrre istogramma dei tempi
diff0 = np.array ( np.diff (p0.hit_time))
plt.hist ( diff0, bins = 100, log = True )
plt.show()
