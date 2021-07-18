#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:28:13 2019

@author: rjnp2
"""
#importing all neccessary packages
import cv2
import numpy as np
from keras.models import load_model


img_size = 200
model = load_model('./model/my_model.h5')

animal = {
            0 : 'cat',
            1: 'dog',
            2: 'monkey',
            3 : 'cow',
            4 : 'elephant',
            5 : 'horse' ,
            6:'squirrel',
           7:  'chicken' ,
            8: 'spider' ,
             9: 'sheep'
        }

def animalprediction(path):

    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (int(img_size),int(img_size)))
    img = img.reshape(-1, img_size, img_size , 1).astype('float32')
    img /= 255 
    x = model.predict(img)
    y = x > 0.5  # when predict value in x is greater than 0.5,
                 # gives True
                 # else gives false
    
    # if any boolen values in y is True ,
    # if condition will be true
    # find animals names of give images
    if y.any():  
        x = np.argmax(x,axis = 1)
    
        pred_animal = animal[x[0]]
        
    else:
        pred_animal = "Not Found"
    
    print(pred_animal)    
    return  pred_animal

# path = '/home/rjnp2/Pictures/Webcam/images.jpeg'
# animalprediction(path)
