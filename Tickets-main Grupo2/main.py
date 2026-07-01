import sys, os, random, subprocess, json
opcion:int=0
ticket={}

def limpiar_pantalla():
    # Detecta el sistema operativo
    comando = "cls" if os.name == "nt" else "clear" # esto es un ternario, lo veremos el proximo cuatri

    # Ejecuta el comando de forma segura
    subprocess.run([comando], shell=True)

def alta_ticket():
    print("Ingrese los datos para generar un nuevo ticket")
    ticket["nombre"]=input("ingrese su nombre: ")
    ticket["sector"]=input("ingrese el sector al que pertenece: ")   
    ticket["asunto"]=input("ingrese una palabra para describir el asunto: ")
    ticket["mensaje"]=input("ingrese una descripción del problema: ")
    ticket["n_ticket"]=random.randrange(1000, 9999) 
    with open('INFO_TICKETS.json','r',encoding='UTF-8') as f:
        datos = json.load(f)
    with open('INFO_TICKETS.json','w',encoding='UTF-8') as f:
        datos.append(ticket)
        json.dump(datos,f,indent=4)
    print("="*10)
    print(" Se genero el siguiente ticket")
    print("="*10)
    for key, value in ticket.items():
        print(f" {key}: {value}")
    print("Estimado cliente por favor, recuerde su numero de ticket")
    resp=input("¿desea crear un nuevo ticket? S/N:").lower().strip()
    if resp=="s":
        alta_ticket()
    else:
        menu()
def leer_ticket():
    while True:
        codigo=input("ingrese su numero de tiket para buscarlo: ") 
        if codigo.isdigit():
            codigo=int(codigo)
            break
        else:
            print("El opcion ingresada no es un numero del uno al tres, vuelva a interlo.")       
    with open('INFO_TICKETS.json','r',encoding='UTF-8') as f:
        datos = json.load(f)
    for i in datos: 
        if i["n_ticket"]==codigo:
            for key, value in i.items():
                print(f" {key}: {value}")
        else:
            print("ticket no encontrado")
    resp=input("¿desea ibuscar otro ticket? S/N:").lower().strip()
    if resp=="s":
       leer_ticket()
    else:
        menu()       

def salir():
    sys.exit()

def menu ():
    limpiar_pantalla()
    print("     Bienvenido/a al sistema de tickets\n\n Seleccione una de las siguientes opciones numeradas a continuación: \n1 - Generar un nuevo ticket\n2 - Leer un ticket \n3 - Salir \n")
    
    while True:
        opcion=input("Selección: ")
        if opcion.isdigit():
            opcion=int(opcion)
            if opcion>=1 and opcion<=3:
                match opcion: 
                    case 1:
                        alta_ticket()
                    case 2:
                        leer_ticket()
                    case 3:
                        salir()
                break
            else:
                 print("El menu solo tiene 3 opciones")
        else:
            print("El opcion ingresada no es un numero del uno al tres, vuelva a interlo.")

menu()