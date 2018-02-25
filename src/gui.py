from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, tkFileDialog, random, lines, param
from Tkinter import Tk, Label, Button, Entry, StringVar, Checkbutton, NORMAL, END, W, E
import sys, getopt

inputfile  = ''
outputfolder = ''
argv = sys.argv[1:]
try:
	opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofolder="])
except getopt.GetoptError:
	print 'gui.py -i <inputfile> -o <outputfolder>'
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print 'yaomc.py -i <inputfile> -o <outputfolder>'
		sys.exit()
	elif opt in ("-i", "--ifile"):
		inputfile = arg
	elif opt in ("-o", "--ofile"):
		outputfolder = arg

class MainGui:
	def __init__(self, master):
		self.master = master
		master.title("YAOMC")
		self.folder_button = Button(master, text="Select scores", command=self.pick_file)
		self.file_button   = Button(master, text="Select Output folder", command=self.pick_folder)
		self.gen_button    = Button(master, text="Generate", command=lines.separate_lines)
		self.exit_button   = Button(master, text="Exit", command=master.quit)
		self.folder_text   = StringVar()
		self.file_text     = StringVar()
		self.folder_text.set("none." if outputfolder == '' else outputfolder)
		self.file_text  .set("none." if inputfile    == '' else inputfile)
		param.outdir = "none." if outputfolder == '' else outputfolder
		param.infile = "none." if inputfile    == '' else inputfile
		self.folder_label  = Label (master, textvariable=self.folder_text)
		self.file_label    = Label (master, textvariable=self.file_text)
		self.build_check   = Checkbutton(master, text="build")
		self.midi_check    = Checkbutton(master, text="midi" )
		self.build_check.select()
		self.midi_check.select()
		self.folder_label.grid  (row=1, column=2, sticky=W)
		self.file_label.grid    (row=2, column=2, sticky=W)
		self.file_button.grid   (row=1, column=1, sticky=W)
		self.folder_button.grid (row=2, column=1, sticky=W)
		self.gen_button.grid    (row=3, column=1)
		self.exit_button.grid   (row=3, column=2)
		self.build_check.grid   (row=4, column=1)
		self.midi_check.grid    (row=4, column=2)

	def pick_file(self):
		param.infile = tkFileDialog.askopenfilename(initialdir = ".",title = "Select scores",filetypes =(("png files","*.png"),("all files","*.*")))
		self.file_text.set(param.infile)

	def pick_folder(self):
		param.outdir = tkFileDialog.askdirectory(initialdir = ".")
		self.folder_text.set(param.outdir)

root   = Tk()
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
my_gui = MainGui(root)
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)
root.mainloop()
