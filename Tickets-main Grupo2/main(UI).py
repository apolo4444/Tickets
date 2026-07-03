import sys, os, random, subprocess, json, time
from tkinter import Tk,Entry,Button,StringVar,Label,Text
opcion:int=0
ticket={}
ventana=Tk()
mensaje=StringVar(value="Valor inicial")
color_fondo="#000000"
fomulario=[]
entradas=[]

def configuracion_ventana(ventana):
    #global ventana
    ventana.configure(bg="#0000EF")
    ventana.title("Generador de Tickets")
    ventana.geometry("550x650")
    ventana.resizable(False,False)

    for i in range(10):
        ventana.grid_columnconfigure(i, weight=1)
   


def limpiar_pantalla():
    # Detecta el sistema operativo
    comando = "cls" if os.name == "nt" else "clear" # esto es un ternario, lo veremos el proximo cuatri

    # Ejecuta el comando de forma segura
    subprocess.run([comando], shell=True)

def alta_ticket():
    global formulario
    global entradas
    global ventana
    #Borrar la pantalla
    for widget in ventana.winfo_children():
        widget.destroy()
    #Configuracion Inicial
    configuracion_ventana(ventana)

    mensaje.set("Ingrese los datos para generar un nuevo ticket")

    datos=Entry( ventana, bg="#000000", fg="#2AEB31", justify="right", font=("Consolas",15), bd=0, state="readonly", textvariable=mensaje, insertbackground="white", readonlybackground="#1E1E24",disabledforeground="#1E1E24")
    datos.grid(row=0,column=0, columnspan=10,ipady=15,padx=15,pady=15, sticky="we")

    formulario=["Nombre","Sector","Asunto","Mensaje"]
    entradas=[]

    for col_id,elemento in enumerate(formulario):
        label=Label(
            ventana,
            text=elemento
        )

        renglones=0

        if elemento=="Mensaje":
            renglones=3
        else:
            renglones=1

        label.grid(row=col_id+1,column=0, columnspan=3,ipady=3,padx=3,pady=3, sticky="we")

        text_box=Entry( ventana, bg="#000000", fg="#2AEB31", justify="right", font=("Consolas",10), bd=0, state="normal", insertbackground="white", readonlybackground="#1E1E24",disabledforeground="#1E1E24")
        text_box.grid(row=col_id+1,column=4, columnspan=5,rowspan=renglones, ipady=10,padx=15,pady=15, sticky="we")

        entradas.append(text_box)
        print(entradas)
    botones=["Aceptar", "volver al menu"]
    for col_id, boton in enumerate(botones):
        if boton=="Aceptar":
            accion=guardar_ticket
        else:
            accion=menu

        boton=Button( ventana, text=boton, font=("Arial",14,"bold"), bd=0, relief="flat", activebackground="#2AEB31", activeforeground="#1E1E24", command=accion)
        boton.grid(row=7,column=(col_id*3)+2,padx=3, pady=3,sticky="nsew", columnspan=3)



def guardar_ticket():
    global formulario
    global entradas
    global mensaje


    for i in range(len(entradas)):
        if entradas[i].get()=="":
            return
        ticket[formulario[i]]=entradas[i].get()
        entradas[i].delete(0, "end")
        
    ticket["n_ticket"]=random.randrange(1000, 9999)

    with open('Tickets-main Grupo2\INFO_TICKETS.json','r',encoding='UTF-8') as f:
        datos = json.load(f)
        
    with open('Tickets-main Grupo2\INFO_TICKETS.json','w',encoding='UTF-8') as f:
        datos.append(ticket)
        json.dump(datos,f,indent=4)

    mostrar_ticket_creado() 

    print(mensaje.get())


    btn=Button( ventana, text="Nuevo Ticket", font=("Arial",12,"bold"), bd=0, relief="flat",activebackground="#2AEB31", activeforeground="#1E1E24", command=alta_ticket)
    btn.grid(row=21,column=3 ,padx=7, pady=7,sticky="nsew", columnspan=3)

    pass    

def mostrar_ticket_creado():
    global mensaje
    nuevo_mensaje="="*10
    nuevo_mensaje=nuevo_mensaje+str(" Se genero el siguiente ticket")
    nuevo_mensaje=nuevo_mensaje+str("="*10)
    nuevo_mensaje=nuevo_mensaje+"\n"
    for key, value in ticket.items():
        nuevo_mensaje=nuevo_mensaje+f" {key}: {value}\n"
    nuevo_mensaje=nuevo_mensaje+("Estimado cliente por favor, recuerde su numero de ticket")
    #mensaje.set(nuevo_mensaje)
    
    text_box=Label( ventana, font=("Arial",10,"bold"), text=nuevo_mensaje, width="1000", height="10")           
    text_box.grid(row=11,column=0, columnspan=10, ipady=10,padx=15,pady=15, sticky="we")




def Buscar_ticket():
    global mensaje
    global entradas
    global color_fondo

    codigo = entradas[0].get()
    print(codigo)

    if not codigo.isdigit():
        color_fondo = "#FF0505"
        entradas[0].config(bg=color_fondo)
        ventana.after(2000, restaurar)
        return

    with open("Tickets-main Grupo2\\INFO_TICKETS.json", "r", encoding="UTF-8") as f:
        datos = json.load(f)

    nuevo_mensaje = "Ticket no encontrado\n"

    for ticket in datos:
        if ticket["n_ticket"] != int(codigo):
            continue

        nuevo_mensaje = "=" * 10
        nuevo_mensaje += " Encontramos el siguiente ticket "
        nuevo_mensaje += "=" * 10 + "\n"

        for key, value in ticket.items():
            nuevo_mensaje += f"{key}: {value}\n"

        break

    nuevo_mensaje += "Estimado cliente, esperamos que esté conforme con el servicio."

    text_box = Label( ventana, font=("Arial", 10, "bold"), text=nuevo_mensaje, width=1000, height=10
    )         
    text_box.grid(row=11,column=0, columnspan=10, ipady=10,padx=15,pady=15, sticky="we")

def restaurar():
    entradas[0].config(bg="#0E0C0C")
    entradas[0].delete(0, "end")

def leer_ticket():
    global formulario
    global entradas
    global ventana
    global color_fondo
    #Borrar la pantalla
    for widget in ventana.winfo_children():
        widget.destroy()
    #Configuracion Inicial
    configuracion_ventana(ventana)

    mensaje.set("Ingrese su numero de ticket para buscarlo")

    datos=Entry( ventana, bg="#000000", fg="#2AEB31", justify="right", font=("Consolas",15), bd=0, state="readonly", textvariable=mensaje, insertbackground="white", readonlybackground="#1E1E24",disabledforeground="#1E1E24")
    datos.grid(row=0,column=0, columnspan=10,ipady=15,padx=15,pady=15, sticky="we")

    entradas=[]

    label=Label(
        ventana,
        text="Numero de Ticket"
    )
    label.grid(row=1,column=0, columnspan=3,ipady=3,padx=3,pady=3, sticky="we")
    
    text_box=Entry(ventana, bg=color_fondo, fg="#2AEB31", justify="right", font=("Consolas",10), bd=0,state="normal", insertbackground="white", readonlybackground=color_fondo,disabledforeground=color_fondo)
    text_box.grid(row=1,column=4, columnspan=5,rowspan=1, ipady=10,padx=15,pady=15, sticky="we")
    entradas.append(text_box)

    botones=["Aceptar", "volver al menu"]
    for col_id, boton in enumerate(botones):
        if boton=="Aceptar":
            accion=Buscar_ticket
        else:
            accion=menu
        boton=Button( ventana, text=boton, font=("Arial",14,"bold"), bd=0, relief="flat",activebackground="#2AEB31", activeforeground="#1E1E24", command=accion)
        boton.grid(row=7,column=(col_id*3)+2,padx=3, pady=3,sticky="nsew", columnspan=3)     

def salir():
    sys.exit()

def menu ():

    for widget in ventana.winfo_children():
        widget.destroy()
    #Configuracion Inicial
    configuracion_ventana(ventana)
    
    mensaje.set("Bienvenido/a al sistema de tickets")
    datos=Entry(ventana, bg="#000000", fg="#2AEB31", justify="right", font=("Consolas",20),bd=0,state="readonly", textvariable=mensaje, insertbackground="white",  readonlybackground="#1E1E24", disabledforeground="#1E1E24")
    datos.grid(row=0,column=0, columnspan=10,ipady=15,padx=15,pady=15, sticky="we")

   
    botones_layout=[ "Generar un nuevo ticket", "Leer un ticket","Salir"]

    for col_id, boton in enumerate(botones_layout):
        accion=salir
        ancho_columnas=5
        color_texto="#000000"
        color_fondo="#FFFFFF"

        if boton=="Generar un nuevo ticket":
            accion=alta_ticket
        elif boton=="Leer un ticket":
            accion=leer_ticket

        btn=Button(ventana,text=boton,font=("Arial",14,"bold"),bd=0,relief="flat",activebackground="#2AEB31",activeforeground="#1E1E24",command=accion)
        btn.grid(row=col_id+1,column=2,padx=3, pady=3,sticky="nsew", columnspan=ancho_columnas)

configuracion_ventana(ventana)
menu()
ventana.mainloop()