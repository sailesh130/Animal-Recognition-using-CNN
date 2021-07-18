#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:45:46 2019

@author: rjn
"""

#importing all neccessary packages
import numpy as np
from keras import optimizers
from keras.models import Sequential
from keras.utils import to_categorical
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten

#initialize all variables
train_data = []
test_data = []
train_label = []
test_label = []

epochs = 150
batch_size = 200

#loading train_data and test_data 
train_data_load = np.load('/home/rjnp2/minorproject/image_array_data/train_data.npy' ,allow_pickle = True)
test_data_load = np.load('./image_array_data/test_data.npy' ,allow_pickle = True) 

for data in train_data_load:
    train_data.append(data[0])
    train_label.append(data[1])
    
train_data_load = 0    
   
for data in test_data_load:
    test_data.append(data[0])
    test_label.append(data[1])    

#pre-processing all data   
train_data = np.array(train_data).reshape(-1, 200,200,1).astype('float32')
test_data = np.array(test_data).reshape(-1, 200, 200 , 1).astype('float32')

#converting int datasets into float datasets 
# for easy processing by CPU/GPU
train_data /= 255
test_data /= 255

#saving rows,col,dim of datasets to input_shape variable
#to give input size /shape to CNN model 
input_shape = train_data.shape[1:]

#convert int labels of data into categorial
# eg: 0 = 1 0 0 0 0 0 0 0 0 0 
train_labels_one_hot = to_categorical(train_label)
test_labels_one_hot = to_categorical(test_label)

def createCNNModel():
    '''
    to create cnn model
    using built-in functions of keras such as
    conv2D,
    maxpooling2D,
    flatten,
    dropout
    '''

    #creating a Neural network is to initialise the network using the Sequential Class from keras.
    model = Sequential()
    
    # The first two layers with 64 filters of window size 3x3
    # filters : Denotes the number of Feature detectors
    # kernel_size : Denotes the shape of the feature detector. (3,3) denotes a 3 x 3 matrix.
    # input _shape : standardises the size of the input image
    # activation : Activation function to break the linearity
    model.add(Conv2D(filters = 64, kernel_size=(3, 3),activation='relu', 
                     input_shape= input_shape))
    model.add(Conv2D(filters = 64, kernel_size=(3, 3), activation='relu'))

    # pool_size : the shape of the pooling window.
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(filters = 64, kernel_size=(3, 3), activation='relu'))
    model.add(Conv2D(filters = 64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    
    model.add(Conv2D(filters = 64, kernel_size=(3, 3), activation='relu'))
    model.add(Conv2D(filters = 64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    
    model.add(Conv2D(filters = 64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Flatten())

    # units: Number of nodes in the layer.
    # activation : the activation function in each node.
    model.add(Dense(units = 512, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(units = 286, activation='relu'))
    model.add(Dense(units = 10, activation='softmax'))
    
    return model


model = createCNNModel()
model.summary()

# Optimiser: the Optimiser  used to reduce the cost calculated by categorical_crossentropy
# Loss: the loss function used to calculate the error
# Metrics: the metrics used to represent the efficiency of the model
# lr : learing rates
rmsprop = optimizers.RMSprop(lr=0.0005)
model.compile(optimizer= rmsprop , loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x= train_data, y= train_labels_one_hot,
                     batch_size = batch_size,
                     epochs=epochs,
                     verbose=1, 
                     validation_data = (test_data,test_labels_one_hot) 
                     )

model.save('my_model.h5')  # creates a HDF5 fil 'my_model.h5'

# for visualizing losses and accuracy
# History.history attribute is a record of training loss values
# metrics values at successive epochs 
# as well as validation loss values and validation metrics values
train_loss=history.history['loss']
val_loss=history.history['val_loss']
train_acc=history.history['acc']
val_acc=history.history['val_acc']
xc=range(epochs)
model_histroy = [
        train_loss,
        val_loss,
        train_acc,
        val_acc,
        xc]
np.save('model_histroy.npy',model_histroy)
