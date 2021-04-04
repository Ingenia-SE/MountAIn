#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from matplotlib import pyplot
 
consumos = pd.read_csv('consumosUPM bien.csv', header=0, squeeze=True)

def filtro(recurso):
    datos_filtrados = consumos[consumos['Recurso'] == recurso]
    datos_filtrados = datos_filtrados[['Campus','NombreCentro','Centro','TipoCentro','FechaInicioLectura','FechaFinLectura','ConsumoTotal']]
    datos_filtrados = datos_filtrados[datos_filtrados['ConsumoTotal'] != '0' ]
    
    
    datos_filtrados = datos_filtrados.reset_index(drop=True)
    defectos =[]
    
    for i in range(len(datos_filtrados)):
        if type(datos_filtrados['FechaInicioLectura'][i]) is str: #intentar hacer con el dropna()
            try:
                datos_filtrados['FechaInicioLectura'][i] = datetime.strptime(datos_filtrados['FechaInicioLectura'][i],'%Y-%m-%d').date()
            except:
                print("algo ha fallado con el formato")
                   

        else:
            print(datos_filtrados['FechaInicioLectura'][i])
            defectos.append(i)
            
        if type(datos_filtrados['FechaFinLectura'][i]) is str:
            try:
                datos_filtrados['FechaFinLectura'][i] = datetime.strptime(datos_filtrados['FechaFinLectura'][i],'%Y-%m-%d').date()
            except:
                print("Something went wrong")

        else:
            defectos.append(i)
            
    defectos = list(dict.fromkeys(defectos))
    datos_filtrados = datos_filtrados.drop(index = defectos)
    datos_filtrados = datos_filtrados.reset_index(drop=True)
#     datos_filtrados = datos_filtrados.sort_values('FechaInicioLectura')
    return datos_filtrados



# In[2]:


electricidad = filtro("Electricidad")
#agua = filtro("Agua")
#gas = filtro("Gas")
#agua.head(20)
# electricidad.head(20)


# In[3]:


def desglose(dataframe):
    datos_desglosados = pd.DataFrame(columns=['Campus','NombreCentro','Centro','TipoCentro','FechaLectura','DiaSemana','ConsumoTotal'])
    for i in range(len(dataframe)):
        
#     for i in range(100) #---->por si quereis probarlo sin que el ordenador se os pase media hora pensando xD
        a = dataframe['FechaFinLectura'][i]
        b = dataframe['FechaInicioLectura'][i]
        c= datos_desglosados.shape[0] #esto me saca el numero de filas en el nuevo dataframe
        
        datos_desglosados.loc[c]=dataframe.loc[i]
        datos_desglosados.loc[c,'FechaLectura']=b
        datos_desglosados.loc[c,'DiaSemana']=b.strftime("%a")

        d=b
        for j in range((a-b).days):
            c+=1
            d += timedelta(days=1)                    
            datos_desglosados.loc[c]=dataframe.loc[i]
            datos_desglosados.loc[c,'FechaLectura']=d
            datos_desglosados.loc[c,'DiaSemana']=d.strftime("%a")
            
    return datos_desglosados


# In[ ]:


ejemplo = desglose(electricidad)

ejemplo.head(50)


# In[ ]:





# In[ ]:




