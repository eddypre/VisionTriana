def poligono(imagen):

  im = Image.open(imagen)
	width, height = im.size
	pixels = im.load()
	
	for i in range(width):
		for j in range(height):
			vec = []
			for k in range(-1, 2):
				for l in range(-1, 2):
					if i+k >=  0 and j+l >= 0 and i+k < width and j+l < height:
						vec.append(pixels[i+k,j+l][1])
			vec.sort()
			posicion = len(vec)/2
			if len(vec) % 2 == 0:
				pixmed = (vec[posicion - 1] + vec[posicion])/2
			else:
				pixmed = vec[posicion]
		
			pixels[i,j] = (pixmed,pixmed,pixmed)
	im.save("temporal.png") # Hasta aqui filtro medio	
