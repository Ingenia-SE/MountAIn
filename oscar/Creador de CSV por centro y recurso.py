#%%
import pandas as pd
import numpy as np
from dateutil.rrule import rrule, MONTHLY

from datetime import datetime
from matplotlib import pyplot

#Filtrado de los datos que nos interesan.
Datos = pd.read_csv('consumosUPM.csv', delimiter=',', header=0, )
Datos = Datos[Datos.Recurso=="Agua"]

Datos = Datos[Datos.NombreCentro=="ETSI Industriales"]

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
end_date = date(2020, 6, 9)
for single_date in daterange(start_date, end_date):
    dia_sem=single_date.strftime("%a")
    intervalo_inf=Datos[Datos.FechaInicioLectura <= pd.to_datetime(single_date)]
    intervalo=intervalo_inf[intervalo_inf.FechaFinLectura > pd.to_datetime(single_date)]
    Consumo_intervalo=pd.to_numeric(intervalo["ConsumoTotal"]).sum()
    if Consumo_intervalo > 0:
        fecha_fin=intervalo['FechaFinLectura'].iloc[0]
        fecha_ini=intervalo['FechaInicioLectura'].iloc[0]
        Numero_dias_validos_intervalo = np.busday_count(fecha_ini.date(), fecha_fin.date() + timedelta(days=1))
        Consumo_dia = Consumo_intervalo / Numero_dias_validos_intervalo
        if np.is_busday(single_date) == True:
            new_row={'Dia_semana':dia_sem,'Dia':str(single_date),'ConsumoDia':Consumo_dia}
            df_data=df_data.append(new_row,ignore_index=True)
            single_date= single_date+ timedelta(days=1)
        else:
            new_row = {'Dia_semana': dia_sem, 'Dia': str(single_date), 'ConsumoDia': 0}
            df_data = df_data.append(new_row, ignore_index=True)
            single_date= single_date+ timedelta(days=1)
    else:
        print ("ERROR")

df_data=df_data[1:]

df_data=df_data.set_index('Dia')
df_data.index = pd.to_datetime(df_data.index)
df_mensual = df_data.resample('MS').sum()
print (df_mensual.head(10))
df_mensual= df_mensual.reset_index()
print (df_mensual.head(10))
df_mensual.to_csv('Industriales.csv',index=False)

