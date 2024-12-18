import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pianeti = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/ExoplanetsPars_2024.csv', comment = '#')
print (pianeti["pl_bmassj"])
coso = np.sort (pianeti["pl_bmassj"])
ax = np.logspace(coso[0], coso[5765])
ay = np.logspace (pianeti["pl_orbper"][0], pianeti["pl_orbper"][5765])
plt.plot(ax, ay, "o")
plt.show()

