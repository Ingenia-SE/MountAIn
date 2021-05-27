#%%
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
ano = "2020"
k = 4

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

Datos = pd.read_csv('Clustering_Electricidad.csv', sep=',', header=0, )
X=Datos[Datos.año == ano]
etiqueta = X.Centro
X.pop('Centro')
X.pop('año')
X.Consumo = pd.to_numeric(X.Consumo)
X.Consumo = NormalizeData(X.Consumo)
X.Personal = pd.to_numeric(X.Personal)
X.Personal = NormalizeData(X.Personal)
X_array = np.array(X)

print(X_array)
kmeans = KMeans(n_clusters=k)
y_pred = kmeans.fit_predict(X)

colores = ["#00cc44",  # Verde
           "#33c1ff",  # Azul
           "#ff7700",  # Naranja
           "#f97cf1",  # Rosa
           "#ff0000"   # Rojo
          ]
plt.scatter(X.Consumo, X.Personal,X.Consumo*1000, c=np.take(colores, y_pred))
etiqueta.reset_index(drop=True, inplace=True)
X.Consumo.reset_index(drop=True, inplace=True)
X.Personal.reset_index(drop=True, inplace=True)
for i in range(len(etiqueta)):
    plt.text(X.Consumo[i]+0.01, X.Personal[i]-0.015,etiqueta[i],fontsize=8)
# %%
