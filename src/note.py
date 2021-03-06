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
        print(f + " " + str(n[0]) + " " + str(n[3]))
        if sort:
            res.append((f,n))
        else:
            res.append(n)
    return res
