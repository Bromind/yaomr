import note
import io

SORT = True

note_dic = {
	"la" : "a",
	"si" : "b",
	"do" : "c",
	"re" : "d",
	"mi" : "e",
	"fa" : "f",
	"sol": "g",
}
rythme_dic = {
	"half"      : 2,
	"quarter"   : 4,
	"sixteenth" : 6,
	"eighth"    : 8,
}

def sort_blob(notes):
	for n in notes:
		print(n)
	pass

def create_part(files):
	print("lehwfjk")
	notes = note.get_notes(files, SORT)
	if SORT:
		sort_blob(notes)
		return
	part = open("part.ly", "w")
	part.write("""\\version "2.18.2"

global= {
  \key c \major
  \\time 4/4
}

violinSolo= \\new Voice \\relative a' {
""")
	for n in notes:
		part.write(note_dic[n[0]] + str(rythme_dic[n[1]]) + " ")
	part.write("""
}

\score {
    \\new Staff << \global \\violinSolo >>
  \layout { }
}""")

