def findshape(shape, l, scolour, bcolor):

	import cube1
	import triangle1
	import pentagon1
	import hexagon1
	import circle
	import rectangle1
	
	if shape == 'cube' :
		cube1.cube(shape, l, scolour, bcolor)

	elif shape == 'triangle' :
		triangle1.tri(shape, l, scolour, bcolor)

	elif shape == 'pentagon' :
		pentagon1.penta(shape, l, scolour, bcolor)

	elif shape == 'circle' :
		circle.cir(shape, l, scolour, bcolor)

	elif shape == 'rectangle' :
		rectangle1.rec(shape, l, scolour, bcolor)

	else:
		hexagon1.hexa(shape, l, scolour, bcolor)