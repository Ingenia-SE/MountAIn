import numpy as np
import pandas as pd
import matplotlib as plt
from datetime import datetime



datos = pd.read_csv('consumosUPM.csv')
eliminar= ['Dirección','TipoCentro','FechaEmisionFactura','ConsumoP1',
           'ConsumoP2','ConsumoP3','ConsumoP4','ConsumoP5','ConsumoP6',
           'AñoFinLectura']
datos1= datos.drop(columns=eliminar)
datos2=datos[datos['ConsumoTotal'] != '0']
electricidad=datos2[datos2['Recurso'] == 'Electricidad']

datos5=pd.to_datetime(electricidad['FechaInicioLectura'], format='%d/%m/%Y %H:%M')


datos5.info()

