'''
  Deteccion de agujeros por medio de histogramas
	Eduardo Triana - ITS
'''

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

	transformar()
	convolucion()
	umbrales()
	agujeros()
	#formas()
	#dibujar()

#Funcion para escala de grises
#Se accede a ella presionando 1
def transformar():
	#tiempoInicial = time.time()
	i = 0
	x = 0
	y = 0
	im = Image.open("news/in1.JPG")
 
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
	im.save('1/temp1.JPG')
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
	
	im = Image.open("1/temp1.JPG")
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
	
	im.save('1/temp2.JPG')					
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
	im = Image.open("1/temp2.JPG")
 
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
	im.save('1/temp3.JPG')
	#tiempoFinal = time.time()
	
#Implelementacion de bfs ***************************************************
#***************************************************************************

def bfs(im, origen, color):
	pix = im.load() #La imagen 
	w, h = im.size
	q = []
	xs = []
	ys = []
	q.append(origen) # el origen, donde el punto es negro[coordenada]
	#print "origen en coordenada: ", origen
	#print "color del origen: ", pix[origen]
	original = pix[origen] 
	n = 0
	while len(q) > 0:
		#print "vuelta"
		(x, y) = q.pop(0)
		actual = pix[x, y]
		#print "actual: ", actual, " original: ", original, "color: ", color
		if actual == original or actual == color:
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					i, j = (x + dx, y + dy)
					if i >= 0 and i < w and j >= 0 and j < h:
						contenido = pix[i, j]
						#print "contenido = ", contenido, "original = ", original
						#print "contenido: ", contenido
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

	imagen = Image.open("1/temp3.JPG") #Imagen con bordes y binarizada
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
			#draw.ellipse((centro[i][0], centro[i][1], 2000, 900), fill=(0, 0, 0))
			print "Centro :) ", centro[i]
			print pixel[centro[i]]
			print i
			print centro

			#imagen.text((i[0]+aux+3, i[1]), ('Tumor', fill=(0,0,255), font=fuente)

	imagen.save('1/temp4.JPG')	#Imagen definitiva
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

def origenes():
	nelipses = int(argv[1])
	imagen = Image.open("in.png")
	x, y = imagen.size

	rx = random.randint(110, 400) 	#radio x entre 200 y 50
	ry = random.randint(90, 300)	#radio y entre 100 y 40
	
	cx = random.randint(110, x-110) 	#Para coordenadas de los centros
	cy = random.randint(110, y-110)

	return rx, ry, cx, cy

def dibujar():
	nelipses = int(argv[1])
	
	imagen = Image.open("in.png") #Imagen con bordes y binarizada
	#draw = ImageDraw.Draw(imagen)	
	fuente = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-C.ttf',20)
	x, y = imagen.size
	total = x * y
	pixels1 = imagen.load()
	#radiox = 300
	#radioy = 200

	#centrox = x/2
	#centroy = y/2	
	Cx = [] #listas para guardar los centros
	Cy = []
	enes = [] #Para calcular porcentajes

	for i in range(nelipses):
		draw = ImageDraw.Draw(imagen)	
		radiox, radioy, centrox, centroy = origenes()
		Cx.append(centrox)
		Cy.append(centroy)
		box = (centrox - radiox/2, centroy - radioy/2, centrox + radiox/2, centroy + radioy/2)	
															
		#box = (centrox - radiox/2, centroy - radioy/2, centrox + radiox/2, centroy + radioy/2)
		draw.ellipse(box, fill=None, outline= (0,255,0))
		del draw
		for angulo in range (0,360):
			puntox = centrox + (radiox/2*cos(angulo))
			puntoy = centroy + (radioy/2*sin(angulo))
			#listax.append(puntox)
			#listay.append(puntoy)
			for h in range (-2,2):
				for o in range(-2,2):
					if puntox+h >= 0 and puntoy+o >=0 and puntox+h < x and puntoy+o <y:
						pixels1[puntox+h,puntoy+o] = (255,0,0)
						#print "punto en x: ", puntox, "punto en y: ", puntoy
						#pixels1[puntox,puntoy] = (255,0,0)
			
	imagen.save('parcial1.png')

	#Rellenado y etiquetado
	ima = Image.open("parcial1.png")
	pixels2 = ima.load()
	for i in range(nelipses):
		dibujo = ImageDraw.Draw(ima)
		r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)  #Asignando pixeles random
		n, x2, y2 = bfs(ima,(Cx[i],Cy[i]),(r,g,b,255))
		pixels2[Cx[i], Cy[i]] = (0,0,255) #Para pintar de azul cada uno de los centros
		dibujo.text((Cx[i], Cy[i]), 'ID '+str(i), fill=(0,0,255), font=fuente) #Para pintar el ID de cada figura

		enes.append(n)
	ima.save('out.png')

	#Imprimiendo porcentajes de los elipses con respecto a las dimensiones de la imagen total
	
	for i in range(nelipses):
		porcentaje = float(enes[i])/float(total) * 100.0
		print "Porcentaje de elipse ID ", i, " = ", porcentaje

	#FIN DE LA FUNCION DIBUJAR ... 

	#INICIO PARA DETECCION DE AGUJEROS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def agujeros():

	lateralx = open('dats/horizontal.dat','a') #Abro el archivo
	lateraly = open('dats/vertical.dat','a') #Abro el archivo

	marcarLineasx = []	#Para guardar los puntos donde marcar las lineas x
	marcarLineasy = [] 	#Para guardar los puntos donde marcar las lineas y

	sumasx = [] #Incluye las sumas de cada renglon
	sumasy = [] #Incluye las sumas de cada columna
	#transformar()
	imagen = Image.open("1/temp1.JPG") #Imagen con bordes y binarizada
	#draw = ImageDraw.Draw(imagen)	
	fuente = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-C.ttf',18)
	width, height = imagen.size
	total = width * height
	pixels1 = imagen.load()
	addsx = 0	#Para llevar la cuenta de las sumas

	'''**********SUMAS DE X***************'''
	
	for i in range(height):		#La variable i controla las columnas 		
		#print adds		
		#sumasx.append(adds)		
		addsx = 0	
    		for j in range(width):	#La variable j va de x0  a xn
			#pixels1[j, i] = (255,255,255)
			addsx = addsx + pixels1[j, i][0]
			#print "j =", j, "i = ", i, "color = ", pixels1[j, i][0]
		sumasx.append(addsx)
		#if addsx < 210000:
		#	marcarLineasx.append(i)
		
		#Escribiendo la fila y la intensidad(suma de los pixeles del renglon)	
		lateralx.write(str(i))
		lateralx.write(' ')
		lateralx.write(str(addsx))
		lateralx.write('\n')
	#print sumasx

	maximox = max(sumasx)	
	minimox = min(sumasx)

	print sumasx
	print "Sumas de x = ", len(sumasx), "\n\n"
	print "Maximo de las sumas de x = ", maximox
	print "Minimo de las sumas de x = ", minimox

	'''*********SUMAS DE Y*****************'''

	addsy = 0	#Llevar cuentas de las sumas
	for i in range(width):
		addsy = 0
		for j in range(height):
			draw = ImageDraw.Draw(imagen)
			addsy = addsy + pixels1[i, j][0]
		sumasy.append(addsy)
		#if addsy < 185000:
		#	marcarLineasy.append(i)

		lateraly.write(str(i))
		lateraly.write(' ')
		lateraly.write(str(addsy))
		lateraly.write('\n')

	######Obteniendo los umbrales
	umbralx = (sum(sumasx))/(len(sumasx))
	umbraly = (sum(sumasy))/(len(sumasy))
	
	#flagx = 
	#flagy = 

	#######Obteniendo los puntos donde poner las lineas
	for i in range(len(sumasx)):
		if i != (len(sumasx)-1) and i != 0:
			if (sumasx[i-1] > sumasx[i] < sumasx[i+1]) and sumasx[i]<(umbralx-3000):
				#flag.append(i)
				marcarLineasx.append(i)
				
	for j in range(len(sumasy)):
		if j != (len(sumasy)-1) and j != 0:
			if (sumasy[j-1] > sumasy[j] < sumasy[j+1]) and (sumasy[j]<(umbraly-4000)):
				marcarLineasy.append(j)
	
	#######Marcando las lineas
	centrosy = []	
	centrosx = []
	
	centrosy.append(marcarLineasy[0]) #meter el primer elemento
	for i in range(len(marcarLineasy)):
		if i != (len(marcarLineasy)-1):
			dif = abs((marcarLineasy[i]) - (marcarLineasy[i+1]))
			if dif > 50:
				centrosy.append(marcarLineasy[i+1]) 

	################################################################

	centrosx.append(marcarLineasx[0]) #meter el primer elemento
	for i in range(len(marcarLineasx)):
		if i != (len(marcarLineasx)-1):
			dif2 = abs((marcarLineasx[i]) - (marcarLineasx[i+1]))
			if dif2 > 50:
				centrosx.append(marcarLineasx[i+1])

	#PINTANDO LAS RECTAS, AHORA SI UNA SOLA RECTA POR CADA AGUJERO

	for i in centrosy:
		draw = ImageDraw.Draw(imagen)
		draw.line((i, 0, i, imagen.size[1]), fill=(0, 255, 0))

	for i in centrosx:
		draw = ImageDraw.Draw(imagen)
		draw.line((0, i, imagen.size[0], i), fill=(255, 0, 0))


	#######puntos centro
	newcentrosy = centrosy[:]
	newcentrosy.reverse()

	for i in range(len(centrosx)): #Aqui podria ser centros x o y, no hay problema
		draw = ImageDraw.Draw(imagen)
		draw.text((newcentrosy[i], centrosx[i]), 'ID '+str(i), fill=(255,233,0), font=fuente) #Para pintar el ID de cada figura		
		pixels1[newcentrosy[i], centrosx[i]] = (255, 233, 0)
	

	#**************************************  pintura *******************************************
	im = Image.open("1/temp3.JPG") #Imagen con bordes y binarizada
	pix = im.load()
	wi, he = imagen.size
	enes = [] #Guarda porcentajes	
	
	for i in range(len(centrosx)): #Aqui podria ser centros x o y, no hay problema
		dibujo = ImageDraw.Draw(im)
	
		r, g, b = random.randint(139, 150), random.randint(122, 126), random.randint(120, 255)  #Asignando pixeles random	
		n, x2, y2 = bfs(im,(newcentrosy[i],centrosx[i]),(r,g,b))
	
		dibujo.text((newcentrosy[i], centrosx[i]), 'ID '+str(i), fill=(255,233,0), font=fuente) #Para pintar el ID de cada figura		
		pix[newcentrosy[i], centrosx[i]] = (255, 233, 0) #Punto de amarillo
		enes.append(n)
	
	im.save('1/temp4.JPG')

	#************************************ fin pintura ******************************************

	#************************************ porcentajes ******************************************

	for i in range(len(centrosx)): #Aqui podria ser centros x o y, no hay problema
		porcentaje = float(enes[i])/float(total) * 100.0
		print "Porcentaje de agujero ID ", i, " = ", porcentaje
	
	#********************************** fin porcentajes ******************************************
		
	
	#Puntos de referencia
	
	#for j in centrosy:
	#	pixels1[j] = (0, 0, 255)

	#for j in centrox:
	#	pixels1[j] = (0, 0, 255)
	'''			

	for i in marcarLineasy:
		draw = ImageDraw.Draw(imagen)
		draw.line((i, 0, i, imagen.size[1]), fill=(0, 255, 0))
		
	centrosx = 
	for i in marcarLineasx:
		draw = ImageDraw.Draw(imagen)
		draw.line((0, i, imagen.size[0], i), fill=(255, 0, 0))
	'''

	maximoy = max(sumasy)
	minimoy = min(sumasy)	
	print sumasy
	print "Sumas de y = ", len(sumasy)
	print "Maximo de las sumas de y = ", maximoy
	print "Minimo de las sumas de y = ", minimoy
	#if addsy < 200000:
	#marcarLineasy.append(i) 
	
	#print "Puntos donde van las lineas = ", marcarLineasy		
	print "umbralx = ", umbralx
	print "umbraly = ", umbraly

	print "\nmarcarLineasx = ", marcarLineasx
	print "marcarLineasy = ", marcarLineasy

	print "\ncentrosx = ", centrosx
	print "centrosy = ", centrosy
	print "newcentrosy = ", newcentrosy



	lateralx.close()
	lateraly.close()
			

	imagen.save('1/out.JPG')	
	imagen.show()


if __name__ == "__main__":
	main()




