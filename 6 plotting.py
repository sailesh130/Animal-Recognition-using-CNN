#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 12:59:43 2019

@author: rjnp2
"""

#importing all neccessary packages
from keras.models import load_model,Model
import matplotlib.pyplot as plt
import cv2

#loading model and reading images
img = cv2.imread('/home/rjnp2/minorproject/dataset/test_data/cat/cat.33.jpeg',0)
img = cv2.resize(img,(200,200))
img = img/255
model = load_model('./model/my_model.h5')

# Visualizing activations of convolutional layer    
layer_outputs = [layer.output for layer in model.layers]
activation_model = Model(inputs=model.input, output =layer_outputs)
activations = activation_model.predict(img.reshape(1,200,200,1))
       
def conv2d_plot_weight(index): 

    weight_conv2d = model.layers[index].get_weights()[0][:,:,0,:]
    shape = weight_conv2d.shape[2]
    row_size = 8
    col_size = int(shape / row_size)
    filter_index = 0
    fig, ax = plt.subplots(row_size, col_size, figsize=(12,12))
    for row in range(0,row_size):
        for col in range(0,col_size):
            ax[row][col].imshow(weight_conv2d[:,:,filter_index],cmap="gray")
            filter_index += 1    
            
conv2d_plot_weight(0)  

def display_activation(activations):
    
    li = [0,1,2,4,5,6,8,9,10,12,13]
    for i in li:
        activation = activations[i]
        activation_index= 17
        plt.imshow(activation[0, :, :, activation_index], cmap='gray')
        plt.show()

display_activation(activations)    
