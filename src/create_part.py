import note
import io
import os
import ntpath
import settings

SORT = False

note_dic = {
	"la" : "a'",
	"si" : "b'",
	"do" : "c''",
	"re" : "d''",
	"mi" : "e''",
	"fa" : "f''",
	"sol": "g'",
	"junk" : "",
}
rythme_dic = {
	"noire"   : 4,
	"croches" : 8,
	"doubles" : 16,
	"junk"    : "",
}

def sort_blob(notes):
	for n in notes:
		os.rename(n[0], "../auto/" + n[1][0] + "/" + ntpath.basename(n[0]))
	pass

def create_part(files, folder_name):
	notes = note.get_notes(files, SORT)
	if SORT:
		sort_blob(notes)
		return
	partpath = "../output/" + folder_name
	partname = partpath + "/part.ly"
	part = open(partname, "w")
	part.write("""\\version "2.18.2"

global= {
  \key c \major
  \\time 4/4
}

violinSolo= \\new Voice {
""")
	prev_note = notes[0];
	for n in notes:
		if(n[0] != "junk"):
			part.write(note_dic[n[0]] + str(rythme_dic[n[1]]) + " ")
			prev_note = n
	part.write("""
}

\score {
	\\new Staff << \global \\violinSolo >>
	\layout { }"""
	if settings.midi:
		part.write("\t\midi { }")
	part.write("}")
	part.close()
	if settings.build:
		os.system("lilypond -o " + partpath + " " + partname)


