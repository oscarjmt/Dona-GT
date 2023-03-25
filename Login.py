from tkinter import *
import csv
import Defensiva as df #Se importa tkinter, csv y el módulo de la programación defensiva.

#Función de login para donadores.
def donadorLogin():
    raiz= Tk()
    raiz.title("Donador - Log In")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("900x550")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana gráfica.
    
    #Función realizada al presionar el botón de atrás.
    def abrirEscoger1():
        raiz.destroy()
        import Iniciar
        Iniciar.escogerAccion() #Se abre la función de escogerAccion, regresa en otras palabras.
    
    #Función realizada al presionar el botón de siguiente.
    def abrirMenu1(): 
        usuarioD = cuadroUsuario.get() 
        passwordD = cuadroPassword.get() #Se obtienen los valores que el usuario escribió en los cuadros de texto.
        
        listaCuentasD = []
        with open("CuentasDonador.csv", "r") as archivoCD:
            leer = csv.reader(archivoCD, delimiter=',')
            for filas in leer:
                listaCuentasD.append(filas)
            archivoCD.close() #Se lee el archivo de las cuentas de donadores, y por cada cuenta toda su información en una lista, se agrega a la listaCuentasD que contendrá todas las cuentas.
        
        listaDonador = []
        
        #Se corre la función defensiva para el login de donadores con los parámetros de usuario y contraseña, en el que si regresa True, entonces si incie sesión.
        if df.defenLoginD(usuarioD, passwordD) == True:
            for i in range(len(listaCuentasD)):
                if listaCuentasD[i][3] == usuarioD:
                    listaDonador = listaCuentasD[i] #En dado caso si sea correcto, en la lista donde se encuentre el usuario ingresado, se guarda una copia el la listaDonador.
            raiz.destroy()
            import MenuDonador
            MenuDonador.donadorBusqueda(listaDonador)
            #Se corre la función de la busqueda para donadores (el menú), con el parámetro de la listaDonador con los datos de la cuenta que inició sesión.
            #De esta forma el programa sabe quien es el usuario que está dentro de la aplicación.
    
    #Función realizada al presionar el botón de registrarse.
    def abrirRegistrar1():
        raiz.destroy()
        import Registro
        Registro.donadorRegistro() #Se abre la función de registro para donadores.
    
    #Función realizada al presionar el botón de que olvidó la contraseña.
    def abrirCambiar1():
        raiz.destroy()
        import CambiarPassword
        CambiarPassword.cambiarDonador() #Se abre la función para cambiar la contraseña de donadores.

    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Bienvenido", width=20, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 25))
    textoBienvenido.grid(row=0, column=0, padx=20, pady=40, sticky="w") 

    logo = PhotoImage(file="Logo.png")
    logo2 = Label(frame1, image=logo)
    logo2.grid(row=0, column=1, padx=20, pady=40, sticky="e") #Primer frame con el mensaje de bienvenido y el logo.

    frame2 = Frame(raiz, bg="cornflowerblue")
    frame2.pack()
    
    #Textos que indican al usuario que debe ingresar.
    textoUsuario = Label(frame2, text="Nombre de usuario:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoUsuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    textoPassword = Label(frame2, text="Contraseña:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoPassword.grid(row=1, column=0, padx=10, pady=10, sticky="e") #Textos que indican al usuario que debe ingresar.
    
    #Cuadros de texto para cada dato a ingresar.
    cuadroUsuario = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroUsuario.grid(row=0, column=1, padx=10, pady=10)
    cuadroPassword = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroPassword.grid(row=1, column=1, padx=10, pady=10)
    cuadroPassword.config(show="*")

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()

    botonCambiar = Button(frame3, text="¿Olvidaste tu contraseña?", anchor="center", command=abrirCambiar1) #Botón de que olvidó la contraseña, que realiza la función abrirCambiar1.
    botonCambiar.config(relief="flat", cursor="hand2", bg="cornflowerblue", fg="white", font=("Calibri", 11))
    botonCambiar.grid(row=0, column=0, padx=1, pady=3)

    textoSeparador = Label(frame3, text="|", anchor="center") #Un separador para los botones, por cuestiones visuales.
    textoSeparador.config(bg="cornflowerblue", fg="white", font=("Calibri", 11))
    textoSeparador.grid(row=0, column=1, padx=1, pady=3)

    botonRegistrarse = Button(frame3, text="Regístrate", anchor="center", command=abrirRegistrar1) #Botón de registrarse, que realiza la función de abrirRegistar1.
    botonRegistrarse.config(relief="flat", cursor="hand2", bg="cornflowerblue", fg="white", font=("Calibri", 11))
    botonRegistrarse.grid(row=0, column=2, padx=1, pady=3)

    frame4 = Frame(raiz, bg="cornflowerblue")
    frame4.pack()

    botonAtras = Button(frame4, text="Atrás", width=10, anchor="center", command=abrirEscoger1) #Botón de atrás, que realiza la función abrirEscoger1.
    botonAtras.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonAtras.grid(row=0, column=0, padx=150, pady=40)

    botonSiguiente = Button(frame4, text="Siguiente", width=10, anchor="center", command=abrirMenu1) #Botón de siguiente, que realiza la función abrirMenu1.
    botonSiguiente.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonSiguiente.grid(row=0, column=1, padx=150, pady=40)

    raiz.mainloop()

#Función de login para solicitantes
def solicitanteLogin():
    raiz= Tk()
    raiz.title("Solicitante - Log In")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("900x550")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana.
    
    #Función realizada al presionar el botón de atrás.
    def abrirEscoger2():
        raiz.destroy()
        import Iniciar
        Iniciar.escogerAccion() #Se abre la función de escogerAccion, regresa en otras palabras.
    
    #Función realizada al presionar el botón siguiente
    def abrirMenu2():
        usuarioS = cuadroUsuario.get()
        passwordS = cuadroPassword.get() #Se obtienen los valores que el usuario escribió en los cuadros de texto.
        
        listaCuentasS = []
        with open("CuentasSolicitante.csv", "r", encoding="latin-1") as archivoCS:
            leer = csv.reader(archivoCS, delimiter=',')
            for filas in leer:
                listaCuentasS.append(filas)
            archivoCS.close() #Se lee el archivo de las cuentas de solicitantes, y por cada cuenta toda su información en una lista, se agrega a la listaCuentasS que contendrá todas las cuentas.
        
        listaSolicitante = []
        
        #Se corre la función defensiva para el login de solicitantes con los parámetros de usuario y contraseña, en el que si regresa True, entonces si incie sesión.
        if df.defenLoginS(usuarioS, passwordS) == True:
            for i in range(len(listaCuentasS)):
                if listaCuentasS[i][6] == usuarioS:
                    listaSolicitante = listaCuentasS[i]    
            raiz.destroy()
            import MenuSolicitante
            MenuSolicitante.solicitanteDonaciones(listaSolicitante)
            #Se corre la función de la donaciones recibidas por el solicitante (el menú), con el parámetro de la listaSolicitante con los datos de la cuenta que inició sesión.
            #De esta forma el programa sabe quien es el usuario que está dentro de la aplicación.
    
    #Función realizada al presionar el botón de registrarse.
    def abrirRegistrar2():
        raiz.destroy()
        import Registro
        Registro.solicitanteRegistro()  #Se abre la función de registro para solicitantes.
    
    #Función realizada al presionar el botón de que olvidó la contraseña.
    def abrirCambiar2():
        raiz.destroy()
        import CambiarPassword
        CambiarPassword.cambiarSolicitante() #Se abre la función para cambiar la contraseña de solicitantes.
        
    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Bienvenido", width=20, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 25))
    textoBienvenido.grid(row=0, column=0, padx=20, pady=40, sticky="w") 

    logo = PhotoImage(file="Logo.png")
    logo2 = Label(frame1, image=logo)
    logo2.grid(row=0, column=1, padx=20, pady=40, sticky="e") #Primer frame con el mensaje de bienvenido y el logo.

    frame2 = Frame(raiz, bg="cornflowerblue")
    frame2.pack()
    
    #Textos que indican al usuario que debe ingresar.
    textoUsuario = Label(frame2, text="Nombre de usuario:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoUsuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    textoPassword = Label(frame2, text="Contraseña:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoPassword.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    
    #Cuadros de texto para cada dato a ingresar.
    cuadroUsuario = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroUsuario.grid(row=0, column=1, padx=10, pady=10)
    cuadroPassword = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroPassword.grid(row=1, column=1, padx=10, pady=10)
    cuadroPassword.config(show="*")

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()

    botonCambiar = Button(frame3, text="¿Olvidaste tu contraseña?", anchor="center", command=abrirCambiar2) #Botón de que olvidó la contraseña, que realiza la función abrirCambiar2.
    botonCambiar.config(relief="flat", cursor="hand2", bg="cornflowerblue", fg="white", font=("Calibri", 11))
    botonCambiar.grid(row=0, column=0, padx=1, pady=3)

    textoSeparador = Label(frame3, text="|", anchor="center") #Un separador para los botones, por cuestiones visuales.
    textoSeparador.config(bg="cornflowerblue", fg="white", font=("Calibri", 11))
    textoSeparador.grid(row=0, column=1, padx=1, pady=3)

    botonRegistrarse = Button(frame3, text="Regístrate", anchor="center", command=abrirRegistrar2) #Botón de registrarse, que realiza la función de abrirRegistar2.
    botonRegistrarse.config(relief="flat", cursor="hand2", bg="cornflowerblue", fg="white", font=("Calibri", 11))
    botonRegistrarse.grid(row=0, column=2, padx=1, pady=3)

    frame4 = Frame(raiz, bg="cornflowerblue")
    frame4.pack()

    botonAtras = Button(frame4, text="Atrás", width=10, anchor="center", command=abrirEscoger2) #Botón de atrás, que realiza la función abrirEscoger2.
    botonAtras.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonAtras.grid(row=0, column=0, padx=150, pady=40)

    botonSiguiente = Button(frame4, text="Siguiente", width=10, anchor="center", command=abrirMenu2) #Botón de siguiente, que realiza la función abrirMenu2.
    botonSiguiente.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonSiguiente.grid(row=0, column=1, padx=150, pady=40)

    raiz.mainloop()
