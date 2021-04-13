#%%
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot
ano = "2019"
k = 3
Datos = pd.read_csv('Clustering_Electricidad.csv', sep=',', header=0, )
X=Datos[Datos.año == ano]
etiqueta = X.Centro
X.pop('Centro')
X.pop('año')
X.Consumo = pd.to_numeric(X.Consumo)
X.Personal = pd.to_numeric(X.Personal)
X_array = np.array(X)

print(X_array)
kmeans = KMeans(n_clusters=k)
y_pred = kmeans.fit_predict(X)
y_color = st
i=0
for i in range(len(y_pred)):
    if y_pred[i] == 0:
        #verde
        y_color[i] = "00cc44"
    if y_pred[i] == 1:
        #naranja
         y_color[i] ="ff7700"
    if y_pred[i] == 2:
        #rojo   
         y_color[i] ="ff0000"    
#kmeans.cluster_centers_
pyplot.scatter(X.Consumo, X.Personal, s=none)


# %%
