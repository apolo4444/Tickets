JUEGO DE TA-TE-TI Instrucciones 

Autores Grupo 2: Matias Lasorsa y Antonella Lasorsa

main.py--> Juego por consola 
    Al iniciar el juego, saldra un menu con 3 opciones: "2 jugadores" , "VS PC" y "Salir".

    "2 jugadores"--> Se le indicara a cada jugador que ingrese un numero del 1 al 9 en sus respectivos turnos para ir completando el tablero con su respectivo simbolo. El jugador 1 siempre es "X" y el 2 es "O". La accion se repite hasta que haya un ganador o el tablero quede completamente lleno. Mostrando por pantalla el resultado de la partida. Luego preguntando si desea o no volver a jugar. 

    "VS PC"-->  Se le indicara al jugador que ingrese un numero del 1 al 9 para ingresar su simbolo en la casilla correspondiente del tablero. Despues debera esperar a que el ordenador haga su jugada y asi repetir el ciclo hasta que haya un ganado o el tablero quede completamente lleno. Mostrando por pantalla el resultado de la partida. Luego preguntando si desea o no volver a jugar.

    "Salir"--> Finaliza la ejecucion del programa. 

    En todo momento se validara que el usuario ingrese los datos correspondientes segun lo pedido.

main(UI).py--> Ventana Grafica con Tkinter 
    Al iniciar el juego, se abrira una ventana, con un titulo y  un menu con 3 botones: "2 jugadores" , "VS PC" y "Salir" los cuales representan las opciones del programa.

    "2 jugadores"--> En la pantalla se mostrara un tablero de 3x3 Botones, los cuales cada jugador debe oprimir para ir completando el tablero con su respectivo simbolo. El jugador 1 siempre es "X" y el 2 es "O". La accion se repite hasta que haya un ganador o el tablero quede completamente lleno. Mostrando el resultado por etiqueta debajo del mismo y preguntando al jugador si desea o no volver a jugar. 

    "VS PC"-->  En la pantalla se mostrara un tablero de 3x3 Botones, en el cual el jugador 1 debe oprimir para ir completando el tablero con su respectivo simbolo. Despues debera esperar a que el ordenador haga su jugada y asi repetir el ciclo hasta que haya un ganado o el tablero quede completamente lleno. Mostrando el resultado por etiqueta debajo del mismo y preguntando al jugador si desea o no volver a jugar.

    "Salir"--> Cierra la ventana del juego.

    En todo momento se validara que el usuario ingrese los datos correspondientes segun lo pedido. 