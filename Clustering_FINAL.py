#%%
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
ano = "2014"
k = 4

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

Datos = pd.read_csv('Clustering_Agua.csv', sep=',', header=0, )
X=Datos[Datos.año == ano]
etiqueta = X.Centro
X.pop('Centro')
X.pop('año')
X.Consumo = pd.to_numeric(X.Consumo)
X.Consumo = NormalizeData(X.Consumo)
X.Personal = pd.to_numeric(X.Personal)
X.Personal = NormalizeData(X.Personal)
X_array = np.array(X)

#print(X_array)
kmeans = KMeans(n_clusters=k)
y_pred = kmeans.fit_predict(X)

colores = ["#00cc44",  # Verde
           "#33c1ff",  # Azul
           "#ff7700",  # Naranja
           "#f97cf1",  # Rosa
           "#ff0000"   # Rojo
          ]
plt.rcParams["figure.figsize"] = (30,15)
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.scatter(X.Consumo, X.Personal,X.Consumo*3000 + 100, c=np.take(colores, y_pred))
etiqueta.reset_index(drop=True, inplace=True)
X.Consumo.reset_index(drop=True, inplace=True)
X.Personal.reset_index(drop=True, inplace=True)
plt.xlabel("More consumption" + r'$\longrightarrow$', fontsize=25)
plt.ylabel("More efficiency" + r'$\longrightarrow$', fontsize=25)
plt.xticks(np.array([0. , 0.2, 0.4, 0.6, 0.8, 1. ]))
plt.xlim((-0.01,1.3))
plt.ylim((-0.05,1.1))
for i in range(len(etiqueta)):
    plt.text(X.Consumo[i]+0.02*X.Consumo[i]+0.01, X.Personal[i]-0.005,etiqueta[i],fontsize=int(16*X.Consumo[i]+9))
nombre = 'Clustering_' + ano + '_water' + '.png'
plt.savefig(nombre)
# %%
