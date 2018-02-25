# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import time

import Tkinter
from Tkinter import Tk, Label, Button, Entry, StringVar, Checkbutton, Radiobutton, NORMAL, END, W, E
from PIL import Image, ImageTk

import numpy as np
import tensorflow as tf

def load_graph(model_file):
	graph = tf.Graph()
	graph_def = tf.GraphDef()

	with open(model_file, "rb") as f:
		graph_def.ParseFromString(f.read())
	with graph.as_default():
		tf.import_graph_def(graph_def)

	return graph

def read_tensor_from_image_file(file_name, input_height=299, input_width=299,
				input_mean=0, input_std=255):
	input_name = "file_reader"
	output_name = "normalized"
	file_reader = tf.read_file(file_name, input_name)
	image_reader = tf.image.decode_png(file_reader, channels = 3,
									   name='png_reader')
	float_caster = tf.cast(image_reader, tf.float32)
	dims_expander = tf.expand_dims(float_caster, 0);
	resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
	normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
	sess = tf.Session()
	result = sess.run(normalized)

	return result

def load_labels(label_file):
	label = []
	proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
	for l in proto_as_ascii_lines:
		label.append(l.rstrip())
	return label


input_height            = 224
input_width             = 224
input_mean              = 128
input_std               = 128
graph_note              = load_graph("retrained_graph_note.pb")
graph_rythme            = load_graph("retrained_graph_rythme.pb")
input_operation_note    = graph_note.get_operation_by_name("import/input");
output_operation_note   = graph_note.get_operation_by_name("import/final_result");
input_operation_rythme  = graph_rythme.get_operation_by_name("import/input");
output_operation_rythme = graph_rythme.get_operation_by_name("import/final_result");
labels_note             = load_labels("retrained_labels_note.txt")
labels_rythme           = load_labels("retrained_labels_rythme.txt")
sess_note               = tf.Session(graph=graph_note)
sess_rythme             = tf.Session(graph=graph_rythme)

popup_threshold = 0.5
v=0

def get_note(file_name):
	t = read_tensor_from_image_file(file_name,
								  input_height=input_height,
								  input_width=input_width,
								  input_mean=input_mean,
								  input_std=input_std)

	results_note = np.squeeze(sess_note.run(
		output_operation_note.outputs[0],
		{input_operation_note.outputs[0]: t}
	))
	top_k_note   = results_note.argsort()[-1:][0]


	results_rythme = np.squeeze(sess_rythme.run(
		output_operation_rythme.outputs[0],
		{input_operation_rythme.outputs[0]: t}
	))
	top_k_rythme   = results_rythme.argsort()[-1:][0]

	return (labels_note[top_k_note], labels_rythme[top_k_rythme], file_name, results_note[top_k_note], results_rythme[top_k_rythme])

def get_notes(files, sort):
    res = []
    for f in files:
        n = get_note(f)
        if n[3] < popup_threshold:
            n = (popup_ask_note(f), n[1], n[2], 1, n[4])
        print(f + " " + str(n[0]) + " " + str(n[3]))
        if sort:
            res.append((f,n))
        else:
            res.append(n)
    return res


class PopUp:
    def __init__(self, master, filename):
        self.master = master
        imag = Image.open(filename)
        display = ImageTk.PhotoImage(imag)
        photo = Label(master, image=display)
        #photo.pack()
        self.question = Label(master, text="What note is on this picture ?")
        self.question.pack()
        self.r1 = Radiobutton(master, text="do", variable=v, value=0)
        self.r1.pack()
        self.r2 = Radiobutton(master, text="re", variable=v, value=5)
        self.r2.pack()
        self.r3 = Radiobutton(master, text="mi", variable=v, value=4)
        self.r3.pack()
        self.r4 = Radiobutton(master, text="fa", variable=v, value=1)
        self.r4.pack()
        self.r5 = Radiobutton(master, text="sol", variable=v, value=7)
        self.r5.pack()
        self.r6 = Radiobutton(master, text="la", variable=v, value=3)
        self.r6.pack()
        self.r7 = Radiobutton(master, text="si", variable=v, value=6)
        self.r7.pack()
        self.r8 = Radiobutton(master, text="junk", variable=v, value=2)
        self.r8.pack()
        self.valbut = Button(master, text="Validate", command=master.destroy)
        self.valbut.pack()
        #self.photo.grid(row=1, column=2)



def popup_ask_note(filename):
    root   = Tk()
    root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
    my_gui = PopUp(root, filename)
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    root.mainloop()
    return labels_note[v]
