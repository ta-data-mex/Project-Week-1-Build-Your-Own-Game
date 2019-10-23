<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Proyecto Sudoku
*Nohely y Diego*

*Campus Mexico City*

## Content
- En este proyecto decidimos programar un sudoku, el cual cuenta con 3 niveles de dificultad.

- A continuación te dejamos unos links con las reglas del juego :D 
	http://www.sudoku.name/rules/es

<a name="project-description"></a>

## Project Description
El proyecto tiene como objetivo lograr validar la solución del jugador a un Sudoku, 
por lo que tiene cargados 5 sudokus diferentes por nivel, una vez que el jugador haya completado las casillas
se le indicará si perdió o ganó el juego.

La validación de su respuesta se realiza validando las reglas del juego: No deben existir números repetidos por fila, columna o celda
y los números a utilizar deben de ir del 1 al 9.

<a name="workflow"></a>

## Workflow
- 1.- Se pensó en el menú que el jugador debería de ver y las opciones que debería de tener durante el juego, esto sirvió
para hacer un borrador de la estructura del menú y las funciones que se iban a necesitar para lograr el objetivo.
- 2.- Se hicieron las funciones:
		- Visualizar Tabla
		- Obtener las celdas modificables
		- Ingresar o Eliminar datos a celdas modificables
		- Comprobar el llenado de la tabla
		- Comprobar que el sudoku sea correcto una vez completo (por filas, columnas y celdas)
- 3.- Se generó el archivo Main.py que utiliza las funciones del archivo Funciones.py para realizar el juego.

<a name="organization"></a>
