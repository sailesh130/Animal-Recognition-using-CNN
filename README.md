# Animal-Recognition-using-CNN
Animal recognition is one major and important field in object detection.

Goal is to identifying the animal in the picture
Uses Deep Learning techniques with convolutional neural network
Uses large labeled datasets to train the model for solving problem of  animal identification in the images

i used Kaggle Animal-10 and Cifar cifar-10 
Kaggle Animal-10 dataset consists of 20000 color images in 10 classes
Cifar cifar-10 there are about 1500 images 
The dataset classes consist of elegant, deer, cow, sheep, dogs, cat, horse, monkey, frog, spider 
there are total  25000 images as dataset


For run this code,
we should have following package

    1.python3
    2.numpy
    3.opencv
    4.keras
    5.sklearn
    6.matplotlib

1. open rename.py \
    To rename images name according to folder if you want.
    it collectly optional or not required
    you need to change below path with your image directory
    
    
    #initiated path variable with datasets locations. 
    path= 'datasets path'
    
2. image_to_array.py
    Pre-processing step
    convert an image into n-dim array for performing some operations such matrix multiplication and addition on it.
    It helps to extract meaningful information from images. 
    Such as whether a certain object is present or not in a particular scene.
    
    First load all images in arrays: training data and test data with their labels and then reshape
    into 200 * 200 size. The array size is N * 200 *200 *1 hold gray images in training data
    and their corresponding N size of array hold the labels training labels from 0 to 9 . Here N
    is no of images (N =2500).
    
    change train_dir and test_dir of animals datasets with yours.
    
    saved train images as train_data_200.npy so that pre-processing of image shouldn’t be done again and again.
    
    
3.  training_cnn.py
    change cnn architecture as u wish
    
4.  after tranning, add the trained model to model folder.

5. change the model name in animal_prediction.py

6. Run DesktopGUI.py and enjoy the application.
