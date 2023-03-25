from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image
import csv
import os
import Defensiva as df #Se importan todos los módulos.

#Función para actualizar los datos de donadores.
def donadorActualizar(listaDonador):
    raiz= Tk()
    raiz.title("Donador - Actualizar datos")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("900x730")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana.
    
    #Función realizada al presionar el botón atrás.
    def abrirMenu1():
        raiz.destroy()
        import MenuDonador
        MenuDonador.donadorBusqueda(listaDonador) #Regresa al menu, abriendo esta función y conservando el parámetro de la lista de donadores.

    def abrirMenu2():
        nombresD = cuadroNombres.get()
        apellidosD = cuadroApellidos.get()
        correoD = cuadroCorreo.get()
        usuarioD = cuadroUsuario.get()
        passwordD = cuadroPassword.get()
        tarjetaD = cuadroTarjeta.get() #Se obtienen los valores que el usuario escribió en los cuadros de texto.
        listaD = [nombresD, apellidosD, correoD, usuarioD, passwordD, tarjetaD] #Se añade todas esas variables a una lista.
        
        listaCuentasD = []
        with open("CuentasDonador.csv", "r") as archivoCD:
            leer = csv.reader(archivoCD, delimiter=',')
            for filas in leer:
                listaCuentasD.append(filas)
            archivoCD.close() #Se lee el archivo de las cuentas de donadores, y por cada cuenta toda su información en una lista, se agrega a la listaCuentasD que contendrá todas las cuentas.
        
        #Se corre la función defensiva para actualizar los datos de donadores, con los parámetros de los datos ingresados y la listaDonador, en el que si regresa True, entonces se actualicen los datos de la cuenta.
        if df.defenActualizarD(nombresD, apellidosD, correoD, usuarioD, passwordD, tarjetaD, listaD, listaDonador) == True:
            confirmacion = messagebox.askyesno("Actualizar datos", "¿Esta seguro que desea cambiar sus datos?") #Pregunta de seguridad.
            if confirmacion == True:
                #Se crea un ciclo para que encuentre la lista de la cuenta que contiene el usuario, y esta se sutituya por la lista nueva.
                for i in range(len(listaCuentasD)):
                    if listaCuentasD[i][3] == usuarioD:
                        listaCuentasD[i] = listaD 
                with open('CuentasDonador.csv', 'w') as archivoCD:
                    for i in range(len(listaCuentasD)):
                        escribir = csv.writer(archivoCD, lineterminator='\n')
                        escribir.writerow(listaCuentasD[i])
                    archivoCD.close() #Se sobreescribre en el archivo de las cuentas de donadores, cada sublista de la listaCuentasD. 
                for i in range(len(listaD)):
                    listaDonador[i] = listaD[i] #Se actualiza la listaDonador con los valores de la lista nueva.
                messagebox.showinfo("Actualización de datos","Sus datos han sido actualizados") #Muestra un mensaje de confrmación.
                raiz.destroy()
                import MenuDonador
                MenuDonador.donadorBusqueda(listaDonador) #Se abre la función de búsqueda en el menu, con el parámetro de la listaDonador actualizada.

    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Actualiza tus datos", width=20, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 25))
    textoBienvenido.grid(row=0, column=0, padx=20, pady=40, sticky="w") 

    logo = PhotoImage(file="Logo.png")
    logo2 = Label(frame1, image=logo)
    logo2.grid(row=0, column=1, padx=20, pady=40, sticky="e") #Primer frame con el mensaje Regístrate y el logo.

    frame2 = Frame(raiz, bg="cornflowerblue")
    frame2.pack()
    
    #Textos que indican al usuario que debe ingresar.
    textoNombres = Label(frame2, text="Nombres:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoNombres.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    textoApellidos = Label(frame2, text="Apellidos:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoApellidos.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    textoCorreo = Label(frame2, text="Correo electrónico:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoCorreo.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    textoUsuario = Label(frame2, text="Nombre de usuario:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoUsuario.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    textoPassword = Label(frame2, text="Contraseña:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoPassword.grid(row=4, column=0, padx=10, pady=10, sticky="e")
    textoTarjeta = Label(frame2, text="No. de tarjeta de crédito:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoTarjeta.grid(row=5, column=0, padx=10, pady=10, sticky="e")
    
    #Valores predeterminados con los datos del donador que inició sesión.
    predNombres = StringVar(frame2, listaDonador[0])
    predApellidos = StringVar(frame2, listaDonador[1])
    predCorreo = StringVar(frame2, listaDonador[2])
    predUsuario = StringVar(frame2, listaDonador[3])
    predPassword = StringVar(frame2, listaDonador[4])
    predTarjeta = StringVar(frame2, listaDonador[5])
    
    #Cuadros de texto para cada dato a modificar.
    cuadroNombres = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predNombres)
    cuadroNombres.grid(row=0, column=1, padx=10, pady=10)
    cuadroApellidos = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predApellidos)
    cuadroApellidos.grid(row=1, column=1, padx=10, pady=10)
    cuadroCorreo = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predCorreo)
    cuadroCorreo.grid(row=2, column=1, padx=10, pady=10)
    cuadroUsuario = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), state="disabled", textvariable=predUsuario)
    cuadroUsuario.grid(row=3, column=1, padx=10, pady=10)
    cuadroPassword = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predPassword)
    cuadroPassword.grid(row=4, column=1, padx=10, pady=10)
    cuadroPassword.config(show="*")
    cuadroTarjeta = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predTarjeta)
    cuadroTarjeta.grid(row=5, column=1, padx=10, pady=10)

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()

    botonAtras = Button(frame3, text="Atrás", width=10, anchor="center", command=abrirMenu1) #Botón de atrás, que realiza la función abrirMenu1.
    botonAtras.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonAtras.grid(row=0, column=0, padx=150, pady=40)

    botonSiguiente = Button(frame3, text="Siguiente", width=10, anchor="center", command=abrirMenu2) #Botón de siguiente, que realiza la función abrirMenu2.
    botonSiguiente.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonSiguiente.grid(row=0, column=1, padx=150, pady=40)

    raiz.mainloop()

#Función para actualizar datos del solicitantes, con los datos del niño.
def nActualizar(listaS, listaSolicitante):
    raiz= Tk()
    raiz.title("Solicitante - Actualizar datos del niño")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("1000x930")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana.
    
    #Función que genera una copia de la foto del niño que elija el usuario.
    def subirFoto():
        #Se abre el directorio para que el usaurio pueda elegir una imagen.
        try:
            foto = askopenfilename()
            confirmacion = True
            if confirmacion == True:
                img = Image.open(foto)
                #Se guarda una copia con el tamaño para el menú de donadores.
                imgN = img.resize((190,190))
                imgN.save(os.getcwd() + "\\Fotos\\" + str(listaS[6]) + "(1).png")
                #Se guarda una segunda copia con el tamaño para la interfaz de donar.
                imgN = img.resize((250,250))
                imgN.save(os.getcwd() + "\\Fotos\\" + str(listaS[6]) + "(2).png")
                messagebox.showinfo("Imagen subida", "Se ha subido la imagen con éxito.")
        except:
            messagebox.showwarning("Archivo de Imagen", "El archivo que ha seleccionado no es una imagen.")
    
    #Función que genera una copia de la foto de la vivienda que elija el usuario.
    def subirVivienda():
        #Se abre el directorio para que el usaurio pueda elegir una imagen.
        try:
            foto = askopenfilename()
            confirmacion = True
            if confirmacion == True:
                img = Image.open(foto)
                #Se guarda una copia con el tamaño para el menú de donadores.
                imgN = img.resize((250,250))
                imgN.save(os.getcwd() + "\\Fotos\\" + str(listaS[6]) + "(3).png")
                messagebox.showinfo("Imagen subida", "Se ha subido la imagen con éxito.")
        except:
            messagebox.showwarning("Archivo de Imagen", "El archivo que ha seleccionado no es una imagen.")
    
    #Función realizada al presionar el botón atrás.
    def abrirActualizarS():
        raiz.destroy()
        solicitanteActualizar(listaSolicitante) #Regresa al ingreso de datos del encargado, abriendo esta función y conservando el parámetro de la lista de solicitantes.
    
    #Función realizada al presionar el botón siguiente.
    def abrirMenu3():
        nombresN = cuadroNombres.get()
        apellidosN = cuadroApellidos.get()
        if listaSolicitante[11] == "Masculino":
            sexoN = "Masculino"
        elif listaSolicitante[11] == "Femenino":
            sexoN = "Femenino" #Se obtiene el sexo del niño.
        alturaN = cuadroAltura.get()
        pesoN = cuadroPeso.get()
        departamentoN = cuadroDepartamento.get()
        municipioN = cuadroMunicipio.get()
        fechaN = cuadroFecha.get()
        educacionN = cuadroEducacion.get()
        institucionN = cuadroInstitucion.get()
        tipoN = cuadroTipo.get()
        enfermedadesN = cuadroEnfermedades.get()
        recursosN = cuadroRecursos.get() #Se obtienen los valores que el usuario escribió en los cuadros de texto.
        listaN = [nombresN, apellidosN, sexoN, alturaN, pesoN, departamentoN, municipioN, fechaN, educacionN, institucionN, tipoN, enfermedadesN, recursosN] #Se añade todas esas variables a una lista.
        
        listaCuentasS = []
        with open("CuentasSolicitante.csv", "r") as archivoCS:
            leer = csv.reader(archivoCS, delimiter=',')
            for filas in leer:
                listaCuentasS.append(filas)
            archivoCS.close() #Se lee el archivo de las cuentas de solicitantes, y por cada cuenta toda su información en una lista, se agrega a la listaCuentasS que contendrá todas las cuentas.
        
        #Se corre la función defensiva para registro con los datos del niño (al ser completamente igual al del registro), con los parámetros de los datos ingresados y la listaSolicitante, en el que si regresa True, entonces se actualicen los datos de la cuenta.
        if df.defenRegistroN(nombresN, apellidosN, sexoN, alturaN, pesoN, departamentoN, municipioN, fechaN, recursosN, listaN) == True:
            for i in range(len(listaN)):
                listaS.append(listaN[i]) #Se agregan los datos del niño de la listaN, a la listaS que envió la función anterior con los datos del encargado.
            confirmacion = messagebox.askyesno("Actualizar datos", "¿Esta seguro que desea cambiar sus datos?") #Pregunta de seguridad.
            if confirmacion == True:
                #Se crea un ciclo para que encuentre la lista de la cuenta que contiene el usuario, y esta se sutituya por la lista nueva.
                for i in range(len(listaCuentasS)):
                    if listaCuentasS[i][6] == listaS[6]:
                        listaCuentasS[i] = listaS
                with open('CuentasSolicitante.csv', 'w') as archivoCS:
                    for i in range(len(listaCuentasS)):
                        escribir = csv.writer(archivoCS, lineterminator='\n')
                        escribir.writerow(listaCuentasS[i])
                    archivoCS.close() #Se sobreescribre en el archivo de las cuentas de solicitantes, cada sublista de la listaCuentasS. 
                for i in range(len(listaS)):
                    listaSolicitante[i] = listaS[i] #Se actualiza la listaSolicitante con los valores de la lista nueva.
                messagebox.showinfo("Actualización de datos","Sus datos han sido actualizados") #Muestra un mensaje de confrmación.
                raiz.destroy()
                import MenuSolicitante
                MenuSolicitante.solicitanteDonaciones(listaSolicitante) #Se abre la función de donaciones recibidas (el menú), con el parámetro de la listaSolicitante actualizada.
        
    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Datos del niño", width=20, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 25))
    textoBienvenido.grid(row=0, column=0, padx=20, pady=20, sticky="w") 

    logo = PhotoImage(file="Logo.png")
    logo2 = Label(frame1, image=logo)
    logo2.grid(row=0, column=1, padx=20, pady=20, sticky="e") #Primer frame con el mensaje Regístrate y el logo.

    frame2 = Frame(raiz, bg="cornflowerblue")
    frame2.pack()
    
    #Textos que indican al usuario que debe ingresar.
    textoNombres = Label(frame2, text="Nombres:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoNombres.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    textoApellidos = Label(frame2, text="Apellidos:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoApellidos.grid(row=0, column=2, padx=10, pady=10, sticky="e")
    
    #Cuadros de texto para cada dato a modificar, con los valores predeterminados con los datos del solicitante que inició sesión.
    predNombres = StringVar(frame2, listaSolicitante[9])
    cuadroNombres = Entry(frame2, width=22, fg="midnightblue", font=("Calibri", 14), textvariable=predNombres)
    cuadroNombres.grid(row=0, column=1, padx=10, pady=10)    
    predApellidos = StringVar(frame2, listaSolicitante[10])
    cuadroApellidos = Entry(frame2, width=22, fg="midnightblue", font=("Calibri", 14), textvariable=predApellidos)
    cuadroApellidos.grid(row=0, column=3, padx=10, pady=10)

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()
    
    #Textos que indican al usuario que debe ingresar.
    textoAltura = Label(frame3, text="Altura (m):", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoAltura.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    textoPeso = Label(frame3, text="Peso (lb):", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoPeso.grid(row=0, column=2, padx=10, pady=10, sticky="e")
    
    #Cuadros de texto para cada dato a modificar, con los valores predeterminados con los datos del solicitante que inició sesión.
    predAltura = StringVar(frame3, listaSolicitante[12])
    cuadroAltura = Entry(frame3, width=8, fg="midnightblue", font=("Calibri", 14), textvariable=predAltura)
    cuadroAltura.grid(row=0, column=1, padx=10, pady=10)
    predPeso = StringVar(frame3, listaSolicitante[13])
    cuadroPeso = Entry(frame3, width=8, fg="midnightblue", font=("Calibri", 14), textvariable=predPeso)
    cuadroPeso.grid(row=0, column=3, padx=10, pady=10)

    frame4 = Frame(raiz, bg="cornflowerblue")
    frame4.pack()

    #Textos que indican al usuario que debe ingresar.
    textoDepartamento = Label(frame4, text="Departamento:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoDepartamento.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    textoMunicipio = Label(frame4, text="Municipio:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoMunicipio.grid(row=0, column=2, padx=10, pady=10, sticky="e")
    
    #Cuadros de texto para cada dato a modificar, con los valores predeterminados con los datos del solicitante que inició sesión.
    predDepartamento = StringVar(frame4, listaSolicitante[14])
    cuadroDepartamento = Entry(frame4, width=20, fg="midnightblue", font=("Calibri", 14), textvariable=predDepartamento)
    cuadroDepartamento.grid(row=0, column=1, padx=10, pady=10)
    predMunicipio = StringVar(frame4, listaSolicitante[15])
    cuadroMunicipio = Entry(frame4, width=20, fg="midnightblue", font=("Calibri", 14), textvariable=predMunicipio)
    cuadroMunicipio.grid(row=0, column=3, padx=10, pady=10)

    frame5 = Frame(raiz, bg="cornflowerblue")
    frame5.pack()

    #Textos que indican al usuario que debe ingresar.
    textoFecha = Label(frame5, text="Fecha de nacimeinto (dd/mm/aaaa):", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoFecha.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    textoEducacion = Label(frame5, text="Nivel de educación:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoEducacion.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    textoInstitucion = Label(frame5, text="Institución en la que estudia:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoInstitucion.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    textoTipo = Label(frame5, text="Tipo de desnutrición:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoTipo.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    textoEnfermedades = Label(frame5, text="Indique si tiene alguna enfermedad:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoEnfermedades.grid(row=4, column=0, padx=10, pady=10, sticky="e")
    textoRecursos = Label(frame5, text="Recursos que necesita:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoRecursos.grid(row=5, column=0, padx=10, pady=10, sticky="e")
    
    #Cuadros de texto para cada dato a modificar, con los valores predeterminados con los datos del solicitante que inició sesión.
    predFecha = StringVar(frame5, listaSolicitante[16])
    cuadroFecha = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predFecha)
    cuadroFecha.grid(row=0, column=1, padx=10, pady=10) 
    predEducacion = StringVar(frame5, listaSolicitante[17])
    cuadroEducacion = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predEducacion)
    cuadroEducacion.grid(row=1, column=1, padx=10, pady=10) 
    predInstitucion = StringVar(frame5, listaSolicitante[18])
    cuadroInstitucion = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predInstitucion)
    cuadroInstitucion.grid(row=2, column=1, padx=10, pady=10)
    predTipo = StringVar(frame5, listaSolicitante[19])
    cuadroTipo = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predTipo)
    cuadroTipo.grid(row=3, column=1, padx=10, pady=10) 
    predEnfermedades = StringVar(frame5, listaSolicitante[20])
    cuadroEnfermedades = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predEnfermedades)
    cuadroEnfermedades.grid(row=4, column=1, padx=10, pady=10)  
    predRecursos = StringVar(frame5, listaSolicitante[21])
    cuadroRecursos = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predRecursos)
    cuadroRecursos.grid(row=5, column=1, padx=10, pady=10)

    frame6 = Frame(raiz, bg="cornflowerblue")
    frame6.pack()

    botonFoto = Button(frame6, text="Cambiar foto del niño", anchor="center", command=subirFoto) #Botón para subir la foto del niño, que realiza la función subirFoto.
    botonFoto.config(relief="flat", cursor="hand2", bg="cornflowerblue", fg="white", font=("Calibri", 11))
    botonFoto.grid(row=0, column=0, padx=1, pady=3)

    textoSeparador = Label(frame6, text="|", anchor="center") #Un separador para los botones, por cuestiones visuales.
    textoSeparador.config(bg="cornflowerblue", fg="white", font=("Calibri", 11))
    textoSeparador.grid(row=0, column=1, padx=1, pady=3)

    botonVivienda = Button(frame6, text="Cambiar foto de la vivienda", anchor="center", command=subirVivienda) #Botón para subir la foto de la vivienda del niño, que realiza la función subirVivienda.
    botonVivienda.config(relief="flat", cursor="hand2", bg="cornflowerblue", fg="white", font=("Calibri", 11))
    botonVivienda.grid(row=0, column=2, padx=1, pady=3)

    frame7 = Frame(raiz, bg="cornflowerblue")
    frame7.pack()

    botonAtras = Button(frame7, text="Atrás", width=10, anchor="center", command=abrirActualizarS) #Botón de atrás, que realiza la función abrirActualizarS.
    botonAtras.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonAtras.grid(row=0, column=0, padx=150, pady=40)

    botonSiguiente = Button(frame7, text="Siguiente", width=10, anchor="center", command=abrirMenu3) #Botón de siguiente, que realiza la función abrirMenu3.
    botonSiguiente.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonSiguiente.grid(row=0, column=1, padx=150, pady=40)

    raiz.mainloop()

#Función para actualizar los datos del solicitante, empezando con el encargado.
def solicitanteActualizar(listaSolicitante):
    raiz= Tk()
    raiz.title("Solicitante - Actualizar datos del encargado")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("900x900")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana.

    def abrirMenu4():
        raiz.destroy()
        import MenuSolicitante
        MenuSolicitante.solicitanteDonaciones(listaSolicitante) #Regresa al menu, abriendo esta función y conservando el parámetro de la lista de solicitantes.

    def abrirActualizarN():
        nombresS = cuadroNombres.get()
        apellidosS = cuadroApellidos.get()
        parentescoS = cuadroParentesco.get()
        ocupacionS = cuadroOcupacion.get()
        telefonoS = cuadroTelefono.get()
        correoS = cuadroCorreo.get()
        usuarioS = cuadroUsuario.get()
        passwordS = cuadroPassword.get()
        dpiS = cuadroDPI.get() #Se obtienen los valores que el usuario escribió en los cuadros de texto.
        listaS = [nombresS, apellidosS, parentescoS, ocupacionS, telefonoS, correoS, usuarioS, passwordS, dpiS] #Se añade todas esas variables a una lista.
        
        listaCuentasS = []
        with open("CuentasSolicitante.csv", "r") as archivoCS:
            leer = csv.reader(archivoCS, delimiter=',')
            for filas in leer:
                listaCuentasS.append(filas)
            archivoCS.close() #Se lee el archivo de las cuentas de solicitantes, y por cada cuenta toda su información en una lista, se agrega a la listaCuentasS que contendrá todas las cuentas.
        
        #Se corre la función defensiva para actualizar los datos de encargados, con los parámetros de los datos ingresados y la listaSolicitnante, en el que si regresa True, entonces continue con la actualización de los datos del niño.
        if df.defenActualizarS(nombresS, apellidosS, parentescoS, ocupacionS, telefonoS, correoS, usuarioS, passwordS, dpiS, listaS, listaSolicitante) == True:
            messagebox.showinfo("Actualización de datos","Proceda a actualizar los datos del niño, si solo desea actualizar los datos del encargado presione siguiente de nuevo.") #Mensaje de continuación.    
            raiz.destroy()
            nActualizar(listaS, listaSolicitante) #Se abre la función de la actualización de los datos del niño, utilizando como parámetro la listaS con los datos del encargado actualizados, y la listaSolicitnate original.

    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Datos del encargado", width=20, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 25))
    textoBienvenido.grid(row=0, column=0, padx=20, pady=40, sticky="w") 

    logo = PhotoImage(file="Logo.png")
    logo2 = Label(frame1, image=logo)
    logo2.grid(row=0, column=1, padx=20, pady=40, sticky="e") #Primer frame con el mensaje Regístrate y el logo.

    frame2 = Frame(raiz, bg="cornflowerblue")
    frame2.pack()
    
    #Textos que indican al usuario que debe ingresar.
    textoNombres = Label(frame2, text="Nombres:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoNombres.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    textoApellidos = Label(frame2, text="Apellidos:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoApellidos.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    textoParentesco = Label(frame2, text="Parentesco con el niño:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoParentesco.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    textoOcupacion = Label(frame2, text="Ocupación:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoOcupacion.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    textoTelefono = Label(frame2, text="Telefono:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoTelefono.grid(row=4, column=0, padx=10, pady=10, sticky="e")
    textoCorreo = Label(frame2, text="Correo electrónico:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoCorreo.grid(row=5, column=0, padx=10, pady=10, sticky="e")
    textoUsuario = Label(frame2, text="Nombre de usuario:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoUsuario.grid(row=6, column=0, padx=10, pady=10, sticky="e")
    textoPassword = Label(frame2, text="Contraseña:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoPassword.grid(row=7, column=0, padx=10, pady=10, sticky="e")
    textoDPI = Label(frame2, text="No. de DPI:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoDPI.grid(row=8, column=0, padx=10, pady=10, sticky="e")
    
    #Valores predeterminados con los datos del solicitante que inició sesión.
    predNombres = StringVar(frame2, listaSolicitante[0])
    predApellidos = StringVar(frame2, listaSolicitante[1])
    predParentesco = StringVar(frame2, listaSolicitante[2])
    predOcupacion = StringVar(frame2, listaSolicitante[3])
    predTelefono = StringVar(frame2, listaSolicitante[4])
    predCorreo = StringVar(frame2, listaSolicitante[5])
    predUsuario = StringVar(frame2, listaSolicitante[6])
    predPassword = StringVar(frame2, listaSolicitante[7])
    predDPI = StringVar(frame2, listaSolicitante[8])
    
    #Cuadros de texto para cada dato a modificar.
    cuadroNombres = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predNombres)
    cuadroNombres.grid(row=0, column=1, padx=10, pady=10)
    cuadroApellidos = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predApellidos)
    cuadroApellidos.grid(row=1, column=1, padx=10, pady=10)
    cuadroParentesco = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predParentesco)
    cuadroParentesco.grid(row=2, column=1, padx=10, pady=10)
    cuadroOcupacion = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predOcupacion)
    cuadroOcupacion.grid(row=3, column=1, padx=10, pady=10)
    cuadroTelefono = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predTelefono)
    cuadroTelefono.grid(row=4, column=1, padx=10, pady=10)
    cuadroCorreo = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predCorreo)
    cuadroCorreo.grid(row=5, column=1, padx=10, pady=10)
    cuadroUsuario = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), state="disabled", textvariable=predUsuario)
    cuadroUsuario.grid(row=6, column=1, padx=10, pady=10)
    cuadroPassword = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predPassword)
    cuadroPassword.grid(row=7, column=1, padx=10, pady=10)
    cuadroPassword.config(show="*")
    cuadroDPI = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14), textvariable=predDPI)
    cuadroDPI.grid(row=8, column=1, padx=10, pady=10)

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()

    botonAtras = Button(frame3, text="Atrás", width=10, anchor="center", command=abrirMenu4) #Botón de atrás, que realiza la función abrirMenu4.
    botonAtras.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonAtras.grid(row=0, column=0, padx=150, pady=40)

    botonSiguiente = Button(frame3, text="Siguiente", width=10, anchor="center", command=abrirActualizarN) #Botón de siguiente, que realiza la función abrirActualizarN.
    botonSiguiente.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonSiguiente.grid(row=0, column=1, padx=150, pady=40)

    raiz.mainloop()