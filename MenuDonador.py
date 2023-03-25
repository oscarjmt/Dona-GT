from tkinter import * #Se importa tkinter.
from datetime import datetime
from datetime import date
import PIL
from PIL import ImageTk, Image
import csv
import os
import Estadisticas as est
import Defensiva as df

#Función para la parte del menú donde se busca a solicitantes a quien donarles (Menú donadores).
def donadorBusqueda(listaDonador):
    raiz= Tk()
    raiz.title("Donador - Menu")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("1000x840")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana.
    
    #Función para abrir las estadísticas.
    def abrirEstadisticas():
        est.donadorEst(listaDonador) #Se abre la función que muestra las donaciones por mes.
        
    #Función realizada al presionar el botón de mis donaciones.
    def abrirDonaciones():
        raiz.destroy()
        donadorDonaciones(listaDonador) #Se abre la función de la donaciones realizadas, tambien parte del menú.
    
    #Función realizada al preisonar el botón de actualizar info.
    def abrirActualizar1():
        raiz.destroy()
        import Actualizar
        Actualizar.donadorActualizar(listaDonador) #Se abre la función de actualizar la información de donadores.
        #Se utiliza el parámetro de la listaDonador que había enviado el login, para que los datos ya esten puestos a la hora de actualizarlos.
    
    #Función realizada al presionar el botón de cerrar sesión.
    def abrirLogin1():
        raiz.destroy()
        import Login
        Login.donadorLogin() #Se regres, abriendo la función de login de donadores.

    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Buscar solicitantes", width=20, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 25))
    textoBienvenido.grid(row=0, column=0, padx=20, pady=30, sticky="w") 

    logo = PhotoImage(file="Logo.png")
    logo2 = Label(frame1, image=logo)
    logo2.grid(row=0, column=1, padx=20, pady=30, sticky="e") #Primer frame con el mensaje Buscar solicitantes y el logo.

    frame2 = Frame(raiz, bg="cornflowerblue")
    frame2.pack()
    
    totalDonado = est.totalDonado(listaDonador)
    textoTotal = Label(frame2, text=("Total Donado:  " + totalDonado), bg="cornflowerblue", fg="white", font=("Calibri", 14))
    textoTotal.grid(row=0, column=0, padx=30, sticky="w") #Muestra el total donado.
    
    botonEstadisticas = Button(frame2, text="Mostrar Estadísticas", width=16, anchor="center", command=abrirEstadisticas) #Botón de estadisticas
    botonEstadisticas.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 14))
    botonEstadisticas.grid(row=0, column=1, padx=30, sticky="w")

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()
    
    #Se crea un canvas, donde irían todos los solicitantes con la info escencial y la foto del niño, y al seleccionar uno abriría una ventana con toda la info y la opción de donar.
    canvas = Canvas(frame3, highlightthickness=0, bg="cornflowerblue", width=650, height=420, cursor="hand2")
    canvas.grid(row=0, column=0, padx=10, pady=35, sticky="w")
    sb = Scrollbar(frame3, orient="vertical", command=canvas.yview)
    sb.grid(row=0, column=1, padx=15, pady=35, sticky="ns")
    canvas.config(yscrollcommand=sb.set)
    
    LS = []
    with open("CuentasSolicitante.csv", "r") as archivoCS:
        leer = csv.reader(archivoCS, delimiter=',')
        for filas in leer:
            LS.append(filas)
        archivoCS.close() #Se crea una lista con todas las cuentas de los solicitantes
    
    def abrirDonar(event):
        for i in range(len(LS)):
            mov2 = i*215
            coordSB = list(sb.get())
            coordY = ((len(LS)-1)*215) + 200 - (420/coordSB[1]) + event.y #Algoritmo para saber donde se preiona en el area del canvas. Utilizando la coordenada "Y" máxima de toda el área, la coordenada del slider, y la coordenada "Y" del click. 
            if (coordY > 0+mov2) and (coordY < 200+mov2):
                listaSolicitante = LS[i]
                import Donar
                Donar.datosDonacion(raiz, listaDonador, listaSolicitante) #Se abre la función para donar, con los parámetros establecidos.
                break
    
    imagenes = []
    
    for i in range(len(LS)):
        #Se obtiene la edad en base a la fecha de nacimiento.
        hoy = date.today()
        nacimiento = datetime.strptime(LS[i][16], "%d/%m/%Y")
        if nacimiento.month < hoy.month:
            edad = hoy.year - nacimiento.year
        elif nacimiento.month > hoy.month:
            edad = hoy.year - nacimiento.year - 1
        elif nacimiento.month == hoy.month:
            if nacimiento.day > hoy.day:
                edad = hoy.year - nacimiento.year -1
            else:
                edad = hoy.year - nacimiento.year

        mov = i*215 #Movimiento entre cada solicitante
        
        #Rectángulo y texto del solicitante.
        botonS = canvas.create_rectangle(5, 5+mov, 620, 200+mov, fill="#1190CB", outline="white", width=5)
        ctNombres = canvas.create_text(215, 40+mov, text=("NOMBRES:"), anchor="w", fill="#d6e8fc", font=("Calibri", 12))
        ctApellidos = canvas.create_text(215, 80+mov, text=("APELLIDOS:"), anchor="w", fill="#d6e8fc", font=("Calibri", 12))
        ctEdad = canvas.create_text(215, 120+mov, text=("EDAD:"), anchor="w", fill="#d6e8fc", font=("Calibri", 12))
        ctUbicacion = canvas.create_text(215, 160+mov, text="UBICACIÓN:", anchor="w", fill="#d6e8fc", font=("Calibri", 12))
        
        ctNombres2 = canvas.create_text(312, 39+mov, text=LS[i][9], anchor="w", fill="white", font=("Calibri", 14))
        ctApellidos2 = canvas.create_text(316, 79+mov, text=LS[i][10], anchor="w", fill="white", font=("Calibri", 14))
        ctEdad2 = canvas.create_text(275, 119+mov, text=str(edad), anchor="w", fill="white", font=("Calibri", 14))
        ctUbicacion2 = canvas.create_text(322, 159+mov, text=(LS[i][15]+", "+LS[i][14]), anchor="w", fill="white", font=("Calibri", 14))
        
        #Imagen del solicitante
        try:
            archivo = os.getcwd() + "\\Fotos\\" + LS[i][6] + "(1).png" #Se saca la dirección de la imagen.
            foto = ImageTk.PhotoImage(Image.open(archivo)) #Se obtiene esa imagen y se guarda como una imagen de Tkinter.
        except:
            foto = ImageTk.PhotoImage(Image.open("ImagenPrueba1.png")) #Si no existe, entonces guarda la imagen de prueba.
        imagenes.append(foto) #Se agrega a la lista de imagenes para que no se pierdan los valores cuando se reinicie el ciclo.
        imagen = canvas.create_image(102.5, 102.5+mov, image=imagenes[i]) #Se crea la imagen.
        
        #A los elementos creados en el canvas se le pone un tag_bind, para que cuando se les haga click realicen la función abrirDonar.
        canvas.tag_bind(botonS, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctNombres, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctApellidos, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctEdad, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctUbicacion, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctNombres2, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctApellidos2, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctEdad2, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctUbicacion2, "<Button-1>", abrirDonar)
        canvas.tag_bind(imagen, "<Button-1>", abrirDonar)
    
    canvas.config(scrollregion=canvas.bbox(ALL))
    
    frame4 = Frame(raiz, bg="cornflowerblue")
    frame4.pack()

    botonBusqueda = Button(frame4, text="Búsqueda", width=13, anchor="center") #Botón de búsqueda, no hace nada pero da la ilusión de que se trabaja en el mismo menú.
    botonBusqueda.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonBusqueda.grid(row=0, column=0, padx=20, pady=10)

    botonDonaciones = Button(frame4, text="Mis donaciones", width=13, anchor="center", command=abrirDonaciones) #Botón de mis donaciones, que realiza la función abrirDonaciones.
    botonDonaciones.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonDonaciones.grid(row=0, column=1, padx=20, pady=10)

    botonActualizar = Button(frame4, text="Actualizar info.", width=13, anchor="center", command=abrirActualizar1) #Botón de actualizar info, que realiza la función abrirActualizar1.
    botonActualizar.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonActualizar.grid(row=0, column=2, padx=20, pady=10)

    botonCerrar = Button(frame4, text="Cerrar sesión", width=11, anchor="se", command=abrirLogin1) #Botón de cerrar sesión, que realiza la función abrirLogin1.
    botonCerrar.config(cursor="hand2", relief="flat", bg="cornflowerblue", fg="white", font=("Calibri", 14,))
    botonCerrar.grid(row=0, column=3, padx=10, pady=10, sticky="e")

    raiz.mainloop()

#Función para la parte del menú donde están todas las donaciones hechas del donador (Menú donadores).
def donadorDonaciones(listaDonador):
    raiz= Tk()
    raiz.title("Donador - Menu")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("1000x840")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana.  
    
    #Función para abrir las estadísticas
    def abrirEstadisticas():
        est.donadorEst(listaDonador) #Se abre la función que muestra las donaciones por mes.
    
    #Función realizada al presionar el botón de búsqueda.
    def abrirBusqueda():
        raiz.destroy()
        donadorBusqueda(listaDonador) #Se abre la función de búsqueda de solicitantes, tambien parte del menú.
    
    #Función realizada al preisonar el botón de actualizar info.
    def abrirActualizar2():
        raiz.destroy()
        import Actualizar
        Actualizar.donadorActualizar(listaDonador) #Se abre la función de actualizar la información de donadores.
        #Se utiliza el parámetro de la listaDonador que había enviado el login, para que los datos ya esten puestos a la hora de actualizarlos.
    
    #Función realizada al presionar el botón de cerrar sesión.
    def abrirLogin2():
        raiz.destroy()
        import Login
        Login.donadorLogin() #Se regresa, abriendo la función de login de donadores.

    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Donaciones realizadas", width=20, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 25))
    textoBienvenido.grid(row=0, column=0, padx=20, pady=30, sticky="w") 

    logo = PhotoImage(file="Logo.png")
    logo2 = Label(frame1, image=logo)
    logo2.grid(row=0, column=1, padx=20, pady=30, sticky="e") #Primer frame con el mensaje Donaciones realizadas y el logo.

    frame2 = Frame(raiz, bg="cornflowerblue")
    frame2.pack()

    totalDonado = est.totalDonado(listaDonador)
    textoTotal = Label(frame2, text=("Total Donado:  " + totalDonado), bg="cornflowerblue", fg="white", font=("Calibri", 14))
    textoTotal.grid(row=0, column=0, padx=30, sticky="w") #Muestra el total donado.
    
    botonEstadisticas = Button(frame2, text="Mostrar Estadísticas", width=16, anchor="center", command=abrirEstadisticas) #Botón de buscar.
    botonEstadisticas.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 14))
    botonEstadisticas.grid(row=0, column=1, padx=30, sticky="w")

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()
    
    #Se crea un canvas, donde irían todas las donaciones realizadas, y al seleccionar uno abriría una ventana con toda la información y la opción de donar más.
    canvas = Canvas(frame3, highlightthickness=0, bg="cornflowerblue", width=650, height=420, cursor="hand2")
    canvas.grid(row=0, column=0, padx=10, pady=35, sticky="w")
    sb = Scrollbar(frame3, orient="vertical", command=canvas.yview)
    sb.grid(row=0, column=1, padx=15, pady=35, sticky="ns")
    canvas.config(yscrollcommand=sb.set)
    
    LS = []
    with open("CuentasSolicitante.csv", "r") as archivoCS:
        leer = csv.reader(archivoCS, delimiter=',')
        for filas in leer:
            LS.append(filas)
        archivoCS.close() #Se crea una lista con todas las cuentas de los solicitantes
    
    LDR = []
    with open("DonacionesRealizadas.csv", "r") as archivoDR:
        leer2 = csv.reader(archivoDR, delimiter=',')
        for filas2 in leer2:
            LDR.append(filas2)
        archivoDR.close() #Se crea una lista con todas las cuentas de los solicitantes
    
    LDR2 = []
    for i in range(len(LDR)):
        if LDR[i][0] == listaDonador[3]:
            LDR2.append(LDR[i])

    for i in range(len(LDR2)):
        
        def abrirDonar(event):
            for i in range(len(LDR2)):
                mov2 = i*120
                if (((len(LDR2)-1)*120) + 100) > 420:
                    coordSB = list(sb.get())
                    coordY = ((len(LDR2)-1)*120) + 100 - (420/coordSB[1]) + event.y #Algoritmo para saber donde se preiona en el area del canvas. Utilizando la coordenada "Y" máxima de toda el área, la coordenada del slider, y la coordenada "Y" del click.
                    if (coordY > 0+mov2) and (coordY < 100+mov2):
                        for e in range(len(LS)):
                            if LS[e][6] == LDR2[i][1]:
                                listaSolicitante = LS[e]
                                import Donar
                                donacion = Donar.datosDonacion(raiz, listaDonador, listaSolicitante) #Se abre la función para donar con los parámetros establecidos.
                                break
                else:
                    if (event.y > 0+mov2) and (event.y < 100+mov2):
                        for e in range(len(LS)):
                            if LS[e][6] == LDR2[i][1]:
                                listaSolicitante = LS[e]
                                import Donar
                                Donar.datosDonacion(raiz, listaDonador, listaSolicitante) #Se abre la función para donar con los parámetros establecidos.
                                break
        
        #Se obtiene el motno de la donación en forma amigable al usuario.
        montoDR = str(LDR2[i][4])
        totalDonado = df.transformarMonto(montoDR)
        
        mov = i*120 #Movimiento vertical entre cada registro.
        
        #Rectángulo y texto de la donación
        botonS = canvas.create_rectangle(5, 5+mov, 640, 100+mov, fill="skyblue", outline="white", width=0)
        botonS2 = canvas.create_rectangle(15, 15+mov, 630, 90+mov, fill="#1190CB", outline="white", width=3)
        ctNombres = canvas.create_text(30, 40+mov, text=("NOMBRES:"), anchor="w", fill="#d6e8fc", font=("Calibri", 12))
        ctApellidos = canvas.create_text(30, 70+mov, text=("APELLIDOS:"), anchor="w", fill="#d6e8fc", font=("Calibri", 12))
        ctMonto = canvas.create_text(350, 40+mov, text=("MONTO:"), anchor="w", fill="#d6e8fc", font=("Calibri", 12))
        ctFecha = canvas.create_text(350, 70+mov, text=("FECHA:"), anchor="w", fill="#d6e8fc", font=("Calibri", 12))

        ctNombres2 = canvas.create_text(127, 39+mov, text=LDR2[i][2], anchor="w", fill="white", font=("Calibri", 14))
        ctApellidos2 = canvas.create_text(130, 69+mov, text=LDR2[i][3], anchor="w", fill="white", font=("Calibri", 14))
        ctMonto2 = canvas.create_text(430, 39+mov, text=totalDonado , anchor="w", fill="white", font=("Calibri", 14))
        ctFecha2 = canvas.create_text(420, 69+mov, text=LDR2[i][5], anchor="w", fill="white", font=("Calibri", 14))
        
        #A los elementos creados en el canvas se le pone un tag_bind, para que cuando se les haga click realicen la función abrirDonar.
        canvas.tag_bind(botonS, "<Button-1>", abrirDonar)
        canvas.tag_bind(botonS2, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctNombres, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctApellidos, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctMonto, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctFecha, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctNombres2, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctApellidos2, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctMonto2, "<Button-1>", abrirDonar)
        canvas.tag_bind(ctFecha2, "<Button-1>", abrirDonar)
        
        canvas.config(scrollregion=canvas.bbox("all"))
    
    frame4 = Frame(raiz, bg="cornflowerblue")
    frame4.pack()

    botonBusqueda = Button(frame4, text="Búsqueda", width=13, anchor="center", command=abrirBusqueda) #Botón de búsqueda, que realiza la función abrirBúsqueda.
    botonBusqueda.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonBusqueda.grid(row=0, column=0, padx=20, pady=10)

    botonDonaciones = Button(frame4, text="Mis donaciones", width=13, anchor="center") #Botón de mis donaciones, no hace nada pero da la ilusión de que se trabaja en el mismo menú.
    botonDonaciones.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonDonaciones.grid(row=0, column=1, padx=20, pady=10)

    botonActualizar = Button(frame4, text="Actualizar info.", width=13, anchor="center", command=abrirActualizar2) #Botón de actualizar info, que realiza la función abrirActualizar2.
    botonActualizar.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonActualizar.grid(row=0, column=2, padx=20, pady=10)

    botonCerrar = Button(frame4, text="Cerrar sesión", width=11, anchor="se", command=abrirLogin2) #Botón de cerrar sesión, que realiza la función abrirLogin2.
    botonCerrar.config(cursor="hand2", relief="flat", bg="cornflowerblue", fg="white", font=("Calibri", 14,)) 
    botonCerrar.grid(row=0, column=3, padx=10, pady=10, sticky="e")

    raiz.mainloop()