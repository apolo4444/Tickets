SISTEMA DE GENERACIÓN DE TICKETS
Autores Grupo 2: Matias Lasorsa y Antonella Lasorsa
Instrucciones

main.py --> Aplicación por consola

    Al iniciar el programa, se mostrará un menú con 3 opciones:
    "Generar un nuevo ticket", "Leer un ticket" y "Salir".

    "Generar un nuevo ticket" -->
    El sistema solicitará al usuario que ingrese su nombre, el sector al que pertenece, el asunto y una descripción del problema. Una vez completados los datos, se generará automáticamente un número de ticket aleatorio y toda la información quedará almacenada en el archivo INFO_TICKETS.json. Finalmente, se mostrará por pantalla el ticket generado y se consultará al usuario si desea crear otro ticket.

    "Leer un ticket" -->
    El sistema solicitará el número de ticket. Si el número ingresado es válido, buscará la información correspondiente dentro del archivo INFO_TICKETS.json y mostrará todos los datos del ticket encontrado. Luego preguntará al usuario si desea realizar otra búsqueda.

    "Salir" -->
    Finaliza la ejecución del programa.

    En todo momento se valida que el usuario ingrese los datos solicitados en el formato correcto, evitando errores por ingresos inválidos.

main(UI).py --> Aplicación con interfaz gráfica (Tkinter)

    Al iniciar el programa, se abrirá una ventana titulada "Generador de Tickets" con un menú principal compuesto por tres botones:
    "Generar un nuevo ticket", "Leer un ticket" y "Salir".

    "Generar un nuevo ticket" -->
    Se mostrará un formulario donde el usuario deberá ingresar Nombre, Sector, Asunto y Mensaje. Al presionar el botón "Aceptar", el sistema generará automáticamente un número de ticket, almacenará la información en el archivo INFO_TICKETS.json y mostrará el ticket creado dentro de la misma ventana. Luego se ofrecerá la posibilidad de generar un nuevo ticket.

    "Leer un ticket" -->
    Se solicitará el número de ticket mediante un campo de texto. Si el número existe en el archivo INFO_TICKETS.json, se mostrarán todos los datos correspondientes. En caso de ingresar un valor inválido, el campo se resaltará en rojo durante unos segundos para indicar el error antes de permitir un nuevo ingreso.

    "Salir" -->
    Cierra la aplicación.

    Durante el uso de la interfaz se validan los datos ingresados por el usuario, verificando que los campos obligatorios estén completos y que el número de ticket ingresado sea numérico antes de realizar la búsqueda.