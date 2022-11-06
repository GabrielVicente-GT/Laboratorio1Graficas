#Gabriel Alejandro Vicente Lorenzo
#SR1 UVG

#Se importan los metodos solicitados por el ejercicios
import gl
from vector import *

gl.glInit()
#Se crea la Ventana (Que renderiza a.bmp)
gl.glCreateWindow(1024,450)

#Cambia el color con el que trabaja Clear
gl.glClearColor(0,0,0)

#Pinta TODOELMAPA de bits de un mismo color
gl.glClear()

#Lab1
#Cambia el color de los trazos para las figuras
gl.glClearColor(1,1,1)

#Traza con blanco las formas de las figuras
gl.TrazosFiguras()

#Llama a la funcion de relleno que segun los puntos dados empieza a
#Colorear dependiendo el color que se llama
gl.Laboratorio1()


# gl.glLine2(V3(700,150),V3(500,500))
gl.glFinish()
