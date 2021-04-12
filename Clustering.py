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
#personal_centrosinvestigacion= 198

personal = [5651, 5367, 1566, 2514, 4418, 2948, 2749, 927, 3091, 1981, 1513, 885, 2103, 1941, 3539, 348, 1625, 1430]

anos = ["2020", "2019", "2018", "2017", "2016", "2015", "2014"]

Recursos = ["Electricidad", "Agua", "Gas"]

Centros=["ETSI Industriales","ETS Arquitectura","ETS Edificación","ETSI Informáticos","ETSI Aeronáutica y del Espacio","ETSI Agronómica Alimentario y de Biosistema",
"ETSI Caminos Canales y Puertos","ETSI Civil","ETSI Diseño Industrial","ETSI Minas y Energía","ETSI Montes Forestal y del Medio Natural",
"ETSI Navales","ETSI Sistemas de Telecomunicación","ETSI Sistemas Informáticos","ETSI Telecomunicación","ETSI Topografía Geodesia y Cartografía","INEF","Rectorado"]


data={'Centro':['x'],'Consumo':['xxxxxx'], 'Personal':['xxxxx'],'año':['xxxx']}
df_data = pd.DataFrame(data)

#Filtrado de los datos que nos interesan.

#inicio bucles


# bucle Recurso
for Recurso in Recursos:
    print(Recurso)
    i = 0
    # bucle Centro
    for Centro in Centros:
        if Centro == "ETSI Industriales":
            Personal = personal [i]
            i += 1
            # bucle Año
        for ano in anos: 

            Datos = pd.read_csv('Consumo.csv', sep=',', header=0, )

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

            print(Centro + " " + str(Gasto) + " " + str(Personal) + " " + ano)
            linea = {'Centro':Centro,'Consumo':Gasto,'Personal':Personal,'año':ano}
            df_data=df_data.append(linea,ignore_index=True)
            #fin bucles
# %%