#%%
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot

personal_industriales= 5651
personal_arquitectura= 5367
personal_edificacion= 1566
personal_informaticos= 2514
personal_aeronauticos= 4418
personal_agronomos= 2948
personal_caminos= 2749
personal_civil= 927
personal_diseñoind= 3091
personal_minasyenergia= 1981
personal_montes= 1513
personal_navales= 885
personal_sistemastelec= 2103
personal_sistemasinf= 1941
personal_telecomunicacion= 3539
personal_topografos= 348
personal_INEF= 1625
personal_rectorado= 1430
personal_centrosinvestigacion= 198

Centro ="ETSI Industriales"
ano = "2019"
Recurso = "Agua"
data={'Centro':['x'],'Consumo':['xxxxxx'], 'Personal':['xxxxx'],'año':['xxxx']}
df_data = pd.DataFrame(data)

#Filtrado de los datos que nos interesan.
Datos = pd.read_csv('Consumo.csv', sep=',', header=0, )

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