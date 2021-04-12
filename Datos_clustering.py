#%%
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot

#Filtrado de los datos que nos interesan.
Datos = pd.read_csv('Consumo.txt', delimiter=',', header=0, )
Datos=Datos[Datos.Recurso=="Electricidad"]

Datos=Datos[Datos.NombreCentro=="ETSI Industriales"]

Datos.pop('Campus')
Datos.pop('Dirección')
Datos.pop('Centro')
Datos.pop('TipoCentro')
Datos.pop('FechaEmisionFactura')
Datos.pop('ConsumoP1')
Datos.pop('ConsumoP2')
Datos.pop('ConsumoP3')
Datos.pop('ConsumoP4')
Datos.pop('ConsumoP5')
Datos.pop('ConsumoP6')
#Datos.pop('AñoFinLectura')

Datos_2019=Datos[Datos.AñoFinLectura == "2019"]
Gasto_2019=Datos_2019.ConsumoTotal
#print (Gasto_2019)
Gasto=pd.to_numeric(Gasto_2019).sum()
print(Gasto)
# %%
