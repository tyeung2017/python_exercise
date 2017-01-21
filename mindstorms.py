import turtle

def draw_square():
	for i in xrange(4):
		draw.forward(100)
		draw.right(90)
#	draw.forward(100)
#	draw.right(90)
#	draw.forward(100)
#	draw.right(90)
#	draw.forward(100)
#	draw.right(90)

def circle():
	d = turtle.Turtle()
	d.shape("arrow")
	d.color(0,0,0)
	d.circle(50)

def tri():
	#d = turtle.Turtle()
	turtle.colormode(255)
	#d.color((255,255,255))
	#d.shape("triangle")
	#d.right(180)
	for i in xrange(3):
		draw.forward(100)
		draw.left(120)

window = turtle.Screen()
window.bgcolor("black")
draw = turtle.Turtle()
draw.shape("turtle")
draw.color("yellow", "black")
draw.speed(100)

for i in range(36): # for flower
	draw_square()
	draw.right(10)
#circle()
#tri()
draw.color("green")
draw.right(90)
draw.forward(300)

#tri()

#for Sierpinski_Triangle


window.exitonclick()
