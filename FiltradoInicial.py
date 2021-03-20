import numpy as np
import pandas as pd
import matplotlib as plt
from datetime import datetime
''' HASTA LA LINEA 13 ELIMINA LAS COLUMNAS INNECESARIAS Y LOS ERRORES 
    IGNORAR LO QUE ESTA COMENTADO'''

datos = pd.read_csv('consumosUPM.csv')
eliminar= ['Dirección','TipoCentro','FechaEmisionFactura','ConsumoP1',
           'ConsumoP2','ConsumoP3','ConsumoP4','ConsumoP5','ConsumoP6',
           'AñoFinLectura']
datos1= datos.drop(columns=eliminar)
datos2=datos[datos['ConsumoTotal'] != '0']
datos3=datos2[datos2['Recurso'] == 'Electricidad']

'''datos5=pd.to_datetime(datos3['FechaInicioLectura'], format='%d/%m/%Y')
fecha = datetime.fromtimestamp(datos5)

print ((datos5[5]))
print (type(fecha))'''
datos1.info()