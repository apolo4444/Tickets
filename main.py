import sys, os, random, subprocess

def limpiar_pantalla():
    # Detecta el sistema operativo
    comando = "cls" if os.name == "nt" else "clear" # esto es un ternario, lo veremos el proximo cuatri

    # Ejecuta el comando de forma segura
    subprocess.run([comando], shell=True)


numero_random = random.randrange(1000, 9999) #con esto crean un numero random
 
os.path.isfile(ruta) # la palabra ruta obtendra el nombre del archivo y verificara que exista

sys.exit() #con este comando cierra la ejecucion del programa