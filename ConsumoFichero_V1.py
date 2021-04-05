#%%
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot

#Filtrado de los datos que nos interesan.
Datos = pd.read_csv('Consumo.txt', delimiter=',', header=0, )
Datos=Datos[Datos.Recurso=="Agua"]

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
Datos.pop('AñoFinLectura')
Datos.FechaInicioLectura = pd.to_datetime(Datos.FechaInicioLectura)
Datos.FechaFinLectura = pd.to_datetime(Datos.FechaFinLectura)
#creación CSV diario
#Dia de la semana (L-D)
#Día (fecha)
#Consumo/día

#creamos dataframe desde 01/01/2014 hasta 31/12/2020
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2015, 1, 1)
end_date = date(2015, 2, 1)
for single_date in daterange(start_date, end_date):
    print (single_date)
    intervalo_inf=Datos[Datos.FechaInicioLectura < pd.to_datetime(single_date)]
    intervalo=intervalo_inf[intervalo_inf.FechaFinLectura > pd.to_datetime(single_date)]
    Consumo_intervalo=pd.to_numeric(intervalo["ConsumoTotal"]).sum()
    fecha_fin=intervalo['FechaFinLectura'].iloc[0]
    fecha_ini=intervalo['FechaInicioLectura'].iloc[0]
    Numero_dias_intervalo = fecha_fin - fecha_ini
    #print(intervalo)
    print("Numero dias intervalo= " + str(Numero_dias_intervalo.days))
    print("Consumo_intervalo = " + str(Consumo_intervalo))
    Consumo_dia = Consumo_intervalo / int(Numero_dias_intervalo.days)
    print("Consumo_dia = " + str(Consumo_dia))

#print(Datos)
# %%
