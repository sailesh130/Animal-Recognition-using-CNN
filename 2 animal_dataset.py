#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:51:10 2019

@author: rjnp2
"""
#importing OS module/packages to work with system.
import os
#importing opencv packages to work with images
import cv2
import matplotlib.pyplot as plt

#initiated path variable with datasets locations. 
path = '/home/rjnp2/minorproject/cnn_200/raw-img'

#initiated list variable for storing animal_name, total number , resolution and format of data images. 
animal = list()
total_number = list()
resolution = list()
form = list()

def dataset():
    '''
    It deals with reading images,
    find it's shapes, formats
    and appending into list
    '''

    for i in os.listdir(path):
        
        animal.append(i)
        img1 = os.path.join(path,i)
        width = set()
        height = set()
        formats = set()
        k = 0        
        for j in os.listdir(img1):
            
            word = j.split('.')[-1]
            img_dir = os.path.join(img1,j)
      
            img = cv2.imread(img_dir)
            shape = img.shape[:2]
            
            width.add(shape[0])
            height.add(shape[1])
            formats.add(word)
            k = k+1
        form.append(list(formats))
        total_number.append(k)
        resolution.append([(min(width),max(width)),(min(height),max(height))])


def plot_bar():

    #this is for plotting purpose
    index = range(len(animal))
    plt.bar(index,total_number)
    plt.xlabel('Animal name', fontsize=15)
    plt.ylabel('No of Animal', fontsize=15)
    plt.xticks(index, animal, fontsize=12, rotation=30)
    plt.title('Total nos of animals')
    plt.show()

if __name__ == "__main__":
    dataset()
    print("Animal \t total_number \t resoultion \t format")   
    print('-' * 80)
    for i in range(10):
        print(animal[i],'\t' ,total_number[i],'\t',resolution[i],'\t',form[i])
        print('-' * 80)
         
    plot_bar()  
