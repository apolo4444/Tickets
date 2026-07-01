from random import randrange,choice
import sys, os, subprocess, time
opcion:int=0
figuras=["X", "O"]
turno_jugador=1
ganador=False
tablero_lleno=False
tateti=[" "," "," "," "," "," "," "," "," "]
JuegaPC=False
#este tateti es para jugar contra la maquina

# randrange(lista) le podemos pasar una lista de valores para que asigne uno al azar
def limpiar_pantalla():
    # Detecta el sistema operativo
    comando = "cls" if os.name == "nt" else "clear" # esto es un ternario, lo veremos el proximo cuatri

    # Ejecuta el comando de forma segura
    subprocess.run([comando], shell=True)

def salir():
    sys.exit()


def validar():
    global ganador, tablero_lleno

    combinaciones = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas
        (0, 4, 8), (2, 4, 6)              # diagonales
    ]

    for a, b, c in combinaciones:
        if tateti[a] != " " and tateti[a] == tateti[b] == tateti[c]:
            ganador = True
            print(f"Ganó jugador {turno_jugador}")
            return

    if " " not in tateti:
        tablero_lleno = True
        print("El tablero está lleno. Nadie ganó. Más suerte la próxima.")

def pintar_tablero():

    global tablero_lleno
    for i in range(9):
        print(f" {tateti[i]} |", end="")
        if i<9 and (i+1)%3==0:
            print("")
    print("")
    validar()
 
            
def dos_jugadores():
    global ganador, turno_jugador, tablero_lleno, JuegaPC

    while not ganador and not tablero_lleno:
        print(f"Turno jugador {turno_jugador}")
         
        if JuegaPC and turno_jugador==2:
            jugada = jugada_pc()
        else: 
            jugada = input(
                "Ingrese un número del 1 al 9 para determinar la posición de la ficha en el tablero: "
            )
            if not jugada.isdigit():
                print("La opción ingresada no es válida.")
                continue
            jugada = int(jugada)

        if jugada < 1 or jugada > 9:
            print("La opción ingresada no es un número del 1 al 9. Vuelva a intentarlo.")
            continue

        if tateti[jugada - 1] != " ":
            print("La opción ingresada corresponde a un espacio ya ocupado. Vuelva a intentarlo.")
            continue

        tateti[jugada - 1] = figuras[turno_jugador - 1]
        pintar_tablero()
        turno_jugador = 2 if turno_jugador == 1 else 1

    time.sleep(5)
    menu()
 
def jugada_pc():
    indices = list(filter(lambda i: tateti[i] == " ", range(len(tateti))))
    return choice(indices)+1

def reset():
    global ganador, tablero_lleno
    ganador=False
    tablero_lleno=False
    for i in range(9):
        tateti[i]=" "
def menu ():
    global JuegaPC
    limpiar_pantalla()
    reset()
    print("     Bienvenido/a al TaTeTi\n\n Seleccione una de las siguientes opciones numeradas a continuación: \n1 - 2 jugadores\n2 - VS. pc \n3 - Salir \n")
    
    while True:
        opcion=input("Selección: ")
        if opcion.isdigit():
            opcion=int(opcion)
            if opcion>=1 and opcion<=3:
                match opcion: 
                    case 1:
                        JuegaPC=False
                        dos_jugadores()
                    case 2:
                        JuegaPC=True
                        dos_jugadores()
                    case 3:
                        salir()
                break
            else:
                 print("El menu solo tiene 3 opciones")
        else:
            print("El opcion ingresada no es un numero del uno al tres, vuelva a interlo.")

menu()


