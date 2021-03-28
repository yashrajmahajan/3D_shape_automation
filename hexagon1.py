def hexa(shape, l, scolour, bcolor):

	import turtle

	t = turtle.Turtle()
	n = 1

	t.speed(1)
	t.color(scolour)
	t.screen.bgcolor(bcolor)

	while n > 0:
		t.forward(l)
		t.left(60)
		t.forward(l)
		t.left(60)
		t.forward(l)				#First hexagon
		t.left(60)
		t.forward(l)
		t.left(60)
		t.forward(l)
		t.left(60)
		t.forward(l)

		t.left(90)
		t.forward(l/2)
		t.right(30)

		t.forward(l)
		t.left(60)
		t.forward(l)
		t.left(60)
		t.forward(l)				#First hexagon
		t.left(60)
		t.forward(l)
		t.left(60)
		t.forward(l)
		t.left(60)
		t.forward(l)

		t.up()
		t.left(60)
		t.forward(l)
		t.down()
		t.right(150)
		t.forward(l/2)

		t.up()
		t.right(150)
		t.forward(l)

		t.down()
		t.right(30)
		t.forward(l/2)

		t.up()
		t.left(90)
		t.forward(l)

		t.down()
		t.left(90)
		t.forward(l/2)

		t.up()
		t.left(-30)
		t.forward(l)

		t.down()
		t.left(210)
		t.forward(l/2)

		t.up()
		t.left(210)
		t.forward(l)

		t.down()
		t.left(-30)
		t.forward(l/2)

		n = n-1