#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot
 
consumos = pd.read_csv('consumosUPM.csv', header=0, squeeze=True)

def filtro(recurso):
    datos_filtrados = consumos[consumos['Recurso'] == recurso]
    datos_filtrados = datos_filtrados[['Campus','NombreCentro','Centro','TipoCentro','FechaInicioLectura','FechaFinLectura','ConsumoTotal']]
    datos_filtrados = datos_filtrados[datos_filtrados['ConsumoTotal'] != 0]
    datos_filtrados = datos_filtrados.reset_index(drop=True)
    defectos =[]
    
    for i in range(len(datos_filtrados)):
        if type(datos_filtrados['FechaInicioLectura'][i]) is str:
            try:
                datos_filtrados['FechaInicioLectura'][i] = datetime.strptime(datos_filtrados['FechaInicioLectura'][i],'%d/%m/%Y %H:%M').date()
            except:
                try:
                    datos_filtrados['FechaInicioLectura'][i] = datetime.strptime(datos_filtrados['FechaInicioLectura'][i],'%m/%d/%Y %H:%M').date()
                except:
                    print("Something went wrong")

        else:
            defectos.append(i)
            
        if type(datos_filtrados['FechaFinLectura'][i]) is str:
            try:
                datos_filtrados['FechaFinLectura'][i] = datetime.strptime(datos_filtrados['FechaFinLectura'][i],'%d/%m/%Y %H:%M').date()
            except:
                try:
                    datos_filtrados['FechaFinLectura'][i] = datetime.strptime(datos_filtrados['FechaFinLectura'][i],'%m/%d/%Y %H:%M').date()
                except:
                    print("Something went wrong")

        else:
            defectos.append(i)
            
    defectos = list(dict.fromkeys(defectos))
    datos_filtrados = datos_filtrados.drop(index = defectos)
    datos_filtrados = datos_filtrados.reset_index(drop=True)
    return datos_filtrados




electricidad = filtro("Electricidad")
agua = filtro("Agua")
gas = filtro("Gas")



