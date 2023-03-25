from tkinter import *
import csv
import Estadisticas as est
import Defensiva as df

#Función para ver todas las donaciones recibidas a los solicitnates (Menu solicitantes).
def solicitanteDonaciones(listaSolicitante):
    raiz= Tk()
    raiz.title("Solicitante - Menu")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("1000x840")
    raiz.config(bg="cornflowerblue") #Propiedades generales de la ventana.
    
    #Función para abrir las estadísticas.
    def abrirEstadisticas():
        est.solicitanteEst(listaSolicitante) #Se abre la función que muestra las donaciones recibidas por mes.
    
    #Función realizada al presionar el botón de actualizar info.
    def abrirActualizar():
        raiz.destroy()
        import Actualizar
        Actualizar.solicitanteActualizar(listaSolicitante) #Se abre la función de actualizar la información de solicitantes.
        #Se utiliza el parámetro de la listaSolicitante que había enviado el login, para que los datos ya esten puestos a la hora de actualizarlos.
    
    #Función realiada al presionar el botón de cerrar sesión.
    def abrirLogin():
        raiz.destroy()
        import Login
        Login.solicitanteLogin() #Se regresa, abriendo la función de login de solicitantes.

    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    textoBienvenido = Label(frame1, text="Donaciones recibidas", width=20, height=2, anchor="center")
    textoBienvenido.config(bg="white", fg="midnightblue", font=("Calibri", 25))
    textoBienvenido.grid(row=0, column=0, padx=20, pady=30, sticky="w") 

    logo = PhotoImage(file="Logo.png")
    logo2 = Label(frame1, image=logo)
    logo2.grid(row=0, column=1, padx=20, pady=30, sticky="e") #Primer frame con el mensaje Donaciones recibidas y el logo.

    frame2 = Frame(raiz, bg="cornflowerblue")
    frame2.pack()

    totalRecibido = est.totalRecibido(listaSolicitante)
    textoTotal = Label(frame2, text=("Total Recibido:  " + totalRecibido), bg="cornflowerblue", fg="white", font=("Calibri", 14))
    textoTotal.grid(row=0, column=0, padx=30, sticky="w") #Muestra el total recibido.
    
    botonEstadisticas = Button(frame2, text="Mostrar Estadísticas", width=16, anchor="center", command=abrirEstadisticas) #Botón para abrir estadísticas.
    botonEstadisticas.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 14))
    botonEstadisticas.grid(row=0, column=1, padx=30, sticky="w")

    frame3 = Frame(raiz, bg="cornflowerblue")
    frame3.pack()

    #Se crea un canvas, donde irían todas las donaciones recibidas.
    canvas = Canvas(frame3, highlightthickness=0, bg="cornflowerblue", width=650, height=420, cursor="hand2")
    canvas.grid(row=0, column=0, padx=10, pady=35, sticky="w")
    sb = Scrollbar(frame3, orient="vertical", command=canvas.yview)
    sb.grid(row=0, column=1, padx=15, pady=35, sticky="ns")
    canvas.config(yscrollcommand=sb.set)
    
    LDR = []
    with open("DonacionesRealizadas.csv", "r") as archivoDR:
        leer2 = csv.reader(archivoDR, delimiter=',')
        for filas2 in leer2:
            LDR.append(filas2)
        archivoDR.close() #Se crea una lista con todas las cuentas de los solicitantes
    
    LDR2 = []
    for i in range(len(LDR)):
        if LDR[i][1] == listaSolicitante[6]:
            LDR2.append(LDR[i])

    for i in range(len(LDR2)): 
        
        montoDR = str(LDR2[i][4])
        totalRecibido = df.transformarMonto(montoDR)
        
        mov = i*90 #Movimiento vertical entre registros.
        
        #Rectangulo e información de la donación recibida.
        botonS = canvas.create_rectangle(5, 5+mov, 610, 60+mov, fill="skyblue", outline="white", width=0)
        botonS2 = canvas.create_rectangle(15, 14+mov, 617, 69+mov, fill="#1190CB", outline="white", width=3)
        ctFecha = canvas.create_text(410, 43+mov, text=("FECHA:"), anchor="w", fill="#d6e8fc", font=("Calibri", 12))

        ctMonto2 = canvas.create_text(50, 42+mov, text=("Te han donado " + totalRecibido), anchor="w", fill="white", font=("Calibri", 14))
        ctFecha2 = canvas.create_text(480, 42+mov, text=LDR2[i][5], anchor="w", fill="white", font=("Calibri", 14))
        
        canvas.config(scrollregion=canvas.bbox("all"))

    frame4 = Frame(raiz, bg="cornflowerblue")
    frame4.pack()

    botonActualizar = Button(frame4, text="Actualizar info.", width=13, anchor="center", command=abrirActualizar) #Botón de actualizar info, que realiza la función abrirActualizar.
    botonActualizar.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 18))
    botonActualizar.grid(row=0, column=2, padx=20, pady=10)

    botonCerrar = Button(frame4, text="Cerrar sesión", width=11, anchor="se", command=abrirLogin)
    botonCerrar.config(cursor="hand2", relief="flat", bg="cornflowerblue", fg="white", font=("Calibri", 14,)) #Botón de cerrar sesión, que realiza la función abrirLogin.
    botonCerrar.grid(row=0, column=3, padx=10, pady=10, sticky="e")

    raiz.mainloop()