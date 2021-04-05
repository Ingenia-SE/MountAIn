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
data={'Dia_semana':['L'],'Dia':['0000-00-00'],'ConsumoDia':[0]}
df_data = pd.DataFrame(data)
#print(df_data)
#creamos dataframe desde 01/01/2014 hasta 31/12/2020
from datetime import timedelta, date
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
#FECHA INICIO Y FIN DEL BUCLE
start_date = date(2014, 1, 1)
end_date = date(2021, 1, 1)
for single_date in daterange(start_date, end_date):
    #print (single_date.weekday())
    if single_date.weekday() == 0:
        dia_sem='L'
    if single_date.weekday() == 1:
        dia_sem='M'
    if single_date.weekday() == 2:
        dia_sem='X'
    if single_date.weekday() == 3:
        dia_sem='J'
    if single_date.weekday() == 4:
        dia_sem='V'
    if single_date.weekday() == 5:
        dia_sem='S'
    if single_date.weekday() == 6:
        dia_sem='D'
    intervalo_inf=Datos[Datos.FechaInicioLectura <= pd.to_datetime(single_date)]
    intervalo=intervalo_inf[intervalo_inf.FechaFinLectura > pd.to_datetime(single_date)]
    Consumo_intervalo=pd.to_numeric(intervalo["ConsumoTotal"]).sum()
    if Consumo_intervalo > 0:
        fecha_fin=intervalo['FechaFinLectura'].iloc[0]
        fecha_ini=intervalo['FechaInicioLectura'].iloc[0]
        Numero_dias_intervalo = fecha_fin - fecha_ini
        #print(intervalo)
        #print("Numero dias intervalo= " + str(Numero_dias_intervalo.days))
        #print("Consumo_intervalo = " + str(Consumo_intervalo))
        Consumo_dia = Consumo_intervalo / int(Numero_dias_intervalo.days)
        #print("Consumo_dia = " + str(Consumo_dia))
        new_row={'Dia_semana':dia_sem,'Dia':str(single_date),'ConsumoDia':Consumo_dia}
        df_data=df_data.append(new_row,ignore_index=True)
    else:
        print ("ERROR")
        print (single_date)
#print(Datos)
#print(df_data)
df_data.to_csv('Industriales.csv',index=False)
# %%
