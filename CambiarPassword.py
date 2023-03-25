from tkinter import *
import csv
import Defensiva as df #Se importa tkinter, csv y el módulo de la programación defensiva.

#Función para cambiar la contraseña de donador.
def cambiarDonador():
    raiz= Tk()
    raiz.title("Donador - Cambiar contraseña")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("900x550")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana.

    #Función realizada al presionar el botón de atrás.
    def abrirLogin1():
        raiz.destroy()
        import Login
        Login.donadorLogin() #Se regresa, abriendo la función de login de donadores.
    
    #Función realizada al presionar el botón de siguiente.
    def abrirLogin2():
        correoD = cuadroCorreo.get()
        usuarioD = cuadroUsuario.get()
        passwordD = cuadroPassword.get() #Se obtienen los valores que el usuario escribió en los cuadros de texto.
        
        listaCuentasD = []
        with open("CuentasDonador.csv", "r") as archivoCD:
            leer = csv.reader(archivoCD, delimiter=',')
            for filas in leer:
                listaCuentasD.append(filas)
            archivoCD.close() #Se lee el archivo de las cuentas de donadores, y por cada cuenta toda su información en una lista, se agrega a la listaCuentasD que contendrá todas las cuentas.
        
        #Se corre la función defensiva para el cambio de contraseña para donadores, con los parámetros de los datos ingresados, en el que si regresa True, entonces si cambie la contraseña.
        if df.defenCambiarD(correoD, usuarioD, passwordD) == True:
            #Se crea un ciclo para que encuentre la lista de la cuenta que contiene el correo ingresado, y en esa lista cambiar la contraseña ingresada en la posición que va la contraseña.
            for i in range(len(listaCuentasD)):
                if listaCuentasD[i][2] == correoD:
                    listaCuentasD[i][4] = passwordD
            with open('CuentasDonador.csv', 'w') as archivoCD:
                for i in range(len(listaCuentasD)):
                    escribir = csv.writer(archivoCD, lineterminator='\n')
                    escribir.writerow(listaCuentasD[i])
                archivoCD.close() #Se sobreescribre en el archivo de las cuentas de donadores, cada sublista de la listaCuentasD. 
            messagebox.showinfo("Cambiar contraseña","Su contraseña se ha cambiado, proceda ha iniciar sesión") #Muestra un mensaje de confrmación.
            raiz.destroy()
            import Login
            Login.donadorLogin() #Se abre la función de login de donadores.

    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Cambie su contraseña", width=20, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 25))
    textoBienvenido.grid(row=0, column=0, padx=20, pady=40, sticky="w") 

    logo = PhotoImage(file="Logo.png")
    logo2 = Label(frame1, image=logo)
    logo2.grid(row=0, column=1, padx=20, pady=40, sticky="e") #Primer frame con el mensaje cambie su contraseña y el logo.

    frame2 = Frame(raiz, bg="cornflowerblue")
    frame2.pack()
    
    #Textos que indican al usuario que debe ingresar.
    textoUsuario = Label(frame2, text="Nombre de usuario:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoUsuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    textoCorreo = Label(frame2, text="Correo electrónico:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoCorreo.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    textoPassword = Label(frame2, text="Nueva contraseña:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoPassword.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    
    #Cuadros de texto para cada dato a ingresar.
    cuadroUsuario = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroUsuario.grid(row=0, column=1, padx=10, pady=10)
    cuadroCorreo = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroCorreo.grid(row=1, column=1, padx=10, pady=10)
    cuadroPassword = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroPassword.grid(row=2, column=1, padx=10, pady=10)
    cuadroPassword.config(show="*")

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()

    botonAtras = Button(frame3, text="Atrás", width=10, anchor="center", command=abrirLogin1) #Botón de atrás, que realiza la función abrirLogin1.
    botonAtras.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonAtras.grid(row=0, column=0, padx=150, pady=40)

    botonSiguiente = Button(frame3, text="Siguiente", width=10, anchor="center", command=abrirLogin2) #Botón de siguinte, que realiza la función abrirLogin2.
    botonSiguiente.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonSiguiente.grid(row=0, column=1, padx=150, pady=40)

    raiz.mainloop()

#Función para cambiar la contraseña del solicitnate.
def cambiarSolicitante():
    raiz= Tk()
    raiz.title("Solicitante - Cambiar contraseña")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("900x550")
    raiz.config(bg="cornflowerblue") #
    
    #Función realizada al presionar el botón atrás.
    def abrirLogin3():
        raiz.destroy()
        import Login
        Login.solicitanteLogin() #Se regresa, abriendo la función de login de solicitantes.
    
    #Función realizada al presionar el botón siguiente.
    def abrirLogin4():
        correoS = cuadroCorreo.get()
        usuarioS = cuadroUsuario.get()
        passwordS = cuadroPassword.get() #Se obtienen los valores que el usuario escribió en los cuadros de texto.
        
        listaCuentasS = []
        with open("CuentasSolicitante.csv", "r") as archivoCS:
            leer = csv.reader(archivoCS, delimiter=',')
            for filas in leer:
                listaCuentasS.append(filas)
            archivoCS.close() #Se lee el archivo de las cuentas de solicitantes, y por cada cuenta toda su información en una lista, se agrega a la listaCuentasS que contendrá todas las cuentas.
        
        #Se corre la función defensiva para el cambio de contraseña para solicitantes, con los parámetros de los datos ingresados, en el que si regresa True, entonces si cambie la contraseña.    
        if df.defenCambiarS(correoS, usuarioS, passwordS) == True:
            #Se crea un ciclo para que encuentre la lista de la cuenta que contiene el correo ingresado, y en esa lista cambiar la contraseña ingresada en la posición que va la contraseña.
            for i in range(len(listaCuentasS)):
                if listaCuentasS[i][5] == correoS:
                    listaCuentasS[i][7] = passwordS
            with open('CuentasSolicitante.csv', 'w') as archivoCS:
                for i in range(len(listaCuentasS)):
                    escribir = csv.writer(archivoCS, lineterminator='\n')
                    escribir.writerow(listaCuentasS[i])
                archivoCS.close() #Se sobreescribre en el archivo de las cuentas de solicitantes, cada sublista de la listaCuentasS. 
            messagebox.showinfo("Cambiar contraseña","Su contraseña se ha cambiado, proceda ha iniciar sesión") #Muestra un mensaje de confrmación.
            raiz.destroy()
            import Login
            Login.solicitanteLogin() #Se abre la función de login de solicitantes.

    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Cambie su contraseña", width=20, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 25))
    textoBienvenido.grid(row=0, column=0, padx=20, pady=40, sticky="w") 

    logo = PhotoImage(file="Logo.png")
    logo2 = Label(frame1, image=logo)
    logo2.grid(row=0, column=1, padx=20, pady=40, sticky="e") #Primer frame con el mensaje cambie su contraseña y el logo.

    frame2 = Frame(raiz, bg="cornflowerblue")
    frame2.pack()

    #Textos que indican al usuario que debe ingresar.
    textoUsuario = Label(frame2, text="Nombre de usuario:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoUsuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    textoCorreo = Label(frame2, text="Correo electrónico:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoCorreo.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    textoPassword = Label(frame2, text="Nueva contraseña:", bg="cornflowerblue", fg="white", font=("Calibri", 16))
    textoPassword.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    
    #Cuadros de texto para cada dato a ingresar.
    cuadroUsuario = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroUsuario.grid(row=0, column=1, padx=10, pady=10)
    cuadroCorreo = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroCorreo.grid(row=1, column=1, padx=10, pady=10)
    cuadroPassword = Entry(frame2, width=25, fg="midnightblue", font=("Calibri", 14))
    cuadroPassword.grid(row=2, column=1, padx=10, pady=10)
    cuadroPassword.config(show="*")

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()

    botonAtras = Button(frame3, text="Atrás", width=10, anchor="center", command=abrirLogin3) #Botón de atrás, que realiza la función abrirLogin3.
    botonAtras.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonAtras.grid(row=0, column=0, padx=150, pady=40)

    botonSiguiente = Button(frame3, text="Siguiente", width=10, anchor="center", command=abrirLogin4) #Botón de siguiente que realiza la función de abrirLogin4.
    botonSiguiente.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonSiguiente.grid(row=0, column=1, padx=150, pady=40)

    raiz.mainloop()
