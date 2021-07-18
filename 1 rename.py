#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:52:00 2019

@author: rjn
"""
#importing OS module/packages to work with system.
import os 

#initiated path variable with datasets locations. 
path="/home/rjnp2/minorproject/dataset/train_data"

#list out all animals names
animals_list = [
               'cat',
               'cow',
               'monkey',
               'dog',
               'elephant',
               'horse',
               'chicken',
               'squirrel',
               'spider',
               'sheep'
              ]


for animal in animals_list:    #loop through each of animal in animals_list
    i=1
    animal_path = os.path.join(path, animal)  #join the path and animals i.e /home/rjn/project/dataset/ + cats
    print(animal_path)

    for filename in os.listdir(animal_path):  #loop through each images of animals
          img_format = filename.split('.')[-1]
          
          my_dest = animal  + '.' + str(i) + '.' + img_format
          my_source = animal_path + '/' + filename
          my_dest = animal_path + '/' + my_dest

          # rename() function will
          # rename all the files with my_dest name
          os.rename(my_source, my_dest)     
          i += 1
