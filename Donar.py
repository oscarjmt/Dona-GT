from tkinter import *
from datetime import datetime
from datetime import date
import PIL
from PIL import Image
import Defensiva as df
import csv
import os

def datosDonacion(raiz, listaDonador, listaSolicitante):
    raiz2 = Toplevel(raiz)
    raiz2.title("Donar - Información")
    raiz2.iconbitmap("Logo.ico")
    raiz2.geometry("1100x900")
    raiz2.config(bg="skyblue") #Propiedades generales de la ventana.
    raiz2.focus_set()
    raiz2.grab_set()
    raiz2.transient(master=raiz)

    #Función realizada al presionar el botón de atrás.
    def abrirMenu():
        raiz2.destroy()  #Se abre la función de escogerAccion, regresa en otras palabras.

    #Función realizada al presionar el botón siguiente
    def abrirRealizarDonacion():
        realizarDonacion(raiz, raiz2, listaDonador, listaSolicitante)
    
    #Se obtiene la edad
    hoy = date.today()
    nacimiento = datetime.strptime(listaSolicitante[16], "%d/%m/%Y")
    if nacimiento.month < hoy.month:
        edad = hoy.year - nacimiento.year
    elif nacimiento.month > hoy.month:
        edad = hoy.year - nacimiento.year - 1
    elif nacimiento.month == hoy.month:
        if nacimiento.day > hoy.day:
            edad = hoy.year - nacimiento.year -1
        else:
            edad = hoy.year - nacimiento.year

    frame1 = Frame(raiz2, bg="skyblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Ayuda a combatir la desnutrición", width=30, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 22))
    textoBienvenido.grid(row=0, column=0, padx=15, pady=20, sticky="w") 

    logo3 = PhotoImage(file="Logo.png")
    logo4 = Label(frame1, image=logo3)
    logo4.image = logo3
    logo4.grid(row=0, column=1, padx=20, pady=15, sticky="e") #Primer frame con el mensaje de bienvenido y el logo.

    frame2 = Frame(raiz2, bg="skyblue")
    frame2.pack()
    
    subframeP = Frame(frame2, bg="#1190CB", highlightbackground="white", highlightcolor="white", highlightthickness=5)
    subframeP.grid(row=0, column=0)
    
    subframe1 = Frame(subframeP, bg="#1190CB", height=500, width=330)
    subframe1.grid(row=0, column=0)
    
    #Se pone la imagen del niño si es que existe, sino pone una de prueba.
    try:    
        img = os.getcwd() + "\\Fotos\\" + listaSolicitante[6] + "(2).png"
        imagen = PhotoImage(file=img)
    except:
        imagen = PhotoImage(file="ImagenPrueba2.png")
    imagen2 = Label(subframe1, image=imagen)
    imagen2.image = imagen
    imagen2.grid(row=0, column=0, padx=20, pady=20, sticky="e")
    
    #Se pone la imagen de la vivienda si es que existe, sino pone una de prueba.
    try:
        viv = os.getcwd() + "\\Fotos\\" + listaSolicitante[6] + "(3).png"
        vivienda = PhotoImage(file=viv)
    except:
        vivienda = PhotoImage(file="ImagenPrueba3.png")
    vivienda2 = Label(subframe1, bg="gray90", image=vivienda)
    vivienda2.image = vivienda
    vivienda2.grid(row=1, column=0, padx=20, pady=20, sticky="e")

    subframe2 = Frame(subframeP, bg="#1190CB", height=500, width=330)
    subframe2.grid(row=0, column=1, padx=20)
    
    Label(subframe2, text="", bg="#1190CB").grid(row=0, column=0, padx=0, pady=0)
    textoDatos = Label(subframe2, text="DATOS DEL NIÑO", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoDatos.grid(row=1, column=0, padx=5, pady=5)

    nombresFrame = Frame(subframe2, bg="#1190CB")
    nombresFrame.grid(row=2, column=0, sticky="w")
    textoNombres = Label(nombresFrame, text="NOMBRES:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoNombres.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoNombres2 = Label(nombresFrame, text=listaSolicitante[9], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoNombres2.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    apellidosFrame = Frame(subframe2, bg="#1190CB")
    apellidosFrame.grid(row=3, column=0, sticky="w")
    textoApellidos = Label(apellidosFrame, text="APELLIDOS:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoApellidos.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoApellidos2 = Label(apellidosFrame, text=listaSolicitante[10], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoApellidos2.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    seFrame = Frame(subframe2, bg="#1190CB")
    seFrame.grid(row=5, column=0, sticky="w")
    textoSexo = Label(seFrame, text="SEXO:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoSexo.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoSexo2 = Label(seFrame, text=listaSolicitante[11], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoSexo2.grid(row=0, column=1, padx=0, pady=0, sticky="w")
    Label(seFrame, text="", bg="#1190CB").grid(row=0, column=2, padx=4)
    textoEdad = Label(seFrame, text="EDAD:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoEdad.grid(row=0, column=3, padx=5, pady=5, sticky="w")
    textoEdad2 = Label(seFrame, text=str(edad) + " años", bg="#1190CB", fg="white", font=("Calibri", 14))
    textoEdad2.grid(row=0, column=4, padx=0, pady=0, sticky="w")
    
    apFrame = Frame(subframe2, bg="#1190CB")
    apFrame.grid(row=6, column=0, sticky="w")
    textoAltura = Label(apFrame, text="ALTURA:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoAltura.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoAltura2 = Label(apFrame, text=listaSolicitante[12] + " m", bg="#1190CB", fg="white", font=("Calibri", 14))
    textoAltura2.grid(row=0, column=1, padx=0, pady=0, sticky="w")
    Label(apFrame, text="", bg="#1190CB").grid(row=0, column=2, padx=10)
    textoPeso = Label(apFrame, text="PESO:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoPeso.grid(row=0, column=3, padx=5, pady=5, sticky="w")
    textoPeso2 = Label(apFrame, text=listaSolicitante[13] + " lb", bg="#1190CB", fg="white", font=("Calibri", 14))
    textoPeso2.grid(row=0, column=4, padx=0, pady=0, sticky="w")

    departamentoFrame = Frame(subframe2, bg="#1190CB")
    departamentoFrame.grid(row=8, column=0, sticky="w")
    textoDepartamento = Label(departamentoFrame, text="DEPARTAMENTO:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoDepartamento.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoDepartamento2 = Label(departamentoFrame, text=listaSolicitante[14], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoDepartamento2.grid(row=0, column=1, padx=0, pady=0, sticky="w") 

    municipioFrame = Frame(subframe2, bg="#1190CB")
    municipioFrame.grid(row=9, column=0, sticky="w")
    textoMunicipio = Label(municipioFrame, text="MUNICIPIO:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoMunicipio.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoMunicipio2 = Label(municipioFrame, text=listaSolicitante[15], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoMunicipio2.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    educacionFrame = Frame(subframe2, bg="#1190CB")
    educacionFrame.grid(row=10, column=0, sticky="w")
    textoEducacion = Label(educacionFrame, text="NIVEL DE EDUCACIÓN:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoEducacion.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoEducacion2 = Label(educacionFrame, text=listaSolicitante[17], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoEducacion2.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    institucionFrame = Frame(subframe2, bg="#1190CB")
    institucionFrame.grid(row=11, column=0, sticky="w")
    textoInstitucion = Label(institucionFrame, text="ESTUDIA EN:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoInstitucion.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoInstitucion2 = Label(institucionFrame, text=listaSolicitante[18], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoInstitucion2.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    tipoFrame = Frame(subframe2, bg="#1190CB")
    tipoFrame.grid(row=12, column=0, sticky="w")
    textoTipo = Label(tipoFrame, text="TIPO DE DESNUTRICIÓN:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoTipo.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoTipo2 = Label(tipoFrame, text=listaSolicitante[19], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoTipo2.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    enfermedadesFrame = Frame(subframe2, bg="#1190CB")
    enfermedadesFrame.grid(row=13, column=0, sticky="w")
    textoEnfermedades = Label(enfermedadesFrame, text="ENFERMEDADES:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoEnfermedades.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    textoEnfermedades2 = Label(enfermedadesFrame, text=listaSolicitante[20], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoEnfermedades2.grid(row=2, column=0, padx=5, pady=0, sticky="w")

    recursosFrame = Frame(subframe2, bg="#1190CB")
    recursosFrame.grid(row=14, column=0, sticky="w")
    textoRecursos = Label(recursosFrame, text="RECURSOS QUE NECESITA:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoRecursos.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    textoRecursos2 = Label(recursosFrame, text=listaSolicitante[21], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoRecursos2.grid(row=2, column=0, padx=5, pady=0, sticky="w")
    
    Label(subframe2, text="", bg="#1190CB").grid(row=15, column=0, padx=0, pady=0)
    
    subframe3 = Frame(frame2, bg="#1190CB", height=500, width=330, highlightbackground="white", highlightcolor="white", highlightthickness=5)
    subframe3.grid(row=0, column=1, sticky="wn", padx=30, pady=60)
    
    Label(subframe3, text="", bg="#1190CB").grid(row=0, column=0, padx=0, pady=0)
    textoEncargado = Label(subframe3, text="DATOS DEL ENCARGADO", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoEncargado.grid(row=1, column=0, padx=5, pady=5)

    nombresFrameE = Frame(subframe3, bg="#1190CB")
    nombresFrameE.grid(row=2, column=0, sticky="w")
    textoNombresE = Label(nombresFrameE, text="NOMBRES:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoNombresE.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoNombresE2 = Label(nombresFrameE, text=listaSolicitante[0], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoNombresE2.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    apellidosFrameE = Frame(subframe3, bg="#1190CB")
    apellidosFrameE.grid(row=3, column=0, sticky="w")
    textoApellidosE = Label(apellidosFrameE, text="APELLIDOS:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoApellidosE.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoApellidosE2 = Label(apellidosFrameE, text=listaSolicitante[1], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoApellidosE2.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    parentescoFrame = Frame(subframe3, bg="#1190CB")
    parentescoFrame.grid(row=4, column=0, sticky="w")
    textoParentesco = Label(parentescoFrame, text="PARENTESCO:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoParentesco.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoParentesco2 = Label(parentescoFrame, text=listaSolicitante[2], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoParentesco2.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    ocupacionFrame = Frame(subframe3, bg="#1190CB")
    ocupacionFrame.grid(row=5, column=0, sticky="w")
    textoOcupacion = Label(ocupacionFrame, text="OCUPACIÓN:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoOcupacion.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoOcupacion2 = Label(ocupacionFrame, text=listaSolicitante[3], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoOcupacion2.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    telefonoFrame = Frame(subframe3, bg="#1190CB")
    telefonoFrame.grid(row=6, column=0, sticky="w")
    textoTelefono = Label(telefonoFrame, text="TELÉFONO:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoTelefono.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoTelefono2 = Label(telefonoFrame, text=listaSolicitante[4], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoTelefono2.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    dpiFrame = Frame(subframe3, bg="#1190CB")
    dpiFrame.grid(row=7, column=0, sticky="w")
    textoDPI = Label(dpiFrame, text="NO. DE DPI:", bg="#1190CB", fg="#d6e8fc", font=("Calibri", 12))
    textoDPI.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    textoDPI2 = Label(dpiFrame, text=listaSolicitante[8], bg="#1190CB", fg="white", font=("Calibri", 14))
    textoDPI2.grid(row=0, column=1, padx=0, pady=0, sticky="w")
    
    Label(subframe3, text="", bg="#1190CB").grid(row=8, column=0, padx=0, pady=0)
    
    frame3 = Frame(raiz2, bg="skyblue")
    frame3.pack()

    botonCerrar = Button(frame3, text="Cerrar", width=10, anchor="center", command=abrirMenu) #Botón de atrás, que realiza la función abrirEscoger2.
    botonCerrar.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonCerrar.grid(row=0, column=0, padx=100, pady=0, sticky="sw")

    botonDonar = Button(frame3, text="DONAR", width=8, anchor="center", command=abrirRealizarDonacion) #Botón de siguiente, que realiza la función abrirMenu2.
    botonDonar.config(cursor="hand2", bg="mediumseagreen", fg="white", font=("Calibri", 26))
    botonDonar.grid(row=0, column=1, padx=400, pady=0, sticky="nw")
    
def realizarDonacion(raiz, raiz2, listaDonador, listaSolicitante):
    raiz3 = Toplevel(raiz2)
    raiz3.title("Donar - Realizar donación")
    raiz3.iconbitmap("Logo.ico")
    raiz3.geometry("910x500")
    raiz3.resizable(width=False, height=False)
    raiz3.config(bg="#1190CB") #Propiedades generales de la ventana.
    raiz3.focus_set()
    raiz3.grab_set()
    raiz3.transient(master=raiz2)

    #Función realizada al presionar el botón de atrás.
    def cerrarDonacion1():
        raiz3.destroy()
        raiz2.focus_set()
        raiz2.grab_set()
        raiz2.transient(master=raiz)
    
    #Función realizada al presionar el botón de siguiente.
    def cerrarDonacion2():
        tarjeta = cuadroTarjeta.get()
        vencimiento = cuadroVencimiento.get()
        codigo = cuadroCodigo.get() 
        monto = cuadroMonto.get()
        montoDefen = cuadroMonto.get()
        if "," in str(monto):
            listaMonto = monto.split(",")
            monto = "".join(listaMonto)
                
        fechaDonacion = date.today()
        fechaDonacion = fechaDonacion.strftime("%d/%m/%Y")
        #Se corre la función defensiva para la donación, con los parámetros de los datos ingresados, en el que si regresa True, entonces si realize la donación.
        if df.defenDonacion(tarjeta, vencimiento, codigo, monto, montoDefen) == True:
            montoDinero = "{0:.2f}".format(float(monto))
            listaDonacion = [listaDonador[3], listaSolicitante[6], listaSolicitante[9], listaSolicitante[10], montoDinero, fechaDonacion]
            confirmacion = messagebox.askyesno("Donar", "¿Desea realizar esta transacción?") #Pregunta de seguridad.
            if confirmacion == True:
                with open('DonacionesRealizadas.csv', 'a+') as archivoDR:
                    escribir = csv.writer(archivoDR, lineterminator='\n')
                    escribir.writerow(listaDonacion)
                    archivoDR.close() #Se Escribre en el archivo de las cuentas de donadores, cada sublista de la listaCuentasD. 
                messagebox.showinfo("Donación realizada","Muchas gracias por tu ayuda! Tu donación contribuirá a financiar los recursos que "+listaSolicitante[9]+" necesita ("+listaSolicitante[21]+").") #Muestra un mensaje de confrmación.
                raiz3.destroy()
                raiz2.focus_set()
                raiz2.grab_set()
                raiz2.transient(master=raiz)

    frame1 = Frame(raiz3, bg="#1190CB")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Realizar donación", width=20, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 25))
    textoBienvenido.grid(row=0, column=0, padx=20, pady=40, sticky="w") #Primer frame con el mensaje de realizar donación.

    frame2 = Frame(raiz3, bg="#1190CB")
    frame2.pack()
    
    #Texto y cuadro para la tarjeta, con el valor predeterminado de la tarjeta registrada.
    predTarjeta = StringVar(frame2, listaDonador[5])
    textoTarjeta = Label(frame2, text="No. de Tarjeta:", bg="#1190CB", fg="white", font=("Calibri", 16))
    textoTarjeta.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    cuadroTarjeta = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predTarjeta)
    cuadroTarjeta.grid(row=0, column=1, padx=10, pady=10)
    
    frame3 = Frame(raiz3, bg="#1190CB")
    frame3.pack()
    
    #Textos que indican al usuario que debe ingresar.
    textoVencimiento = Label(frame3, text="Fecha de vencimiento:", bg="#1190CB", fg="white", font=("Calibri", 16))
    textoVencimiento.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    textoCodigo = Label(frame3, text="Código de seguridad:", bg="#1190CB", fg="white", font=("Calibri", 16))
    textoCodigo.grid(row=0, column=2, padx=20, pady=10, sticky="w")
    
    #Cuadros de texto para cada dato a ingresar.
    cuadroVencimiento = Entry(frame3, width=8, fg="midnightblue", font=("Calibri", 14))
    cuadroVencimiento.grid(row=0, column=1, padx=20, pady=10)
    cuadroCodigo = Entry(frame3, width=8, fg="midnightblue", font=("Calibri", 14))
    cuadroCodigo.grid(row=0, column=3, padx=10, pady=10)
    
    frame4 = Frame(raiz3, bg="#1190CB")
    frame4.pack()
    
    #Texto y cuadro para el monto.
    textoMonto = Label(frame4, text="Monto:   Q . ", bg="#1190CB", fg="white", font=("Calibri", 16))
    textoMonto.grid(row=0, column=0, padx=0, pady=10, sticky="e")
    cuadroMonto = Entry(frame4, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroMonto.grid(row=0, column=1, padx=0, pady=10)

    frame5 = Frame(raiz3, bg="#1190CB")
    frame5.pack()

    botonCancelar = Button(frame5, text="Cancelar", width=10, anchor="center", command=cerrarDonacion1) #Botón de atrás, que realiza la función cerrarDonacion1.
    botonCancelar.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonCancelar.grid(row=0, column=0, padx=150, pady=40)

    botonDonar = Button(frame5, text="DONAR", width=8, anchor="center", command=cerrarDonacion2) #Botón de donar, que realiza la función cerrarDonacion2.
    botonDonar.config(cursor="hand2", bg="mediumseagreen", fg="white", font=("Calibri", 22))
    botonDonar.grid(row=0, column=1, padx=150, pady=40)
    
    raiz3.protocol("WM_DELETE_WINDOW", cerrarDonacion1)
