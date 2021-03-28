def cir(shape, l, scolour, bcolor):
	import turtle
	import numpy as np


	t = turtle.Turtle()
	n = 1
	t.speed(1)
	t.color(scolour)
	t.screen.bgcolor(bcolor) 

	while n > 0:

		t.circle(l)
		t.left(70)
		t.circle( l * 3 - 20, 45)
		t.left(135)
		t.circle( l * 3 - 20, 45)
		t.up()
		n = n - 1