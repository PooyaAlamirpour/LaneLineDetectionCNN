import os
from os import listdir
from os.path import isfile, join
import matplotlib.image as mpimg
import numpy as np
import cv2
import pandas
import random
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout, Lambda, ELU
from keras.activations import relu, softmax
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.utils import plot_model
import math
import glob

print('=============================================================')

def load_dataset():
	print('Loading datasrt...\n')
	
	directory = "D:\\Partition E\\Self Studies\\Self Driving Car\\Datasets\\CULane\\Main\\driver_161_90frame\\"
	paths = [path[0] for path in os.walk(directory)]
	print(len(paths), ' folders found')
	train_X = []
	train_Y = []
	
	for mypath in paths:
		data_path = os.path.join(mypath, '*.jpg')
		files = glob.glob(data_path)
		for img_file in files:
			#img = cv2.imread(img_file)
			train_X.append(img_file)
		
		data_path = os.path.join(mypath, '*.txt')
		files = glob.glob(data_path)
		for txt_file in files:
			#img = cv2.imread(img_file)
			train_Y.append(txt_file)
	
	print('train_X: ', len(train_X))
	print('train_Y: ', len(train_Y))
	print('\nDataset is loaded successfully')
	return train_X, train_Y
	
load_dataset()

print('=============================================================')