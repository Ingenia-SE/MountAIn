#%%
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot
personal_industriales= 5367
Centro ="ETSI Industriales"
ano = "2019"
Recurso = "Electricidad"
data={'Centro':['x'],'Consumo':['xxxxxx'], 'Personal':['xxxxx'],'año':['xxxx']}
df_data = pd.DataFrame(data)

#Filtrado de los datos que nos interesan.
Datos = pd.read_csv('Consumo.txt', delimiter=',', header=0, )

#inicio bucles
# bucle Recurso
    # bucle Centro
        # bucle Año

Datos=Datos[Datos.Recurso==Recurso]

Datos=Datos[Datos.NombreCentro==Centro]

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
Datos_ano=Datos[Datos.AñoFinLectura == ano]
Gasto_ano=Datos_ano.ConsumoTotal
Gasto=pd.to_numeric(Gasto_ano).sum()
if Centro == "ETSI Industriales":
    Personal = personal_industriales
print(Centro + " " + str(Gasto) + " " + str(Personal) + " " + ano)
linea = {'Centro':Centro,'Consumo':Gasto,'Personal':Personal,'año':ano}
df_data=df_data.append(linea,ignore_index=True)
#fin bucles
# %%
