from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, tkFileDialog, random, lines
from Tkinter import Tk, Label, Button, Entry, StringVar, NORMAL, END, W, E, settings

class GuessingGame:
	def __init__(self, master):
		self.master = master
		master.title("YAOMC")
		self.folder_button = Button(master, text="Select scores", command=self.pick_file)
		self.file_button   = Button(master, text="Select Output folder", command=self.pick_folder)
		self.gen_button    = Button(master, text="Generate", command=lines.separate_lines)
		self.folder_button.pack()
		self.file_button.pack()
		self.gen_button.pack()

	def pick_file(self):
		outdir = tkFileDialog.askopenfilename(initialdir = ".",title = "Select scores",filetypes =(("png files","*.png"),("all files","*.*")))

	def pick_folder(self):
		infile = tkFileDialog.askdirectory(initialdir = ".")

root   = Tk()
my_gui = GuessingGame(root)
root.mainloop()