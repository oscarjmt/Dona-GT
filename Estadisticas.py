import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date
import Defensiva as df

#Función para generar el data fram de donaciones realizadas.
def donacionesRealizadas():
    donacionesDF = pd.DataFrame(pd.read_csv("DonacionesRealizadas.csv", sep=",", encoding="latin-1", header=None,
                                            names=["Donador", "Solicitante", "Nombres", "Apellidos", "Monto", "Fecha"]))
    donacionesDF["Fecha"] = pd.to_datetime(donacionesDF["Fecha"], format="%d/%m/%Y")
    return(donacionesDF)

#Función para mostrar el total de donaciones realizadas por mes.
def donadorEst(listaDonador):
    donador = listaDonador[3] #Se extrae el nombre de usuario de la lista de donador.
    donacionesDF = donacionesRealizadas() #Se guarda el data frame que retorna la función donacionesRealizadas.
    #Se hace que solo se tengan datos de los útlimos 12 meses.
    hoy = date.today()
    try:
        desde = datetime(hoy.year-1, hoy.month+1, 1)
    except:
        desde = datetime(hoy.year, 1, 1)
    mask = (donacionesDF['Fecha'] > desde)
    donacionesDF = donacionesDF.loc[mask]
    #Se filtra para que solo salgan los datos del donador que ingresó.
    donacionesDF = donacionesDF[donacionesDF["Donador"]==donador]
    #Se crea una columna por mes y año de la fecha, y se agrupa por mes.
    donacionesDF["Mes"] = pd.DatetimeIndex(donacionesDF["Fecha"]).month
    donacionesDF["Year"] = pd.DatetimeIndex(donacionesDF["Fecha"]).year
    agrupado = donacionesDF.groupby("Mes").aggregate({'Monto':np.sum,'Year':np.average})
    #Se obtiene el nombre del mes.
    meses = pd.DataFrame({"Mes": [1,2,3,4,5,6,7,8,9,10,11,12],
                          "Meses": ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]})
    combinado = pd.merge(meses, agrupado, on=["Mes","Mes"])
    #Se ordenan por año, para que último registro sea el mes actual.
    ordenado = combinado.sort_values("Year").drop(["Year"], axis=1)
    #Se grafica
    ordenado.plot(x="Meses", y="Monto", kind="bar")
    plt.title("TOTAL DE DONACIONES REALIZADAS POR MES")
    plt.show()

#Función que obtiene el total donado del donador.
def totalDonado(listaDonador):
    donador = listaDonador[3] #Se extrae el nombre de usuario de la listaDonador.
    donacionesDF = donacionesRealizadas() #Se guarda el data frame que retorna la función donacionesRealizadas.
    donacionesDF = donacionesDF.groupby("Donador").sum() #Se agrupa por donador con la función sum.
    total = donacionesDF.loc[donador][0] #Se obtien el total donado del donador ingresado.
    #Se transforma el total en forma más amigable al usuario.
    montoDR = str(total)
    totalDonado = df.transformarMonto(montoDR) 
    return(totalDonado)

#Función para mostrar el total de donaciones recibidas por mes.
def solicitanteEst(listaSolicitante):
    solicitante = listaSolicitante[6] #Se obtiene el nombre de usuario de la listaSoliciatnte.
    donacionesDF = donacionesRealizadas() #Se guarda el data frame que retorna la función donacionesRealizadas.
    #Se hace que solo se tengan datos de los útlimos 12 meses.
    hoy = date.today()
    try:
        desde = datetime(hoy.year-1, hoy.month+1, 1)
    except:
        desde = datetime(hoy.year, 1, 1)
    mask = (donacionesDF['Fecha'] > desde)
    donacionesDF = donacionesDF.loc[mask]
    #Se filtra para que solo salgan los datos del donador que ingresó.
    donacionesDF = donacionesDF[donacionesDF["Solicitante"]==solicitante]
    #Se crea una columna por mes y año de la fecha, y se agrupa por mes.
    donacionesDF["Mes"] = pd.DatetimeIndex(donacionesDF["Fecha"]).month
    donacionesDF["Year"] = pd.DatetimeIndex(donacionesDF["Fecha"]).year
    agrupado = donacionesDF.groupby("Mes").aggregate({'Monto':np.sum,'Year':np.average})
    #Se obtiene el nombre del mes.
    meses = pd.DataFrame({"Mes": [1,2,3,4,5,6,7,8,9,10,11,12],
                          "Meses": ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]})
    combinado = pd.merge(meses, agrupado, on=["Mes","Mes"])
    #Se ordenan por año, para que último registro sea el mes actual.
    ordenado = combinado.sort_values("Year").drop(["Year"], axis=1)
    #Se grafica
    ordenado.plot(x="Meses", y="Monto", kind="bar")
    plt.title("TOTAL DE DONACIONES RECIBIDAS POR MES")
    plt.show()

#Función que obtiene el total recibido del solicitante.
def totalRecibido(listaSolicitante):
    solicitante = listaSolicitante[6] #Se extrae el nombre de usuario de la listaSolicitante.
    donacionesDF = donacionesRealizadas() #Se guarda el data frame que retorna la función donacionesRealizadas.
    donacionesDF = donacionesDF.groupby("Solicitante").sum() #Se agrupa por solicitante con la función sum.
    total = donacionesDF.loc[solicitante][0]  #Se obtien el total recibido del solicitante ingresado.
    #Se transforma el total en forma más amigable al usuario.
    montoDR = str(total)
    totalDonado = df.transformarMonto(montoDR)
    return(totalDonado)