from tkinter import *
from tkinter import messagebox
import re
import csv #Se importa tkinter, los messagebox, re, time y csv.
import math
from datetime import datetime
from datetime import date

#Función defensiva para registrar un donador.
def defenRegistroD(nombresD, apellidosD, correoD, usuarioD, passwordD, tarjetaD, listaD):  
    
    #Programación defensiva para que el nombre sea en forma de título.
    if nombresD.istitle() == False:
        warningNomD = True
        messagebox.showwarning("Nombres", "Los nombres son un campo necesario, y deben empezar con mayúscula.")
    else:
        warningNomD = False
    
    #Programación defensiva para que el apellido sea en forma de título.
    if apellidosD.istitle() == False:
        warningApeD = True
        messagebox.showwarning("Apellidos", "Los apellidos son un campo necesario, y deben empezar con mayúscula.")
    else:
        warningApeD = False
    
    #Programación defensiva para que el correo tenga formato de e-mail.
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correoD.lower()):
        warningCorD = False
    else:
        warningCorD = True
        messagebox.showwarning("Correo", "El correo es un campo necesario, y debe ser válido (ej: ejemplo123@email.com).")
    
    #Programación defensiva para que el usuario sea válido.
    if (usuarioD.isidentifier() == False) or (len(usuarioD) > 20):
        warningUsuD = True
        messagebox.showwarning("Nombre de usuario", "El usuario es un campo necesario, y debe ser válido. No puede tener espacios, solo letras(a-z), dígitos(0-9) o guión bajo(_). No puede empezar con un número ni tener más de 20 caracteres. (ej: ejemplo_123)")
    else:
        warningUsuD = False
    
    #Programación defensiva para que la contraseña sea entre 4 y 20 caracteres.
    if (len(passwordD) >= 4) and (len(passwordD) <= 20):
        warningPassD = False
    else:
        warningPassD = True
        messagebox.showwarning("Contraseña", "La contraseña es un campo necesario, y debe ser válido. No puede tener comas(,) y debe tener entre 4 a 20 caracteres.")
    
    #Programación defensiva para que el número de tarjeta sea entre 13 y 19 dígitos.
    if (len(tarjetaD) >= 13) and (len(tarjetaD) <= 19) and (tarjetaD.isdigit() == True):
        warningTarD = False
    else:
        warningTarD = True
        messagebox.showwarning("Tarjeta de crédito", "El numero de tarjeta no es válido. Tome en cuenta que no debe utilizar espacios.")
    
    #Programación defensiva para que no hayan comas.
    for i in range(len(listaD)):
        comasListaD = list(listaD[i])
        if "," in comasListaD:
            comasLD = True
            break
        else:
            comasLD = False
    
    listaCuentasD = []
    with open("CuentasDonador.csv", "r") as archivoCD:
        leer = csv.reader(archivoCD, delimiter=',')
        for filas in leer:
            listaCuentasD.append(filas)
        archivoCD.close()
    
    #Programación defensiva por si el correo, usuario o contraseña ya estan registrados.
    for i in range(len(listaCuentasD)):
        if listaCuentasD[i][2] == correoD:
            warningCorD2 = True
            messagebox.showwarning("Correo", "El correo ingresado ya tiene una cuenta registrada.")
            break
        else:
            warningCorD2 = False 
    for i in range(len(listaCuentasD)):
        if listaCuentasD[i][3] == usuarioD:
            warningUsuD2 = True
            messagebox.showwarning("Nombre de usuario", "El nombre de usuario ingresado ya está usado.")
            break
        else:
            warningUsuD2 = False
    for i in range(len(listaCuentasD)):
        if listaCuentasD[i][4] == passwordD:
            warningPassD2 = True
            messagebox.showwarning("Contraseña", "La contraseña ingresada ya está usada.")
            break
        else:
            warningPassD2 = False
    
    #Si no hay un problema la función retorna False, de lo contrario retorna True.
    if (warningNomD == True) or (warningApeD == True) or (warningCorD == True) or (warningUsuD == True) or (warningPassD == True) or (warningTarD == True):
        defenRegistroD = False
    elif (warningCorD2 == True) or (warningUsuD2 == True) or (warningPassD2 == True):
        defenRegistroD = False
    elif comasLD == True:
        messagebox.showwarning("Uso de comas", "No puede usar comas, si necesita separar información puede usar el punto(.) o algún otro signo de puntuación.")
        defenRegistroD = False
    else:
        defenRegistroD = True
    return(defenRegistroD)

#Función defensiva para registrar un solicitante.
def defenRegistroS(nombresS, apellidosS, parentescoS, ocupacionS, telefonoS, correoS, usuarioS, passwordS, dpiS, listaS):
    
    #Programación defensiva para que el nombre sea en forma de título.
    if nombresS.istitle() == False:
        warningNomS = True
        messagebox.showwarning("Nombres", "Los nombres son un campo necesario, y deben empezar con mayúscula.")
    else:
        warningNomS = False
    
    #Programación defensiva para que el apellido sea en forma de título.
    if apellidosS.istitle() == False:
        warningApeS = True
        messagebox.showwarning("Apellidos", "Los apellidos son un campo necesario, y deben empezar con mayúscula.")
    else:
        warningApeS = False
    
    #Programación defensiva para que el parentesco sea en forma de título.
    if parentescoS.istitle() == False:
        warningParS = True
        messagebox.showwarning("Parentesco", "El parentesco es un campo necesario, y deben empezar con mayúscula.")
    else:
        warningParS = False
    
    #Programación defensiva para que la ocupación sea en forma de título.
    if ocupacionS.istitle() == False:
        warningOcuS = True
        messagebox.showwarning("Ocupación", "La ocupación es un campo necesario, y deben empezar con mayúscula.")
    else:
        warningOcuS = False
    
    #Programación defensiva para que el telefono sean 8 dígitos.
    if (len(telefonoS) == 8) and (telefonoS.isdigit() == True):
        warningTelS = False
    else:
        warningTelS = True
        messagebox.showwarning("Teléfono", "El número de teléfono no es válido. Tome en cuenta que debe escribir solo dígitos, sin espacios ni guiones.")
    
    #Programación defensiva para que el correo tenga formato de e-mail.
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correoS.lower()):
        warningCorS = False
    else:
        warningCorS = True
        messagebox.showwarning("Correo", "El correo es un campo necesario, y debe ser válido (ej: ejemplo123@email.com).")
    
    #Programación defensiva para que el usuario sea válido.
    if (usuarioS.isidentifier() == False) or (len(usuarioS) > 20):
        warningUsuS = True
        messagebox.showwarning("Nombre de usuario", "El usuario es un campo necesario, y debe ser válido. No puede tener espacios, solo letras(a-z), dígitos(0-9) o guión bajo(_). No puede empezar con un número ni tener más de 20 caracteres. (ej: ejemplo_123)")
    else:
        warningUsuS = False
    
    #Programación defensiva para que la contraseña sea entre 4 y 20 caracteres.
    if (len(passwordS) >= 4) and (len(passwordS) <= 20):
        warningPassS = False
    else:
        warningPassS = True
        messagebox.showwarning("Contraseña", "La contraseña es un campo necesario, y debe ser válido. No puede tener comas(,) y debe tener entre 4 a 20 caracteres.")
    
    #Programación defensiva para que el DPI sean 13 dígitos.
    if (len(dpiS) == 13) and (dpiS.isdigit() == True):
        warningDpiS = False
    else:
        warningDpiS = True
        messagebox.showwarning("No. de DPI", "El numero de DPI no es válido. Tome en cuenta que no debe utilizar espacios.")
    
    #Programación defensiva para que no hayan comas.
    for i in range(len(listaS)):
        comasListaS = list(listaS[i])
        if "," in comasListaS:
            comasLS = True
            break
        else:
            comasLS = False
    
    listaCuentasS = []
    with open("CuentasSolicitante.csv", "r") as archivoCS:
        leer = csv.reader(archivoCS, delimiter=',')
        for filas in leer:
            listaCuentasS.append(filas)
        archivoCS.close()
    
    #Programación defensiva por si el correo, usuario, contraseña o dpi ya estan registrados.
    for i in range(len(listaCuentasS)):
        if listaCuentasS[i][5] == correoS:
            warningCorS2 = True
            messagebox.showwarning("Correo", "El correo ingresado ya tiene una cuenta registrada.")
            break
        else:
            warningCorS2 = False
    for i in range(len(listaCuentasS)):
        if listaCuentasS[i][6] == usuarioS:
            warningUsuS2 = True
            messagebox.showwarning("Nombre de usuario", "El nombre de usuario ingresado ya está usado.")
            break
        else:
            warningUsuS2 = False
    for i in range(len(listaCuentasS)):
        if listaCuentasS[i][7] == passwordS:
            warningPassS2 = True
            messagebox.showwarning("Contraseña", "La contraseña ingresada ya está usada.")
            break
        else:
            warningPassS2 = False
    for i in range(len(listaCuentasS)):
        if listaCuentasS[i][8] == dpiS:
            warningDpiS2 = True
            messagebox.showwarning("Número de DPI", "Ya hay una persona registrada con este número de DPI.")
            break
        else:
            warningDpiS2 = False
    
    #Si no hay un problema la función retorna False, de lo contrario retorna True.
    if (warningNomS == True) or (warningApeS == True) or (warningParS == True) or (warningOcuS == True) or (warningTelS == True) or (warningCorS == True) or (warningUsuS == True) or (warningPassS == True) or (warningDpiS == True):
        defenRegistroS = False
    elif comasLS == True:
        messagebox.showwarning("Uso de comas", "No puede usar comas, si necesita separar información puede usar el punto(.) o algún otro signo de puntuación.")
        defenRegistroS = False
    elif (warningCorS2 == True) or (warningUsuS2 == True) or (warningPassS2 == True) or (warningDpiS2 == True):
        defenRegistroS = False     
    else:
        defenRegistroS = True
    return(defenRegistroS)

#Función defensiva para registrar los datos del niño.
def defenRegistroN(nombresN, apellidosN, sexoN, alturaN, pesoN, departamentoN, municipioN, fechaN, recursosN, listaN):
    
    #Programación defensiva para que el nombre sea en forma de título.
    if nombresN.istitle() == False:
        warningNomN = True
        messagebox.showwarning("Nombres", "Los nombres son un campo necesario, y deben empezar con mayúscula.")
    else:
        warningNomN = False
    
    #Programación defensiva para que el apellido sea en forma de título.
    if apellidosN.istitle() == False:
        warningApeN = True
        messagebox.showwarning("Apellidos", "Los apellidos son un campo necesario, y deben empezar con mayúscula.")
    else:
        warningApeN = False
    
    #Programación defensiva para ver que si se eligió sexo del niño o niña.
    if (sexoN == "Masculino") or (sexoN == "Femenino"):
        warningSexN = False
    else:
        warningSexN = True
        messagebox.showwarning("Sexo", "No ha puesto el sexo del niño.")
    
    #Programación defensiva para que la altura sea un valor numérico y en un rango realista.
    try:
        floatAltura = float(alturaN)
        floatA = True
        if (floatA != True) or (float(alturaN) < 0.2) or (float(alturaN) > 2.5):
            warningAltN = True
            messagebox.showwarning("Altura", "La altura es muy grande o muy pequeña, recuerde que la altura debe estar en metros (ej: 1.35)")
        else:
            warningAltN = False
    except ValueError:
        warningAltN = True
        messagebox.showwarning("Altura", "La altura es un campo necesario, y debe ser un valor numérico.")
    
    #Programación defensiva para que el peso sea un valor numérico y en un rango realista.
    try:
        floatPeso = float(alturaN)
        floatP = True
        if (floatP != True) or (float(pesoN) < 10) or (float(pesoN) > 200):
            warningPesN = True
            messagebox.showwarning("Peso", "El peso es muy grande o muy pequeña, recuerde que el peso debe estar en libras (ej: 52.5)")
        else:
            warningPesN = False
    except ValueError:
        warningPesN = True
        messagebox.showwarning("Peso", "El peso es un campo necesario, y debe ser un valor numérico.")
    
    #Programación defensiva para que el departamento sea en forma de título.
    if departamentoN.istitle() == False:
        warningDepN = True
        messagebox.showwarning("Departamento", "El departamento es un campo necesario, y debe empezar con mayúscula cada palabra.")
    else:
        warningDepN = False
    
    #Programación defensiva para que el municipio sea en forma de título.
    if municipioN.istitle() == False:
        warningMunN = True
        messagebox.showwarning("Municipio", "El municipio es un campo necesario, y deben empezar con mayúscula cada palabra.")
    else:
        warningMunN = False
    
    #Programación defensiva para que la fecha este en el formato requerido.
    try:
        timeFechaN = datetime.strptime(fechaN, "%d/%m/%Y")
        warningFecN = False
    except:
        warningFecN = True
        messagebox.showwarning("Fecha de nacimiento", "La fecha de naciemiento no tiene el formato requerido: dd/mm/aaaa (ej: 21/05/2010)")
    
    hoy = date.today()
    if warningFecN == True:
        warningFecN2 = False
    elif timeFechaN.year > hoy.year:
        warningFecN2 = True
        messagebox.showwarning("Fecha de nacimiento", "La fecha de nacimiento no es posible, aún no ha pasado esa fecha.")
    elif timeFechaN.year == hoy.year:
        if timeFechaN.month > hoy.month:
            warningFecN2 = True
            messagebox.showwarning("Fecha de nacimiento", "La fecha de nacimiento no es posible, aún no ha pasado esa fecha.")
        elif timeFechaN.month == hoy.month:
            if timeFechaN.day > hoy.day:
                warningFecN2 = True
                messagebox.showwarning("Fecha de nacimiento", "La fecha de nacimiento no es posible, aún no ha pasado esa fecha.")
            else:
                warningFecN2 = False
        else:
            warningFecN2 = False
    else:
        warningFecN2 = False
    
    #Programación defensiva para que no deje en blanco este espacio.
    if len(recursosN) > 0:
        warningRecN = False
    else:
        warningRecN = True
        messagebox.showwarning("Recursos que necesita", "Los recursos que necesita es un campo necesario.")
    
    #Programación defensiva para que no hayan comas.
    for i in range(len(listaN)):
        comasListaN = list(listaN[i])
        if "," in comasListaN:
            comasLN = True
            break
        else:
            comasLN = False
    
    #Si no hay un problema la función retorna False, de lo contrario retorna True.
    if (warningNomN == True) or (warningApeN == True) or (warningSexN == True) or (warningAltN == True) or (warningPesN == True) or (warningDepN == True) or (warningMunN == True) or (warningFecN == True) or (warningFecN2 == True) or (warningRecN == True):
        defenRegistroN = False
    elif comasLN == True:
        messagebox.showwarning("Uso de comas", "No puede usar comas, si necesita separar información puede usar el punto(.) o algún otro signo de puntuación.")
        defenRegistroN = False
    else:
        defenRegistroN = True
    return(defenRegistroN)

#Función defensiva para cambiar la contraseña de un donador.
def defenCambiarD(correoD, usuarioD, passwordD):   
    listaCuentasD = []
    with open("CuentasDonador.csv", "r") as archivoCD:
        leer = csv.reader(archivoCD, delimiter=',')
        for filas in leer:
            listaCuentasD.append(filas)
        archivoCD.close()
    
    #Programación defensiva por si el usuario o el correo no estan registrados.
    for i in range(len(listaCuentasD)):
        if listaCuentasD[i][2] == correoD:
            correoRegistradoD = True
            compararCorreoD = i
            break
        else:
            correoRegistradoD = False
            compararCorreoD = "C"        
    if correoRegistradoD == False:
        messagebox.showwarning("Correo", "El correo ingresado no se encuentra registrado, intente de nuevo")
    for i in range(len(listaCuentasD)):
        if listaCuentasD[i][3] == usuarioD:
            usuarioRegistradoD = True
            compararUsuarioD = i
            break
        else:
            usuarioRegistradoD = False
            compararUsuarioD = "U"
    if usuarioRegistradoD == False:
        messagebox.showwarning("Nombre de usuario", "El nombre de usuario ingresado no se encuentra registrado, intente de nuevo.")
    
    #Verifica que el usuario y el correo pertenezcan a la misma cuenta.
    if (correoRegistradoD == True) and (usuarioRegistradoD == True) and (compararCorreoD != compararUsuarioD):
        messagebox.showwarning("Correo y usuario", "El correo no coincide con el nombre de usuario")
    
    #Programación defensiva para que la contraseña sea entre 4 y 20 caracteres.
    if (len(passwordD) >= 4) and (len(passwordD) <= 20):
        cWarningPassD = False
    else:
        cWarningPassD = True
        messagebox.showwarning("Contraseña", "La contraseña es un campo necesario, y debe ser válido. No puede tener comas(,) y debe tener entre 4 a 20 caracteres.")
    
    #Programación defensiva por si la contraseña ya esta registrada.
    for i in range(len(listaCuentasD)):
        if listaCuentasD[i][4] == passwordD:
            cWarningPassD2 = True
            messagebox.showwarning("Contraseña", "La contraseña ingresada ya está siendo usada, asegúrese de que no sea la suya.")
            break
        else:
            cWarningPassD2 = False
    
    #Programación defensiva para que no hayan comas.
    comasCambiarD = list(passwordD)
    if "," in comasCambiarD:
        comasCamD = True
    else:
        comasCamD = False
    
    #Si no hay un problema la función retorna False, de lo contrario retorna True.
    if (correoRegistradoD == False) or (usuarioRegistradoD == False) or (compararCorreoD != compararUsuarioD):
        defenCambiarD = False
    elif (cWarningPassD == True) or (cWarningPassD2 == True):
        defenCambiarD = False
    elif comasCamD == True:
        messagebox.showwarning("Uso de comas", "No puede usar comas, si necesita separar información puede usar el punto(.) o algún otro signo de puntuación.")
        defenCambiarD = False
    else:
        defenCambiarD = True
    return(defenCambiarD)

#Función defensiva para cambiar la contraseña de un solicitante.
def defenCambiarS(correoS, usuarioS, passwordS):   
    listaCuentasS = []
    with open("CuentasSolicitante.csv", "r") as archivoCS:
        leer = csv.reader(archivoCS, delimiter=',')
        for filas in leer:
            listaCuentasS.append(filas)
        archivoCS.close()
    
    #Programación defensiva por si el usuario o el correo no estan registrados.
    for i in range(len(listaCuentasS)):
        if listaCuentasS[i][5] == correoS:
            correoRegistradoS = True
            compararCorreoS = i
            break
        else:
            correoRegistradoS = False
            compararCorreoS = "C"        
    if correoRegistradoS == False:
        messagebox.showwarning("Correo", "El correo ingresado no se encuentra registrado, intente de nuevo") 
    for i in range(len(listaCuentasS)):
        if listaCuentasS[i][6] == usuarioS:
            usuarioRegistradoS = True
            compararUsuarioS = i
            break
        else:
            usuarioRegistradoS = False
            compararUsuarioS = "U"
    if usuarioRegistradoS == False:
        messagebox.showwarning("Nombre de usuario", "El nombre de usuario ingresado no se encuentra registrado, intente de nuevo.")
    
    #Verifica que el usuario y el correo pertenezcan a la misma cuenta.
    if (correoRegistradoS == True) and (usuarioRegistradoS == True) and (compararCorreoS != compararUsuarioS):
        messagebox.showwarning("Correo y usuario", "El correo no coincide con el nombre de usuario")
    
    #Programación defensiva para que la contraseña sea entre 4 y 20 caracteres.
    if (len(passwordS) >= 4) and (len(passwordS) <= 20):
        cWarningPassS = False
    else:
        cWarningPassS = True
        messagebox.showwarning("Contraseña", "La contraseña es un campo necesario, y debe ser válido. No puede tener comas(,) y debe tener entre 4 a 20 caracteres.")
    
    #Programación defensiva por si la contraseña ya esta registrada.
    for i in range(len(listaCuentasS)):
        if listaCuentasS[i][7] == passwordS:
            cWarningPassS2 = True
            messagebox.showwarning("Contraseña", "La contraseña ingresada ya está siendo usada, asegúrese de que no sea la suya.")
            break
        else:
            cWarningPassS2 = False
    
    #Programación defensiva para que no hayan comas.
    comasCambiarS = list(passwordS)
    if "," in comasCambiarS:
        comasCamS = True
    else:
        comasCamS = False
    
    #Si no hay un problema la función retorna False, de lo contrario retorna True.
    if (correoRegistradoS == False) or (usuarioRegistradoS == False) or (compararCorreoS != compararUsuarioS):
        defenCambiarS = False
    elif (cWarningPassS == True) or (cWarningPassS2 == True):
        defenCambiarS = False
    elif comasCamS == True:
        messagebox.showwarning("Uso de comas", "No puede usar comas, si necesita separar información puede usar el punto(.) o algún otro signo de puntuación.")
        defenCambiarS = False
    else:
        defenCambiarS = True
    return(defenCambiarS)

#Función defensiva el login de donador.
def defenLoginD(usuarioD, passwordD):   
    listaCuentasD = []
    with open("CuentasDonador.csv", "r") as archivoCD:
        leer = csv.reader(archivoCD, delimiter=',')
        for filas in leer:
            listaCuentasD.append(filas)
        archivoCD.close()
    
    #Se comprueba que el usuario y la contraseña esten registrados.
    for i in range(len(listaCuentasD)):
        if listaCuentasD[i][3] == usuarioD:
            usuarioRegistradoD = True
            compararUsuarioD = i
            break
        else:
            usuarioRegistradoD = False
            compararUsuarioD = "U" 
    for i in range(len(listaCuentasD)):
        if listaCuentasD[i][4] == passwordD:
            passwordRegistradoD = True
            compararPasswordD = i
            break
        else:
            passwordRegistradoD = False
            compararPasswordD = "P"
    
    #Si no hay un problema la función retorna False, de lo contrario retorna True.
    if (usuarioRegistradoD == False) or (passwordRegistradoD == False) or (compararUsuarioD != compararPasswordD):
        messagebox.showwarning("Usuario y contraseña", "El nombre de usuario ingresado y/o la contraseña son incorrectos.")
        defenLoginD = False
    else:
        defenLoginD = True
    return(defenLoginD)

#Función defensiva el login de solicitante.
def defenLoginS(usuarioS, passwordS):   
    listaCuentasS = []
    with open("CuentasSolicitante.csv", "r") as archivoCS:
        leer = csv.reader(archivoCS, delimiter=',')
        for filas in leer:
            listaCuentasS.append(filas)
        archivoCS.close()
    
    #Se comprueba que el usuario y la contraseña esten registrados.
    for i in range(len(listaCuentasS)):
        if listaCuentasS[i][6] == usuarioS:
            usuarioRegistradoS = True
            compararUsuarioS = i
            break
        else:
            usuarioRegistradoS = False
            compararUsuarioS = "U"
    for i in range(len(listaCuentasS)):
        if listaCuentasS[i][7] == passwordS:
            passwordRegistradoS = True
            compararPasswordS = i
            break
        else:
            passwordRegistradoS = False
            compararPasswordS = "P"
    
    #Si no hay un problema la función retorna False, de lo contrario retorna True.
    if (usuarioRegistradoS == False) or (passwordRegistradoS == False) or (compararUsuarioS != compararPasswordS):
        messagebox.showwarning("Usuario y contraseña", "El nombre de usuario ingresado y/o la contraseña son incorrectos.")
        defenLoginS = False
    else:
        defenLoginS = True
    return(defenLoginS)

#Función defensiva actualizar datos de un donador.
def defenActualizarD(nombresD, apellidosD, correoD, usuarioD, passwordD, tarjetaD, listaD, listaDonador):  
    
    #Programación defensiva para que el nombre sea en forma de título.
    if nombresD.istitle() == False:
        warningNomD = True
        messagebox.showwarning("Nombres", "Los nombres son un campo necesario, y deben empezar con mayúscula.")
    else:
        warningNomD = False
    
    #Programación defensiva para que el apellido sea en forma de título.
    if apellidosD.istitle() == False:
        warningApeD = True
        messagebox.showwarning("Apellidos", "Los apellidos son un campo necesario, y deben empezar con mayúscula.")
    else:
        warningApeD = False
    
    #Programación defensiva para que el correo tenga formato de e-mail.
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correoD.lower()):
        warningCorD = False
    else:
        warningCorD = True
        messagebox.showwarning("Correo", "El correo es un campo necesario, y debe ser válido (ej: ejemplo123@email.com).")
    
    #Programación defensiva para que la contraseña sea entre 4 y 20 caracteres.
    if (len(passwordD) >= 4) and (len(passwordD) <= 20):
        warningPassD = False
    else:
        warningPassD = True
        messagebox.showwarning("Contraseña", "La contraseña es un campo necesario, y debe ser válido. No puede tener comas(,) y debe tener entre 4 a 20 caracteres.")
    
    #Programación defensiva para que el número de tarjeta sea entre 13 y 19 dígitos.
    if (len(tarjetaD) >= 13) and (len(tarjetaD) <= 19) and (tarjetaD.isdigit() == True):
        warningTarD = False
    else:
        warningTarD = True
        messagebox.showwarning("Tarjeta de crédito", "El numero de tarjeta no es válido. Tome en cuenta que no debe utilizar espacios.")
    
    #Programación defensiva para que no hayan comas.
    for i in range(len(listaD)):
        comasListaD = list(listaD[i])
        if "," in comasListaD:
            comasLD = True
            break
        else:
            comasLD = False
    
    listaCuentasD = []
    with open("CuentasDonador.csv", "r") as archivoCD:
        leer = csv.reader(archivoCD, delimiter=',')
        for filas in leer:
            listaCuentasD.append(filas)
        archivoCD.close()
        
    #Programación defensiva por si el correo o contraseña ya estan registrados.
    for i in range(len(listaCuentasD)):
        if (listaCuentasD[i][2] == correoD) and (listaCuentasD[i][2] != listaDonador[2]):
            warningCorD2 = True
            messagebox.showwarning("Correo", "El correo ingresado ya tiene una cuenta registrada.")
            break
        else:
            warningCorD2 = False
    for i in range(len(listaCuentasD)):
        if (listaCuentasD[i][4] == passwordD) and (listaCuentasD[i][4] != listaDonador[4]):
            warningPassD2 = True
            messagebox.showwarning("Contraseña", "La contraseña ingresada ya está usada.")
            break
        else:
            warningPassD2 = False
    
    #Si no hay un problema la función retorna False, de lo contrario retorna True.
    if (warningNomD == True) or (warningApeD == True) or (warningCorD == True) or (warningPassD == True) or (warningTarD == True):
        defenActualizarD = False
    elif (warningCorD2 == True) or (warningPassD2 == True):
        defenActualizarD = False
    elif comasLD == True:
        messagebox.showwarning("Uso de comas", "No puede usar comas, si necesita separar información puede usar el punto(.) o algún otro signo de puntuación.")
        defenActualizarD = False
    else:
        defenActualizarD = True
    return(defenActualizarD)

#Función defensiva actualizar datos de un solicitante.
def defenActualizarS(nombresS, apellidosS, parentescoS, ocupacionS, telefonoS, correoS, usuarioS, passwordS, dpiS, listaS, listaSolicitante):
    
    #Programación defensiva para que el nombre sea en forma de título.
    if nombresS.istitle() == False:
        warningNomS = True
        messagebox.showwarning("Nombres", "Los nombres son un campo necesario, y deben empezar con mayúscula.")
    else:
        warningNomS = False
    
    #Programación defensiva para que el apellido sea en forma de título.
    if apellidosS.istitle() == False:
        warningApeS = True
        messagebox.showwarning("Apellidos", "Los apellidos son un campo necesario, y deben empezar con mayúscula.")
    else:
        warningApeS = False
    
    #Programación defensiva para que el parentesco sea en forma de título.
    if parentescoS.istitle() == False:
        warningParS = True
        messagebox.showwarning("Parentesco", "El parentesco es un campo necesario, y deben empezar con mayúscula.")
    else:
        warningParS = False
    
    #Programación defensiva para que la ocupación sea en forma de título.
    if ocupacionS.istitle() == False:
        warningOcuS = True
        messagebox.showwarning("Ocupación", "La ocupación es un campo necesario, y deben empezar con mayúscula.")
    else:
        warningOcuS = False
    
    #Programación defensiva para que el telefono sean 8 dígitos.
    if (len(telefonoS) == 8) and (telefonoS.isdigit() == True):
        warningTelS = False
    else:
        warningTelS = True
        messagebox.showwarning("Teléfono", "El número de teléfono no es válido. Tome en cuenta que debe escribir solo dígitos, sin espacios ni guiones.")
    
    #Programación defensiva para que el correo tenga formato de e-mail.
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correoS.lower()):
        warningCorS = False
    else:
        warningCorS = True
        messagebox.showwarning("Correo", "El correo es un campo necesario, y debe ser válido (ej: ejemplo123@email.com).")
    
    #Programación defensiva para que la contraseña sea entre 4 y 20 caracteres.
    if (len(passwordS) >= 4) and (len(passwordS) <= 20):
        warningPassS = False
    else:
        warningPassS = True
        messagebox.showwarning("Contraseña", "La contraseña es un campo necesario, y debe ser válido. No puede tener comas(,) y debe tener entre 4 a 20 caracteres.")
    
    #Programación defensiva para que el DPI sean 13 dígitos.
    if (len(dpiS) == 13) and (dpiS.isdigit() == True):
        warningDpiS = False
    else:
        warningDpiS = True
        messagebox.showwarning("No. de DPI", "El numero de DPI no es válido. Tome en cuenta que no debe utilizar espacios.")
    
    #Programación defensiva para que no hayan comas.
    for i in range(len(listaS)):
        comasListaS = list(listaS[i])
        if "," in comasListaS:
            comasLS = True
            break
        else:
            comasLS = False
    
    listaCuentasS = []
    with open("CuentasSolicitante.csv", "r") as archivoCS:
        leer = csv.reader(archivoCS, delimiter=',')
        for filas in leer:
            listaCuentasS.append(filas)
        archivoCS.close()
    
    #Programación defensiva por si el correo, contraseña o dpi ya estan registrados.
    for i in range(len(listaCuentasS)):
        if (listaCuentasS[i][5] == correoS) and (listaCuentasS[i][5]!=listaSolicitante[5]):
            warningCorS2 = True
            messagebox.showwarning("Correo", "El correo ingresado ya tiene una cuenta registrada.")
            break
        else:
            warningCorS2 = False
    for i in range(len(listaCuentasS)):
        if (listaCuentasS[i][7] == passwordS) and (listaCuentasS[i][7]!=listaSolicitante[7]):
            warningPassS2 = True
            messagebox.showwarning("Contraseña", "La contraseña ingresada ya está usada.")
            break
        else:
            warningPassS2 = False
    for i in range(len(listaCuentasS)):
        if (listaCuentasS[i][8] == dpiS) and (listaCuentasS[i][8]!=listaSolicitante[8]):
            warningDpiS2 = True
            messagebox.showwarning("Número de DPI", "Ya hay una persona registrada con este número de DPI.")
            break
        else:
            warningDpiS2 = False
    
    #Si no hay un problema la función retorna False, de lo contrario retorna True.
    if (warningNomS == True) or (warningApeS == True) or (warningParS == True) or (warningOcuS == True) or (warningTelS == True) or (warningCorS == True) or (warningPassS == True) or (warningDpiS == True):
        defenActualizarS = False
    elif comasLS == True:
        messagebox.showwarning("Uso de comas", "No puede usar comas, si necesita separar información puede usar el punto(.) o algún otro signo de puntuación.")
        defenActualizarS = False
    elif (warningCorS2 == True) or (warningPassS2 == True) or (warningDpiS2 == True):
        defenActualizarS = False     
    else:
        defenActualizarS = True
    return(defenActualizarS)

def defenDonacion(tarjeta, vencimiento, codigo, monto, montoDefen):
    
    #Programación defensiva para que el número de tarjeta sea entre 13 y 19 dígitos.
    if (len(tarjeta) >= 13) and (len(tarjeta) <= 19) and (tarjeta.isdigit() == True):
        warningTar = False
    else:
        warningTar = True
        messagebox.showwarning("Tarjeta de crédito", "El numero de tarjeta no es válido. Tome en cuenta que no debe utilizar espacios.")
    
    #Programación defensiva para que la fecha de vencimiento tenga el formato requerido.
    try:
        fechaVencimiento = datetime.strptime(vencimiento, "%m/%y")
        warningVen = False
    except:
        warningVen = True
        messagebox.showwarning("Fecha de vencimiento", "La fecha de vencimeinto no tiene el formato requerido: mm/aa (ej: 05/21)")
    
    #Programación defensiva para que la tarjeta no se encuentre vencida.
    hoy = date.today()
    if warningVen == False:
        if fechaVencimiento.year < hoy.year:
            warningVen2 = True
            messagebox.showwarning("Tarjeta vencida", "Su tarjeta se encuentra vencida.")
        elif fechaVencimiento.year == hoy.year:
            if fechaVencimiento.month < hoy.month:
                warningVen2 = True
                messagebox.showwarning("Tarjeta vencida", "Su tarjeta se encuentra vencida.")
            else:
                warningVen2 = False
        else:
            warningVen2 = False
    
    #Programación defensiva para que el código de seguridad sean 3 o 4 dígitos.
    if codigo.isdigit() == False:
        warningCod = True
        messagebox.showwarning("Código de seguridad", "El código de seguridad solo puede tener dígitos.")
    elif len(codigo) < 3:
        warningCod = True
        messagebox.showwarning("Código de seguridad", "El código de seguridad debe tener al menos 3 dígitos.")
    elif len(codigo) > 4:
        warningCod = True
        messagebox.showwarning("Código de seguridad", "El código de seguridad no puede tener más de 4 dígitos.")
    else:
        warningCod = False
    
    #Programación defensiva para que el monto sea un valor numérico, y que este nk tenga más de 2 decimales.

    try:
        floatMonto = float(monto)
        floatM = True
    except ValueError:
        floatM = False
    if monto.isdigit() == True:
        warningMon = False
    elif floatM == True:
        decimales2 = "{0:.2f}".format(floatMonto)
        decimales1 = "{0:.1f}".format(floatMonto)
        if (str(decimales2) == str(floatMonto)) or (str(decimales1) == str(floatMonto)):
            warningMon = False
        else:
            warningMon = True
            messagebox.showwarning("Monto a donar", "El monto no puede tener más de 2 decimales, inténtelo de nuevo.")
    else:
        warningMon = True
        messagebox.showwarning("Monto a donar", "El monto no es un valor numérico válido, inténtelo de nuevo.")
    
    if (warningMon == False) and ("," in montoDefen):
        if "." in montoDefen:
            listaMD = montoDefen.split(".")
            listaMonto = listaMD[0].split(",")
        else:
            listaMonto = montoDefen.split(",")
        for i in range(len(listaMonto)):
            if (i == 0) and (len(listaMonto[i]) > 3):
                warningMon2 = True
                messagebox.showwarning("Monto a donar", "El monto ingresado tiene un mal posicionamiento en las comas, inténtelo de nuevo, o puede tambien ingresarlo todo junto sin comas.")
                break 
            elif (i != 0) and (len(listaMonto[i]) != 3):
                warningMon2 = True
                messagebox.showwarning("Monto a donar", "El monto ingresado tiene un mal posicionamiento en las comas, inténtelo de nuevo, o puede tambien ingresarlo todo junto sin comas.")
                break   
            else:
                warningMon2 = False
    else:
        warningMon2 = False
                            
    #Si no hay un problema la función retorna False, de lo contrario retorna True.
    if (warningTar == True) or (warningVen == True) or (warningVen2 == True) or (warningCod == True) or (warningMon == True) or (warningMon2 == True):
        defenDonacion = False
    else:
        defenDonacion = True
    return(defenDonacion)
        
def transformarMonto(montoDR):
    listaMontoDR = montoDR.split(".")
    listaSM = list(listaMontoDR[0])
    repM = math.ceil(len(listaSM)/3)
    listaSM3 = []
    for m in range(repM):
        if (repM - len(listaSM)/3) == 0:
            c = m*3
            listaSM3.append(listaSM[c]+listaSM[c+1]+listaSM[c+2])
        elif (repM - len(listaSM)/3) < 0.5:
            c = (m*3)-1
            if m==0:
                listaSM3.append(listaSM[0]+listaSM[1])
            else:
                listaSM3.append(listaSM[c]+listaSM[c+1]+listaSM[c+2])
        else:
            c = (m*3)-2
            if m==0:
                listaSM3.append(listaSM[0])
            else:
                listaSM3.append(listaSM[c]+listaSM[c+1]+listaSM[c+2])
    montoDR2 = ",".join(listaSM3) + "." + str(listaMontoDR[1])
    monto = "Q. " + montoDR2
    return(monto)