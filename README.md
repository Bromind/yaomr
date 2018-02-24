pip install opencv-python


Tutorial
https://www.tensorflow.org/get_started/premade_estimators

Go into src and start separator.py to generate images that will be used in the estimator
cd src
python separator.py -i <name without extention of file in ../assets>

Setup/Start tenseflow
https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0

See template/setup_.bash

#############

Input function is composed of
* feature: a name and its value. In our case the value should be an image of a key
* label: in supervised mode it is the value corresponding to the musical note: 0 (A), 1 (B),..

To train, you need to give features and corresponding labels
Shuffle and repeat for some reasons

Create the feature columns to give the model the twpe of data used for each features

Instantiate an estimator using Tenseflow pre-instances:
* Give layers and number of nodes
* Give number of classes






