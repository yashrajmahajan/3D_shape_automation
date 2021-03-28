def penta(shape, l, scolour, bcolor):

	import turtle

	t = turtle.Turtle()
	n = 1

	t.speed(1)
	t.color(scolour)
	t.screen.bgcolor(bcolor)

	while n > 0:
		t.forward(l)
		t.left(72)
		t.forward(l)
		t.left(72)
		t.forward(l)				#First pentagon
		t.left(72)
		t.forward(l)
		t.left(72)
		t.forward(l)


		t.left(90)
		t.forward(l/2)
		t.right(20)

		t.forward(l)
		t.left(72)
		t.forward(l)
		t.left(72)
		t.forward(l)				#Second pentagon
		t.left(72)
		t.forward(l)
		t.left(72)
		t.forward(l)

		t.up()
		t.left(72)
		t.forward(l)
		t.down()
		t.right(163)
		t.forward(l/2)
		
		t.up()
		t.right(123)
		t.forward(l)

		t.down()
		t.right(58)
		t.forward(l/2 + 3) #error control using addtion of some value

		t.up()
		t.left(130)
		t.forward(l)

		t.down()
		t.left(50)
		t.forward(l/2)

		t.up()
		t.left(21)
		t.forward(l)

		t.down()
		t.left(162)
		t.forward(l/2 + 3)

		n = n-1