#Obtener resoluciones
#Umbrales
import pygame
from pygame.locals import*
from PIL import Image
from math import *
import sys
import numpy
import time
from Tkinter import *
from PIL import Image, ImageTk
import random
from sys import argv
import Image, ImageTk
import Tkinter
from PIL import Image, ImageDraw,ImageFont

def main():		
	
	acumulado1 = 0
	acumulado2 = 0
	acumulado3 = 0
	acumulado4 = 0

	transformar()
	convolucion()
	umbrales()
	formas()
	

#Funcion para escala de grises
#Se accede a ella presionando 1
def transformar():
	#tiempoInicial = time.time()
	i = 0
	x = 0
	y = 0
	im = Image.open("elipsample.png")
 
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
	
	im = Image.open("meh.jpg")
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
	
	im.save('meh2.jpg')					
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
	im = Image.open("meh2.jpg")
 
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
	im.save('meh3.jpg')
	#tiempoFinal = time.time()
	
#Implelementacion de bfs ***************************************************
#***************************************************************************

def bfs(im, origen, color):
	pix = im.load()
	w, h = im.size
	q = []
	xs = []
	ys = []
	q.append(origen)
	print origen
	original = pix[origen]
	n = 0
	while len(q) > 0:
		(x, y) = q.pop(0)
		actual = pix[x, y]
		if actual == original or actual == color:
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					i, j = (x + dx, y + dy)
					if i >= 0 and i < w and j >= 0 and j < h:
						contenido = pix[i, j]
						if contenido == original:
							pix[i, j] = color
							xs.append(i)
							ys.append(j)
							n += 1
							q.append((i, j))
	im.save("bla01.jpg")
	return n, xs, ys

#**************************************************************************

def formas():

	imagen = Image.open("meh3.jpg") #Imagen con bordes y binarizada
	draw = ImageDraw.Draw(imagen)	
	fuente = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-C.ttf',10)
	width, height = imagen.size
	total = width * height
	porcentajes = []
	centro = []
	corr = 0 ##Solo para corroborar porcentajes
	conteo = 0
	pixel = imagen.load()
	temp = []
	colorsR = [] #Para guardar colores R
	colorsG = [] #Para guardar colores G
	colorsB = [] #Para guardar colores B
	conteoColores = 0
	for i in range(width):			#Recorriendo imagen
    		for j in range(height):		#Recorriendo imagen
      			if pixel[i, j] == (0, 0, 0):	#Ir pintando pixeles (negros obviamente)
				r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)  #Asignando pixeles random
				
				n, x, y = bfs(imagen,(i,j),(r,g,b))				
				ptemp = float(n)/float(total) * 100.0	#Obteniendo porcentajes
				if ptemp > 0.2:
					  centro.append((sum(x) / len(x), sum(y) / len(y)))	  #Localizando centros
					  porcentajes.append([ptemp, (r, g, b)])
					  conteo += 1
        			else:
          				temp.append((x, y))
			elif pixel[i, j] == (255, 255, 255):
				pixel[i, j] == (255, 0, 0)
	fondo = porcentajes.index(max(porcentajes))
	color = porcentajes[fondo][1]
	for i in range(width):
    		for j in range(height):
      			if pixel[i, j] == color:
        			pixel[i, j] = (150, 150, 150)
	
  	for i in range(len(centro)):
    		if i == fondo:
        		pixel[centro[i]] = (255, 0, 0)	#Para poner centros de masa
			#Aqui va lo de las tags, proximamente en Tkinter o Pygame
    		else:
      			pixel[centro[i]] = (0, 255, 0)	
			draw.text((centro[i][0], centro[i][1]), 'C', fill=(0,0,255), font=fuente)
			draw.ellipse((centro[i][0], centro[i][1], 2000, 900), fill=(0, 0, 0))
			print "Centro :) ", centro[i]
			print pixel[centro[i]]
			print i
			print centro

			#imagen.text((i[0]+aux+3, i[1]), ('Tumor', fill=(0,0,255), font=fuente)

	imagen.save('meh4.jpg')	#Imagen definitiva
  	conteo = 1
	
	#for c in centro:
	#	i, j = centro[0], c[1]
	#	Tkinter.Label(canvas, text='Id %d'%conteo).place(x=i, y=j)
	#	conteo = conteo+1	
	
	#conteo = 1
  	for ptemp in porcentajes:
    		print "Porcentaje de figura %s: %.2f"%(conteo, ptemp[0])
    		conteo = conteo+ 1
		corr = ptemp[0] + corr 
	#print "Corroborando porcentaje: ", corr

# FIN ********************************************************************



if __name__ == "__main__":
	main()




