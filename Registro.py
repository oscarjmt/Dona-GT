from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image
import csv
import os
import Defensiva as df #Se importan todos los módulos.

#Función para registrar una cuenta de donador.
def donadorRegistro():
    raiz= Tk()
    raiz.title("Donador - Registrarse")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("900x730")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana.
    
    #Función realizada al presionar el botón atrás.
    def abrirLogin1():
        raiz.destroy()
        import Login
        Login.donadorLogin() #Se regresa, abriendo la función de login de donadores.
    
    #Función realizada al presionar el botón siguiente.
    def abrirLogin2():
        nombresD = cuadroNombres.get()
        apellidosD = cuadroApellidos.get()
        correoD = cuadroCorreo.get()
        usuarioD = cuadroUsuario.get()
        passwordD = cuadroPassword.get()
        tarjetaD = cuadroTarjeta.get() #Se obtienen los valores que el usuario escribió en los cuadros de texto.
        listaD = [nombresD, apellidosD, correoD, usuarioD, passwordD, tarjetaD] #Se añade todas esas variables a una lista.
        
        #Se corre la función defensiva para el registro de donadores, con los parámetros de los datos ingresados, en el que si regresa True, entonces se registre la cuenta.
        if df.defenRegistroD(nombresD, apellidosD, correoD, usuarioD, passwordD, tarjetaD, listaD) == True:
            with open('CuentasDonador.csv', 'a+') as archivoCD:
                escribir = csv.writer(archivoCD, lineterminator='\n')
                escribir.writerow(listaD)
                archivoCD.close() #Se escribe la listaD en el archivo de las cuentas de donadores.
            messagebox.showinfo("Registro","Su cuenta ha sido registrada, proceda a iniciar sesión.") #Muestra un mensaje de confrmación.
            raiz.destroy()
            import Login
            Login.donadorLogin() #Se abre la función de login de donadores.

    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Regístrate", width=20, height=2, anchor="center")
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
    
    #Cuadros de texto para cada dato a ingresar.
    cuadroNombres = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroNombres.grid(row=0, column=1, padx=10, pady=10)
    cuadroApellidos = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroApellidos.grid(row=1, column=1, padx=10, pady=10)
    cuadroCorreo = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroCorreo.grid(row=2, column=1, padx=10, pady=10)
    cuadroUsuario = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroUsuario.grid(row=3, column=1, padx=10, pady=10)
    cuadroPassword = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroPassword.grid(row=4, column=1, padx=10, pady=10)
    cuadroPassword.config(show="*")
    cuadroTarjeta = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroTarjeta.grid(row=5, column=1, padx=10, pady=10)

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()

    botonAtras = Button(frame3, text="Atrás", width=10, anchor="center", command=abrirLogin1) #Botón de atrás, que realiza la función abrirLogin1.
    botonAtras.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonAtras.grid(row=0, column=0, padx=150, pady=40)

    botonSiguiente = Button(frame3, text="Siguiente", width=10, anchor="center", command=abrirLogin2) #Botón de siguiente, que realiza la función abrirLogin2.
    botonSiguiente.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonSiguiente.grid(row=0, column=1, padx=150, pady=40)

    raiz.mainloop()

#Función para el registro de solicitantes, con los datos del niño.
def nRegistro(listaS):
    raiz= Tk()
    raiz.title("Solicitante - Registro")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("1000x930")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana.

    RadioS = IntVar() 
    
    #Función que retora el sexo del niño en base a los radiobuttons del sexo.
    def sRadio():
        if RadioS.get() == 1:
            sexoN = "Masculino"
        elif RadioS.get() == 2:
            sexoN = "Femenino"
        else:
            sexoN = "No"
        return(sexoN)
    
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
    
    #Función realizada al presionar el botón de atrás.
    def abrirRegistroS():
        raiz.destroy()
        solicitanteRegistro() #Se regresa, abriendo la función del registro de solicitante de los datos del encargado.
    
    #Función realizada al presionar el botón de siguiente.
    def abrirLogin3():
        nombresN = cuadroNombres.get()
        apellidosN = cuadroApellidos.get()
        sexoN = sRadio()
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
        
        #Se corre la función defensiva para el registro con los datos del niño, con los parámetros de los datos ingresados, en el que si regresa True, entonces se registre la cuenta.
        if df.defenRegistroN(nombresN, apellidosN, sexoN, alturaN, pesoN, departamentoN, municipioN, fechaN, recursosN, listaN) == True:
            for i in range(len(listaN)):
                listaS.append(listaN[i]) #Se agregan los datos del niño de la listaN, a la listaS que envió la función anterior con los datos del encargado.
            messagebox.showinfo("Registro","Su cuenta ha sido registrada, proceda a iniciar sesión.") #Mensaje de confirmación
            with open('CuentasSolicitante.csv', 'a+') as archivoCS:
                escribir = csv.writer(archivoCS, delimiter = ',', lineterminator='\n')
                escribir.writerow(listaS) #Se escribe la listaS en el archivo de las cuentas de solicitantes, ya con todos los datos (de encargado y del niño).
            raiz.destroy()
            import Login
            Login.solicitanteLogin() #Se abre la función de login de solicitantes.
        
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
    
    #Cuadros de texto para cada dato a ingresar.
    cuadroNombres = Entry(frame2, width=22, fg="midnightblue", font=("Calibri", 14))
    cuadroNombres.grid(row=0, column=1, padx=10, pady=10)
    cuadroApellidos = Entry(frame2, width=22, fg="midnightblue", font=("Calibri", 14))
    cuadroApellidos.grid(row=0, column=3, padx=10, pady=10)

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()
    
    #Texto y radiobuttons para seleccionar el sexo del niño.
    textoSexo = Label(frame3, text="Sexo:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoSexo.grid(row=0, column=0, padx=10, sticky="e")
    radioM = Radiobutton(frame3, text="Masculino", width=9, bg="white", fg="midnightblue", font=("Calibri", 11), value=1, variable=RadioS, command=sRadio)
    radioM.grid(row=0, column=1, padx=5)
    radioF = Radiobutton(frame3, text="Femenino", width=9, bg="white", fg="midnightblue", font=("Calibri", 11), value=2, variable=RadioS, command=sRadio)
    radioF.grid(row=1, column=1, padx=5)
    
    #Textos que indican al usuario que debe ingresar.
    textoAltura = Label(frame3, text="Altura (m):", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoAltura.grid(row=0, column=2, padx=10, pady=10, sticky="e")
    textoPeso = Label(frame3, text="Peso (lb):", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoPeso.grid(row=0, column=4, padx=10, pady=10, sticky="e")
    
    #Cuadros de texto para cada dato a ingresar.
    cuadroAltura = Entry(frame3, width=8, fg="midnightblue", font=("Calibri", 14))
    cuadroAltura.grid(row=0, column=3, padx=10, pady=10)
    cuadroPeso = Entry(frame3, width=8, fg="midnightblue", font=("Calibri", 14))
    cuadroPeso.grid(row=0, column=5, padx=10, pady=10)

    frame4 = Frame(raiz, bg="cornflowerblue")
    frame4.pack()
    
    #Textos que indican al usuario que debe ingresar.
    textoDepartamento = Label(frame4, text="Departamento:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoDepartamento.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    textoMunicipio = Label(frame4, text="Municipio:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoMunicipio.grid(row=0, column=2, padx=10, pady=10, sticky="e")
    
    #Cuadros de texto para cada dato a ingresar.
    cuadroDepartamento = Entry(frame4, width=20, fg="midnightblue", font=("Calibri", 14))
    cuadroDepartamento.grid(row=0, column=1, padx=10, pady=10)
    cuadroMunicipio = Entry(frame4, width=20, fg="midnightblue", font=("Calibri", 14))
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
    
    #Cuadros de texto para cada dato a ingresar.
    cuadroFecha = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroFecha.grid(row=0, column=1, padx=10, pady=10)
    cuadroEducacion = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroEducacion.grid(row=1, column=1, padx=10, pady=10)
    cuadroInstitucion = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroInstitucion.grid(row=2, column=1, padx=10, pady=10)
    cuadroTipo = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroTipo.grid(row=3, column=1, padx=10, pady=10)
    cuadroEnfermedades = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroEnfermedades.grid(row=4, column=1, padx=10, pady=10)
    cuadroRecursos = Entry(frame5, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroRecursos.grid(row=5, column=1, padx=10, pady=10)

    frame6 = Frame(raiz, bg="cornflowerblue")
    frame6.pack()

    botonFoto = Button(frame6, text="Sube una foto del niño", anchor="center", command=subirFoto) #Botón para subir la foto del niño, que realiza la función subirFoto.
    botonFoto.config(relief="flat", cursor="hand2", bg="cornflowerblue", fg="white", font=("Calibri", 11))
    botonFoto.grid(row=0, column=0, padx=1, pady=3)

    textoSeparador = Label(frame6, text="|", anchor="center") #Un separador para los botones, por cuestiones visuales.
    textoSeparador.config(bg="cornflowerblue", fg="white", font=("Calibri", 11))
    textoSeparador.grid(row=0, column=1, padx=1, pady=3)

    botonVivienda = Button(frame6, text="Sube una foto de la vivienda", anchor="center", command=subirVivienda) #Botón para subir la foto de la vivienda del niño, que realiza la función subirVivienda.
    botonVivienda.config(relief="flat", cursor="hand2", bg="cornflowerblue", fg="white", font=("Calibri", 11))
    botonVivienda.grid(row=0, column=2, padx=1, pady=3)

    frame7 = Frame(raiz, bg="cornflowerblue")
    frame7.pack()

    botonAtras = Button(frame7, text="Atrás", width=10, anchor="center", command=abrirRegistroS) #Botón de atrás, que realiza la función abrirRegistroS.
    botonAtras.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonAtras.grid(row=0, column=0, padx=150, pady=40)

    botonSiguiente = Button(frame7, text="Siguiente", width=10, anchor="center", command=abrirLogin3) #Botón de siguiente, que realiza la función abrirLogin3.
    botonSiguiente.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonSiguiente.grid(row=0, column=1, padx=150, pady=40)

    raiz.mainloop()

#Función para registrar una cuenta de solicitantes.
def solicitanteRegistro():
    raiz= Tk()
    raiz.title("Solicitante - Registro")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("900x900")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana.
    
    #Función realizada al preionar el botón de atrás
    def abrirLogin4():
        raiz.destroy()
        import Login
        Login.solicitanteLogin() #Se regresa, abriendo la función de login para solicitantes.
     
    #Función realizada al presionar el botón de siguiente.
    def abrirRegistroN():
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
        
        #Se corre la función defensiva para el registro de solicitantes, con los parámetros de los datos ingresados, en el que si regresa True, entonces continue con el ingreso de los datos del niño.
        if df.defenRegistroS(nombresS, apellidosS, parentescoS, ocupacionS, telefonoS, correoS, usuarioS, passwordS, dpiS, listaS) == True:
            messagebox.showinfo("Registro","Sus datos han sido guardados, proceda a ingresar los datos del niño.") #Muestra un mensaje de continuación.
            raiz.destroy()
            listaS = [nombresS, apellidosS, parentescoS, ocupacionS, telefonoS, correoS, usuarioS, passwordS, dpiS]
            nRegistro(listaS) #Se abre la función del registro con los datos del niño, utilizando como parámetro la listaS con los datos del encargado.

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
    
    #Cuadros de texto para cada dato a ingresar.
    cuadroNombres = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroNombres.grid(row=0, column=1, padx=10, pady=10)
    cuadroApellidos = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroApellidos.grid(row=1, column=1, padx=10, pady=10)
    cuadroParentesco = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroParentesco.grid(row=2, column=1, padx=10, pady=10)
    cuadroOcupacion = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroOcupacion.grid(row=3, column=1, padx=10, pady=10)
    cuadroTelefono = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroTelefono.grid(row=4, column=1, padx=10, pady=10)
    cuadroCorreo = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroCorreo.grid(row=5, column=1, padx=10, pady=10)
    cuadroUsuario = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroUsuario.grid(row=6, column=1, padx=10, pady=10)
    cuadroPassword = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroPassword.grid(row=7, column=1, padx=10, pady=10)
    cuadroPassword.config(show="*")
    cuadroDPI = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroDPI.grid(row=8, column=1, padx=10, pady=10)

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()

    botonAtras = Button(frame3, text="Atrás", width=10, anchor="center", command=abrirLogin4) #Botón de atrás, que realiza la función abrirLogin4.
    botonAtras.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonAtras.grid(row=0, column=0, padx=150, pady=40)

    botonSiguiente = Button(frame3, text="Siguiente", width=10, anchor="center", command=abrirRegistroN) #Botón de siguiente, que realiza la función abrirRegistroN.
    botonSiguiente.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonSiguiente.grid(row=0, column=1, padx=150, pady=40)

    raiz.mainloop()
