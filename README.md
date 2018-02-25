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






