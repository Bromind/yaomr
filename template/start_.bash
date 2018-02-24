#!/bin/bash

IMAGE_SIZE=224
ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"

if [ ${1+x} ]; then

python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=1000 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=../sain

cp tf_files/retrained_graph.pb ../src/retrained_graph_note.pb
cp tf_files/retrained_labels.txt ../src/retrained_labels_note.txt

python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=1000 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=../image_rythme

cp tf_files/retrained_graph.pb ../src/retrained_graph_rythme.pb
cp tf_files/retrained_labels.txt ../src/retrained_labels_rythme.txt


fi
  
python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=../test.png
