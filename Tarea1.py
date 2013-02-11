#Pedir megapixeles
#Pedir dimensiones

#******Los pasos son: 
#
#1 - Escala de grises
#2 - Filtro (de los vecinos)
#3 - Convolucion
#4 - Normalizacion (por diferencia)
#5 - Binarizacion

#Obtener resoluciones
#Umbrales
import pygame
from pygame.locals import*
from PIL import Image
from math import *
import sys
import numpy
import time

def main():  	
	
	acumulado1 = 0
	acumulado2 = 0
	acumulado3 = 0
	acumulado4 = 0
	#eleccion = 0	

	#pygame.init()
	#screen = pygame.display.set_mode((800, 680))
	#pygame.display.set_caption("Bla")

	#fondo = pygame.image.load("bla.jpg").convert()
	#Posicion
	#screen.blit(fondo, (0, 0))
	#pygame.display.flip()
		#eleccion = int(raw_input('Ingresa 1 para escala de grises y 2 para umbrales: '))

	#Para las 30 ejecuciones de la escala de grises		
	for i in range(30):
		tInicial1 = time.time()		
		transformar()
		tFinal1 = time.time()
		transcurrido1 = tFinal1 - tInicial1
		acumulado1 = acumulado1 + transcurrido1	
	print "El promedio de tiempo transcurrido para la escala de grises(en 30 repeticiones de ejecucion) es = ", acumulado1/30, "segundos"
	
	#Para las 30 ejecuciones de la filtracion
	i = 0	
	for i in range(30):	
		tInicial2 = time.time()
		filtrada()	
		tFinal2 = time.time()
		transcurrido2 = tFinal2 - tInicial2
		acumulado2 = acumulado2 + transcurrido2
	print "\nEl promedio de tiempo transcurrido para la filtracion(en 30 repeticiones de ejecucion) es = ", acumulado2/30, "segundos"
	#diferencia()

	#Para las 30 ejecuciones de la convolucion
	i = 0	
	for i in range(30):
		tInicial3 = time.time()
		convolucion()
		tFinal3 = time.time()
		transcurrido3 = tFinal3 - tInicial3
		acumulado3 = acumulado3 + transcurrido3
	print "\nEl promedio de tiempo transcurrido para la convolucion(en 30 repeticiones de ejecucion) es = ", acumulado3/30, "segundos"
	
	#Para las 30 ejecuciones de la binarizacion	
	i = 0
	for i in range(30):
		tInicial4 = time.time()
		umbrales()
		tFinal4 = time.time()
		transcurrido4 = tFinal4 - tInicial4
		acumulado4 = acumulado4 + transcurrido4
	print "\nEl promedio de tiempo transcurrido para la binarizacion(en 30 repeticiones de ejecucion) es = ", acumulado4/30, "segundos\n"
	#while True:
	#	for event in pygame.event.get():
	#		if event.type == pygame.QUIT:
	#			sys.exit()

#Funcion para escala de grises
#Se accede a ella presionando 1
def transformar():
	#tiempoInicial = time.time()
	i = 0
	x = 0
	y = 0
	im = Image.open("bla.jpg")
 
	for x in xrange(im.size[0]):
		for y in xrange(im.size[1]):
			pix = im.load()
			tupla = pix[x, y]
	
			a = tupla[0]
			b = tupla[1]
			c = tupla[2]
			
			prom = int((a+b+c)/3)
			newTupla = (prom,prom,prom)
			im.putpixel((x, y), newTupla)			

			#print tupla, "--", a,",",b,",",c
	im.save('meh.jpg')
	#tiempoFinal = time.time()
	#transcurso = tiempoFinal - tiempoInicial
	#print "Tiempo de escala de grises = ", transcurso 

def filtrada(): #Filtrada por el metodo de los vecinos
	#tiempoInicial = time.time()
	i = 0
	x = 0
	y = 0
	im = Image.open("meh.jpg")
	width, height = im.size
	pix = im.load() 
	promedio = 0
	width = width-1
	height = height-1

	#x = j y y = i
	for x in range(height):
		for y in range(width):
			#esquina superior izquierda
			if y == 0 and x == 0:
				promedio = (sum(pix[y + 1,x])/3 + sum(pix[y,x + 1])/3 + sum(pix[y,x])/3)/3
			#esquina superior derecha
			if y == width and x == 0:
				promedio = (sum(pix[y,x+1])/3 + sum(pix[y-1,x])/3 + sum(pix[y,x])/3)/3

			if y == 0 and x == height:
				 promedio = (sum(pix[y,x-1])/3 + sum(pix[y+1,x])/3 + sum(pix[y,x])/3)/3

			if y == height and x == width:
				 promedio = (sum(pix[y - 1,x])/3 + sum(pix[y,x - 1])/3 + sum(pix[y,x])/3)/3

			if y > 0 and y < width and x == 0:
				promedio = (sum(pix[y+1,x])/3 + sum(pix[y-1,x])/3 +sum(pix[y,x+1])/3+ sum(pix[y,x])/3)/4
		
			if y > 0 and y < width and x == height:
				promedio = (sum(pix[y -1,x])/3 + sum(pix[y,x-1])/3 +sum(pix[y+1,x])/3+ sum(pix[y,x])/3)/4

			if x >0 and x <height and y == 0:
				promedio = (sum(pix[y+1,x])/3 + sum(pix[y,x-1])/3 +sum(pix[y,x +1])/3+ sum(pix[y,x])/3)/4

			if y == width and x >0 and x < height:
				promedio = (sum(pix[y - 1,x])/3 + sum(pix[y,x-1])/3 + sum(pix[y,x +1])/3+ sum(pix[y,x])/3)/4

			if y > 0 and y< width and x>0 and x< height:
				promedio = (sum(pix[y,x])/3 + sum(pix[y + 1,x])/3 + sum(pix[y - 1,x])/3 + sum(pix[y,x + 1])/3 + sum(pix[y,x -1])/3)/5	
 


			#-----------------------------
			#tupla = pix[x, y]
			
			a = promedio
			b = promedio
			c = promedio	
			'''
			a = tupla[0]
			b = tupla[1]
			c = tupla[2]
			'''
			#prom = int((a+b+c)/3)
			pix[y, x] = (a,b,c)
			#tup = pix[]
			#im.putpixel((y, y), pix)			

			#print tupla, "--", a,",",b,",",c
	im.save('meh2.jpg')
	#tiempoFinal = time.time()
	#transcurso = tiempoFinal - tiempoInicial
	#print "Tiempo transcurrido durante la filtracion = ", transcurso


def diferencia(): #O normalizacion
	#tiempoInicial = time.time()
	imagen1 = Image.open("meh.jpg")
	imagen2 = Image.open("meh2.jpg")
	width, height = imagen1.size
	pix = imagen1.load()
	pix2 = imagen2.load()

	for y in range(width):
		for x in range(height):
			(a,b,c) = pix[y, x]
			(d,e,f) = pix2[y, x]
			promedio = a+b+c/3
			promedio1 = d+e+f/3
			promedio2 = promedio - promedio1

			if promedio2 > 115:
				promedio2 = 255
			else:
				promedio2 = 0
			a = promedio2
			b = promedio2
			c = promedio2	 
			pix[y, x] = (a,b,c)
	imagen1.save("meh3.jpg")
	#tiempoFinal = time.time()
	#transcurso = tiempoFinal - tiempoInicial
	#print "Tiempo transcurrido durante la normalizacion = ", transcurrido

def convolucion():
	#tiempoInicial = time.time()
	'''         ---       ---                     ---    ---
		    | -1  0  1  |		     | 1  2  1  |
	SOBEL: Sx = | -2  0  2  |		Sy = | 0  0  0  |
  		    | -1  0  1  |		     |-1 -2 -1  |
 		    ---       ---                     ---    ---

	S = raiz(Sx2+Sy2)

	'''	
	
	im = Image.open("meh2.jpg")
	width, height = im.size
	pix = im.load()
	resultado = 0
	gradienteX = ([-1, 0, 1], [-2, 0, 2], [-1, 0, 1])  #Valores establecidos por medio del operador Sobel
	gradienteY = ([1, 2, 1], [0, 0, 0], [-1, -2, -1])  #Para gradiente de y, el de arriba es el gradiente de x.
	sumasX = 0
	sumasY = 0 	

	for x in range(height):
		for y in range(width):
			sumasX = 0
			sumasY = 0
			if x != 0 and y != 0 and y != width and x != height: #Para obtener un centrado de la mascara, evita la primera linea de pixeles de la imagen por los 4 lados
				#x = a
				#y = b			
				for a in range(3): #Debido a que la matriz de los gradientes es de 3x3
					for b in range(3):
						try:
							productosGX = gradienteX[a][b]*pix[y+b, x+a][1] #Obteniendo el valor de gradiente X
							productosGY = gradienteY[a][b]*pix[y+b, x+a][1]	#Obteniendo el valor de gradiente Y
			
						except:
							productosGX = 0
							productosGY = 0
					
						sumasX = productosGX+sumasX #Adicionando los valores del gradiente X
						sumasY = productosGY+sumasY #Adicionando los valores del gradiente Y
			
				potenciaGradienteX = pow(sumasX, 2) #Obteniendo el cuadrado del gradiente X
				potenciaGradienteY = pow(sumasY, 2) #Obteniendo el cuadrado del gradiente Y
				Gradiente = int(sqrt(potenciaGradienteX+potenciaGradienteY)) #Para obtener el gradiente por medio de los componentes x, y
				#resultado = Gradiente

				if Gradiente > 255: #Por si se pasan los valores
					Gradiente = 255

				if Gradiente < 0: #Para estar dentro del rango (0, 255) 
					Gradiente = 0
		
				pix[y,x] = (Gradiente, Gradiente, Gradiente) # Creando el pixel nuevo con el gradiente obtenido			
	
	im.save('meh4.jpg')					
	#tiempoFinal = time.time()	
	#transcurrido = tiempoFinal - tiempoInicial
	#print "Tiempo transcurrido durante la convolucion = ", transcurrido
	
#Funcion umbrales
#Se accede a ella presionando 2
def umbrales():
	#tiempoInicial = time.time()
	i = 0
	x = 0  
	y = 0
	umbInferior = 77
	umbSuperior = 177
	im = Image.open("meh4.jpg")
 
	for x in xrange(im.size[0]):
		for y in xrange(im.size[1]):
			pix = im.load()
			tupla = pix[x, y]
	
			a = tupla[0]
			b = tupla[1]
			c = tupla[2]
			
			prom = int((a+b+c)/3)
			if prom < umbInferior:
				prom = 0
			elif prom >= umbSuperior:
				prom = 255
			newTupla = (prom,prom,prom)
			im.putpixel((x, y), newTupla)			

			#print tupla, "--", a,",",b,",",c
	im.save('meh5.jpg')
	#tiempoFinal = time.time()
	#transcurrido = tiempoFinal - tiempoInicial
	#print "Tiempo transcurrido durante la binarizacion = ", transcurrido

if __name__ == "__main__":
	main()




