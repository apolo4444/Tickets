#Autores: Matias Lasorsa y Antonella Lasorsa
from random import randrange,choice
from tkinter import Tk,Entry,Button,StringVar,Label,Text
import sys, os, subprocess, time
opcion:int=0
figuras=["X", "O"]
turno_jugador=1
ganador=False
tablero_lleno=False
tateti=[" "," "," "," "," "," "," "," "," "]
JuegaPC=False
#Parte grafica

ventana=Tk()
mensaje=StringVar(value="Valor inicial")
botones=[]
resultado=""


def limpiar_pantalla():
   
    for widget in ventana.winfo_children():
        widget.destroy()

    configuracion_ventana(ventana)

def configuracion_ventana(ventana):
    #global ventana
    ventana.configure(bg="#4CA744")
    ventana.title("Generador de Tickets")
    ventana.geometry("550x650")
    ventana.resizable(False,False)

    for i in range(10):
        ventana.grid_columnconfigure(i, weight=1)


def salir():
    sys.exit()


def validar():
    global ganador, tablero_lleno, turno_jugador, resultado

    combinaciones = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas
        (0, 4, 8), (2, 4, 6)              # diagonales
    ]

    for a, b, c in combinaciones:
        if tateti[a] != " " and tateti[a] == tateti[b] == tateti[c]:
            ganador = True
            resultado=f"Ganó jugador {turno_jugador}"


    if " " not in tateti and not ganador:
        tablero_lleno = True
        resultado="El tablero está lleno. Nadie ganó. Más suerte la próxima."
    
    print(ganador)
    print(tablero_lleno)

    if ganador or tablero_lleno:
        mostrar_resultado();
        return
    
    if turno_jugador==1:
        turno_jugador=2
    else:
        turno_jugador=1
    
    

def pintar_tablero():

    global tablero_lleno, botones
    numero_boton=-1
    botones=[]

    for i in range(3):
        for j in range(3):
            accion=llenar_tablero
            numero_boton+=1
            accion=lambda t=int(numero_boton):llenar_tablero(t)


            boton=Button( ventana, text=" ", font=("Arial",14,"bold"), bd=0, relief="flat", activebackground="#2AEB31", activeforeground="#1E1E24", command=accion, name=str(numero_boton))
            boton.grid(row=(i*2)+5,column=(j*2)+2,padx=10, pady=10,sticky="nsew", columnspan=2)
            botones.append(boton)

   
 
def llenar_tablero(numero:int=0):

    global botones,ganador,tablero_lleno
    
    if not ganador and not tablero_lleno:
        if tateti[numero]==" ":
            if turno_jugador==1:
                tateti[numero]=figuras[turno_jugador - 1]
                
            else:
                tateti[numero]=figuras[turno_jugador - 1]
            botones[numero].config(text=figuras[turno_jugador - 1])
            validar()

            if JuegaPC and turno_jugador==2:
                #ventana.after(2000)
                jugada = jugada_pc()
    


def mostrar_resultado():
    global resultado
    resultado+=("\n Si desea volver a jugar vuelva a seleccionar las opciones de arriba")
    label=Label(ventana, text=resultado)
    label.grid(row=12,column=1, columnspan=10,ipady=15,padx=15,pady=15, sticky="we")
    

def dos_jugadores(jugador):
    global ganador, turno_jugador, tablero_lleno, JuegaPC
    reset()
    pintar_tablero()

    #while not ganador and not tablero_lleno:
    if jugador=="2 Jugadores":
        JuegaPC=False
    else: 
        JuegaPC=True
         
def jugada_pc():
    indices = list(filter(lambda i: tateti[i] == " ", range(len(tateti))))
    ventana.after(1000)
    llenar_tablero(choice(indices))
    #return choice(indices)+1

def reset():
    global ganador, tablero_lleno,botones, resultado, turno_jugador
    resultado=""
    botones=[]
    ganador=False
    tablero_lleno=False
    JuegaPC=False
    turno_jugador=1
    for i in range(9):
        tateti[i]=" "
    
def menu ():
    global JuegaPC,botones
    
    limpiar_pantalla()
    
    mensaje.set("Bienvenido/a al TA-TE-TI")
    datos=Entry(ventana, bg="#000000", fg="#2AEB31", justify="center", font=("Consolas",20),bd=0,state="readonly", textvariable=mensaje, insertbackground="white",  readonlybackground="#1E1E24", disabledforeground="#1E1E24")
    datos.grid(row=0,column=0, columnspan=10,ipady=15,padx=15,pady=15, sticky="we")

   
    botones_layout=[ "2 Jugadores", "VS PC", "Salir"]

    for col_id, boton in enumerate(botones_layout):
        accion=salir
        nombre_boton=botones_layout[col_id]
        ancho_columnas=5
        color_texto="#000000"
        color_fondo="#FFFFFF"

        if boton=="2 Jugadores" or boton=="VS PC":
            accion=lambda t=nombre_boton:dos_jugadores(t)
       
        btn=Button(ventana,text=boton,font=("Arial",14,"bold"),bd=0,relief="flat",activebackground="#2AEB31",activeforeground="#1E1E24",command=accion)
        btn.grid(row=col_id+1,column=2,padx=3, pady=3,sticky="nsew", columnspan=ancho_columnas)


menu()
ventana.mainloop()


