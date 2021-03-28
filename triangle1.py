def tri(shape, l, scolour, bcolor):

	import turtle
	import numpy as np

	t = turtle.Turtle()
	n = 1
	t.speed(1)
	t.color(scolour)
	t.screen.bgcolor(bcolor)

	while n > 0:

		t.forward(l)
		t.left(120)
		t.forward(l)
		t.left(120)
		t.forward(l)

		t.left(135)
		t.forward(l/2)
		t.right(15)

		t.forward(l)
		t.left(120)
		t.forward(l)
		t.left(120)
		t.forward(l)

		t.up()
		t.left(120)
		t.forward(l)
		t.right(165)
		t.down()
		t.forward(l/2)

		t.up()
		t.right(75)
		t.forward(l)
		t.right(105)
		t.down()
		t.forward(l/2)

		n = n-1