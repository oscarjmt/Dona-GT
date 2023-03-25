"""
Cristóbal Serra 20160
Isaac Cyrman 20552
Oscar Méndez 20402
Proyecto - Protoptipo
Dona GT - Ayuda a comabatir la desnutrición en Guatemala
"""

from tkinter import * #Se importa tkinter
import sys

#Función para escoger si s donador o solicitante.
def escogerAccion():   
    raiz= Tk()
    raiz.title("Escoger Acción")
    raiz.iconbitmap("Logo.ico")
    raiz.geometry("800x450")
    raiz.config(bg="cornflowerblue") #Propiedades de la ventana gráfica.
    
    #Función realizada al presionar el botón de donador.
    def abrirDonador():
        raiz.destroy()
        import Login
        Login.donadorLogin() #Se abre la función de login de donador.
    
    #Función realizada al presionar el botón de solicitante.
    def abrirSolicitante():
        raiz.destroy()
        import Login
        Login.solicitanteLogin() #Se abre la función de login de solicitante.

    frame1 = Frame(raiz, bg="cornflowerblue")
    frame1.pack()

    logo = PhotoImage(file="Logo.png")
    logo2 = Label(frame1, image=logo)
    logo2.grid(row=0, column=0, pady=20) #Primer frame donde está el logo.

    frame2 = Frame(raiz, bg="cornflowerblue")
    frame2.pack()

    botonDonador = Button(frame2, text="Donador", height=2, width=14, anchor="center", command=abrirDonador) #Botón de donador, que realiza la función abrirDonador.
    botonDonador.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 24))
    botonDonador.grid(row=1, column=0, padx=30, pady=60)

    botonSolicitante = Button(frame2, text="Solicitante", height=2, width=14, anchor="center", command=abrirSolicitante) #Botón de solicitante, que realiza la función de abrirSolicitante.
    botonSolicitante.config(cursor="hand2", bg="white", fg="midnightblue", font=("Calibri", 24))
    botonSolicitante.grid(row=1, column=1, padx=30, pady=60)

    raiz.mainloop()

escogerAccion() #Se ejecuta para empezar el programa.
sys.exit()