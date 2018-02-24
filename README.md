Tutorial
https://www.tensorflow.org/get_started/premade_estimators

Input function is composed of
* feature: a name and its value. In our case the value should be an image of a key
* label: in supervised mode it is the value corresponding to the musical note: 0 (A), 1 (B),..

To train, you need to give features and corresponding labels
Shuffle and repeat for some reasons

Create the feature columns to give the model the twpe of data used for each features

Instantiate an estimator using Tenseflow pre-instances:
* Give layers and number of nodes
* Give number of classes






