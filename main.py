'''
Hello this yashraj, if you have any query or work related Information Technology
then ask friendly on : yashrajmahajan260@gmail.com
'''

# develops a simple software using python
import shapes
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Auther- Yash")

shape = StringVar()
l = IntVar()
scolour = StringVar()
bcolor = StringVar()


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
  
def sel():			#submit button function 

#=========Shape=======
	shape = E1.get()


#=======length========
	l = int(E2.get())
	ans.config(text = "Done")
	   
#=========colour=========
	scolour = E3.get()


#========Bg_colour=======
	bcolor = E4.get()


#==========final_call=================
	shapes.findshape(shape, l, scolour, bcolor)
	print(shape)
	
#================================================Menubar========================================================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

#===============Background canvas===============================================================================

C = Canvas(root,height=250, width=300)
filename = PhotoImage(file = "ok.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#==================================================================================================================

#====================Main widge==================================================================================

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

L1 = Label(root, text="Shapes")		# shape of 3d diagram
L1.pack( side = TOP)

E1 = ttk.Combobox(root, textvariable = shape)
E1['values'] = (	'cube',
					'triangle',
					'rectangle',
					'pentagon',
					'hexagon',
					'circle')
E1.pack(side = TOP)

L2 = Label(root, text="Length")		# length of 3d diagram
L2.pack( side = TOP)
E2 = Entry(root, bd =5)
E2.pack(side = TOP)

L3 = Label(root, text="Colour")		# colour of 3d diagram
L3.pack( side = TOP)
E3 = ttk.Combobox(root, textvariable = scolour)
E3['values'] = (	'default',
					'blue',
					'green',
					'cyan',
					'red',
					'magenta',
					'yellow',
					'white',
					'brown',
					'plum',
					'orange')
E3.pack(side = TOP)

L4 = Label(root, text="Background")	# background colour of 3d diagram
L4.pack( side = TOP)
E4 = ttk.Combobox(root, textvariable = bcolor)
E4['values'] = (	'default',
					'blue',
					'green',
					'cyan',
					'red',
					'magenta',
					'yellow',
					'white',
					'brown',
					'plum',
					'orange')
E4.pack(side = TOP)

button1 = Button(text="Start", command = sel) #submit button
button1.pack()

ans = Label(root, text = "")
ans.pack()

#=================================================================================================================
root.config(menu=menubar)
root.mainloop()