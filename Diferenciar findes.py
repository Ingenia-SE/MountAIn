
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from matplotlib import pyplot
######################################################
#      la primera parte es el filtrado de datos que ya teniamos
#      hecho lo de diferenciar los fines de semana esta al final
######################################################

consumos = pd.read_csv('consumosUPM.csv', header=0, squeeze=True)

def filtro(recurso):
    datos_filtrados = consumos[consumos['Recurso'] == recurso]
    datos_filtrados = datos_filtrados[['Campus' ,'NombreCentro' ,'Centro' ,'TipoCentro' ,'FechaInicioLectura' ,'FechaFinLectura' ,'ConsumoTotal']]
    datos_filtrados = datos_filtrados[datos_filtrados['ConsumoTotal'] != '0' ]


    datos_filtrados = datos_filtrados.reset_index(drop=True)
    defectos =[]

    for i in range(len(datos_filtrados)):
        if type(datos_filtrados['FechaInicioLectura'][i]) is str:  # intentar hacer con el dropna()
            try:
                datos_filtrados['FechaInicioLectura'][i] = datetime.strptime(datos_filtrados['FechaInicioLectura'][i],
                                                                             '%Y-%m-%d').date()
            except:
                print("algo ha fallado con el formato")


        else:
            print(datos_filtrados['FechaInicioLectura'][i])
            defectos.append(i)

        if type(datos_filtrados['FechaFinLectura'][i]) is str:
            try:
                datos_filtrados['FechaFinLectura'][i] = datetime.strptime(datos_filtrados['FechaFinLectura'][i],
                                                                          '%Y-%m-%d').date()
            except:
                print("Something went wrong")

        else:
            defectos.append(i)

    defectos = list(dict.fromkeys(defectos))
    datos_filtrados = datos_filtrados.drop(index=defectos)
    datos_filtrados = datos_filtrados.reset_index(drop=True)
    #     datos_filtrados = datos_filtrados.sort_values('FechaInicioLectura')
    return datos_filtrados


# In[2]:


electricidad = filtro("Electricidad")
# agua = filtro("Agua")
# gas = filtro("Gas")
# agua.head(20)
print(electricidad.head())#formato fecha año mes dia

######################################################
#               DIFERENCIAR FINES DE SEMANA
######################################################
for i in range(5):
    inicio = electricidad['FechaInicioLectura'][i]
    final = electricidad['FechaFinLectura'][i]
    dias_validos = np.busday_count(inicio, final + timedelta(days=1)) #la funcion no incluye la fecha final por eso se inclue el timedelta que suma un dia
    consumo_diario = np.int64(electricidad['ConsumoTotal'][i])/dias_validos #conversion de consumo a int porque es un string en el dataframe
    while inicio <= final:
      if np.is_busday()== True#funcion para saber si la fecha es dia de la semana o no
        '''Aqui seria meter en el dataframe nuevo los consumos diarios para cada intervalo'''
        inicio = inicio + timedelta(days=1)


    print (inicio)
    print (final)
    print(electricidad['ConsumoTotal'][i])
    print (dias_validos)
    print (consumo_diario)