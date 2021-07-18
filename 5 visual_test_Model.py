#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:44:05 2019

@author: rjnp2
"""

#importing all neccessary packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from keras.models import load_model

#loading model and test_data 
model_histroy_load = np.load('./model/model_histroy.npy',allow_pickle = True)
model = load_model('./model/my_model.h5')
test_data_load = np.load('./image_array_data/test_data.npy' ,allow_pickle = True)

animal = [ 'cat','dog','monkey','cow','elephant','horse','squirrel','chicken',
           'spider','sheep']

def testing():
    
    img_size = 200
    test_data = []
    test_label = []
    
    for data in test_data_load:
       test_data.append(data[0])
       test_label.append(data[1])

    test_data = np.array(test_data).reshape(-1, img_size, img_size , 1).astype('float32')
    test_data /= 255      
    
    x = model.predict(test_data)
    x = np.argmax(x,axis = 1)
    cnf_matrix = confusion_matrix(test_label, x)
    cm_df = pd.DataFrame(cnf_matrix,animal,animal)  
    
    return cm_df                    

cm=testing()

train_loss = model_histroy_load[0,:]
val_loss = model_histroy_load[1,:]
train_acc = model_histroy_load[2,:]
val_acc = model_histroy_load[3,:]
epochs = model_histroy_load[4,:]
 

#plotting training and validation loss
plt.plot(epochs, train_loss, color='red',linewidth=4, label='Training loss')
plt.plot(epochs, val_loss, color='green', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

#plotting training and validation accuracy
plt.plot(epochs, train_acc, color='red',linewidth=4, label='Training acc')
plt.plot(epochs, val_acc, color='green', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

#plotting training Loss and accuracy
plt.plot(epochs, train_acc, color='red', label='Training acc')
plt.plot(epochs, train_loss, color='green', label='Training loss')
plt.title('Training accuracy and loss')
plt.xlabel('Epochs')
plt.ylabel('Loss and accuracy')
plt.legend()
plt.show()

#plotting Validation Loss and accuracy
plt.plot(epochs, val_acc, color='red', label='Validation acc')
plt.plot(epochs, val_loss, color='green', label='Validation loss')
plt.title('Validation accuracy and loss')
plt.xlabel('Epochs')
plt.ylabel('Loss and accuracy')
plt.legend()
plt.show()
