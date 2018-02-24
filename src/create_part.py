import note
from os import listdir
from os.path import isfile, join

def create_part(folder):
	res = []
	for f in listdir(folder):
		if isfile(join(folder, f)):
			n = note.get_note(join(folder, f))
			print(n)

create_part("../test")