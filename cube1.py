def cube(shape, l, scolour, bcolor):
	import turtle
	import numpy as np

	p = l

	print(p)

	a = (l*l)+(l*l)

	a = np.sqrt(a)

	t = turtle.Turtle()
	n = 1

	t.speed(1)
	t.color(scolour)
	t.screen.bgcolor(bcolor)

	while n > 0:

		t.forward(l)
		t.right(90)
		t.forward(l)
		t.right(90)			#first square
		t.forward(l)
		t.right(90)
		t.forward(l)
		

		t.up()
		t.forward(l/2)
		t.right(90)
		t.forward(l/2)
		t.down()

		t.forward(l)
		t.right(90)
		t.forward(l)
		t.right(90)			#Second square
		t.forward(l)
		t.right(90)
		t.forward(l)
		

		t.left(135)
		t.forward(a/2)

		t.left(45)
		t.up()
		t.forward(l)

		t.left(135)
		t.down()
		t.forward(a/2)
		t.up()
		t.forward(a/2)
		t.down()
		t.forward(a/2)

		t.up()
		t.right(135)
		t.forward(l)
		t.right(45)
		t.down()
		t.forward(a/2)


		t.right(45)
		t.forward(l)
		t.right(90)
		t.forward(l)

		t.up()
		t.forward(l/2)
		t.right(90)
		t.forward(l/2)
		t.down()
		n = n - 1
