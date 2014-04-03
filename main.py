from tkinter import *
from PIL import Image

class main():

	def __init__(self):

		self.loadImage()
		self.loadWindow()

	def loadWindow(self):
		root = Tk()
		frame = Frame(root)

		frame.pack()

		bottomframe = Frame(root)
		bottomframe.pack( side = BOTTOM )

		redbutton = Button(frame, text="Red", fg="red")
		redbutton.pack( side = LEFT)

		greenbutton = Button(frame, text="Brown", fg="brown")
		greenbutton.pack( side = LEFT )

		bluebutton = Button(frame, text="Blue", fg="blue")
		bluebutton.pack( side = LEFT )

		blackbutton = Button(bottomframe, text="Black", fg="black")
		blackbutton.pack( side = BOTTOM)

		root.mainloop()

	def loadImage(self):
		myimage = Image.open("Katakana_image.jpg")
		myimage.load()
		print("GAY")

app = main()