![alt text](https://github.com/Bromind/yaomr/raw/master/REAME_Picture.jpg) 

# Dependencies 
python2.7
pip install opencv-python
https://www.tensorflow.org/

# Tutorial
For this project; we used
https://www.tensorflow.org/get_started/premade_estimators
https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0

It helped us to understand the basics for machine learning. This project adapted some examples in order to generate PDF partitions and MIDI files from scanned partitions either downloaded from Internet or handwritten ones or scanned using a smartphone.

This project extracts the various blobs from partitions and deduces the corresponding tone and rythms. 
- The detection of the blob is done using OpenCV: https://opencv.org/ and python2.7
- The deduction of the tone is done using machine learning. During this project we trained a network with samples of partitions.

# Structure

This repository has the following structure:
- folder _asset/_ is used to store partitions that will be parsed
- folder _src/_ contains scripts related to the scripts used for detecting the blobs in the partition. It also contain the basic GUI to start the project.
- folder _template/_ contains the source of the tensorflow and the settings to setup the model
- folder _output/_ contains the parsed blobs from a partition
- folders _image_note/_ and _image_rythme/_ contains the sample data used for training the model

# Use this project

Go into _src/_ folder and start:
``` python gui.py ```
A GUI window should appear and you need to select the partition file and the output directory

The model needs to be trained and 
See _template/setup_.bash_ to train the model with the dataset and export the files that will be used.
Update the folders depending on the dataset you need to train/


# Random information

Input function is composed of
* feature: a name and its value. In our case the value should be an image of a key
* label: in supervised mode it is the value corresponding to the musical note: 0 (A), 1 (B),..

To train, you need to give features and corresponding labels
Shuffle and repeat for some reasons

Create the feature columns to give the model the twpe of data used for each features

Instantiate an estimator using Tenseflow pre-instances:
* Give layers and number of nodes
* Give number of classes

# Music dataset

We provide a minimal dataset to train to recognize music symbols. We assume the score starts with a trebble clef, and our goal is to recognize notes from the G on the second line to the F on the 5th line. We also want to recognize the rythm.

In order to train our neural network, we accumulated around 1300 musical symbols in various format. In order to avoid other people the tedious to categorize symbols by themself, we provide our dataset included in this repository. 

Two folders are provided, one sorted according to which note is on the image, and the other one depending on the rythm. The note data set includes 8 subfolders, one for each note plus one for junk symbols (silences, bars, tempi, etc.). Subfolders are named according to the french nomenclature with the correspondance with the letter system is provided below. All notes are natural.

French name | Letter
---|---
LA | A
SI | B
DO | C
RÉ | D
MI | E
FA | F
SOL| G

The rythm folder is divided in four subfolders, three for common rythms and the last one for junk. Subfolders are named according to the french nomenclature, which correspondance with the english system is provided below.

French name | English Name
---|---
Noire | Quarter
Croche | Eighth
Double Croche | Sixteenth

This dataset is not complete, it only covers a small part of music grammar, but is suitable for rapid prototyping. It was sorted by hand, hence errors *do* exists, although we hope they are not numerous. Considering the way the dataset was built, it is likely to be biased and hence, is provided *as is*, no guarantees are provided.
