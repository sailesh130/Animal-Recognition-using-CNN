#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 17:02:46 2019

@author: rjn
"""

import cv2                   # working with mainly reading, convert to grayscale, resizing images
import numpy as np           # dealing with arrays
import os                    # dealing with directories

#path of animals datasets
train_dir = '/home/rjnp2/minorproject/dataset/train_data'
test_dir = '/home/rjnp2/minorproject/dataset/test_data'

# image size for resizing the images i.e 200 * 200
img_size = 200

class CreateTrain:
    
    def __init__(self,train_dir,test_dir,img_size):
        
        self.train_dir = train_dir
        self.test_dir = test_dir
        self.img_size = img_size
        
        self.animal = {
            'cat' : 0,
            'dog' : 1,
            'monkey' : 2,
            'cow' : 3,
            'elephant' : 4,
            'horse' : 5,
            'squirrel' : 6,
             'chicken' : 7,
            'spider'  : 8,
             'sheep': 9
            }

    def create_train_data(self):
        """
        It mainly deals with reading gray images of size 200 * 200 from path,
        shuffle it and save as train_data.npy 
        for future used of image array without 
        pre-processing it again and again.
        """
        
        #stores arrays of all training images
        training_data = []
        for dir_name in os.listdir(self.train_dir):
            img_dir = os.path.join(self.train_dir, dir_name)
            label = self.animal[dir_name]
        
            for img in os.listdir(img_dir):
                path = os.path.join(img_dir,img)
                try:
                    #try to catch any formats that is not suitable for reading and converting in opencv
                    img = cv2.imread(path)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    img = cv2.resize(img, (int(self.img_size),int(self.img_size)))
                    training_data.append([np.array(img),label])
                except:
                    # catch any errors and dsplay no
                    print('Not on proper formats')
        
        training_data = np.array(training_data)  
        np.random.shuffle(training_data)                
        np.save('train_data.npy', training_data)  
        
        print("sucessfully completed ")


    def create_test_data(self):
        """
        same as create_train_data() function
        but for test images
        """
        
        #stores arrays of all testing images
        test_data = []
        
        for dir_name in os.listdir(self.test_dir):
            img_dir = os.path.join(self.test_dir, dir_name)
            label = self.animal[dir_name]
    
            for img in os.listdir(img_dir):
                path = os.path.join(img_dir,img)
                try:
                    img = cv2.imread(path)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    img = cv2.resize(img, (int(self.img_size),int(self.img_size)))
                    test_data.append([np.array(img),label])
                    
                except:
                    # catch any errors and dsplay no
                    print('Not on proper formats')
                
        test_data = np.array(test_data)
        np.random.shuffle(test_data)                
        np.save('test_data.npy', test_data)
        print("sucessfully completed ")

if __name__ == "__main__":
    create_train = CreateTrain(train_dir = train_dir ,test_dir = test_dir,img_size = img_size) 
    create_train.create_train_data()
    create_train.create_test_data()
