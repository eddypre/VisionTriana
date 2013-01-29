#Pedir megapixeles
#Pedir dimensiones

#Obtener resoluciones
import pygame
from pygame.locals import*
from PIL import Image

def main():
	
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption("Bla")

	fondo = pygame.image.load("bla.jpg").convert()
	#Posicion
	screen.blit(fondo, (0, 0))
	pygame.display.flip()
	transformar()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	
def transformar():
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

			print tupla, "--", a,",",b,",",c
	im.save('meh.jpg')

if __name__ == "__main__":
	main()

