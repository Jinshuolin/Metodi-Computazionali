import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dati_kepler2 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv')

nomi_colonne = np.array(dati_kepler2.columns)
print ("I nomi delle colonne sono ", "\n")

q = len(nomi_colonne)

for i in range (0, q):
    print (nomi_colonne[i], "  ")


#Dobbiamo fare grafico del flusso in funzione del tempo

ax = dati_kepler2["TIME"]
ay = dati_kepler2["SAP_FLUX"]
plt.errorbar (ax,ay,yerr =dati_kepler2["SAP_FLUX_ERR"],fmt= "o")
plt.xlabel("Time")
plt.ylabel("Sap_Flux")
plt.show()

plt.savefig("Flusso nel tempo.pdf")

minimo = dati_kepler2.loc[(dati_kepler2["TIME"] > 939) & (dati_kepler2["TIME"] < 940)]
plt.plot ( minimo["TIME"], minimo["SAP_FLUX"])
plt.show()
