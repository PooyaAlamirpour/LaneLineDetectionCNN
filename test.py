import os
from os import listdir
from os.path import isfile, join
import glob
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
from Dataset import *

print('=============================================================')
dataset = Dataset()
train_X, train_Y = dataset.Load()

print(train_X[0])

print('=============================================================')