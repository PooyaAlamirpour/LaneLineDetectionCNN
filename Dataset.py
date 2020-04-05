import os
from os import listdir
from os.path import isfile, join
import glob
from Component import *
import cv2

class Dataset:
	def Load(self):
		print('Loading datasrt...\n')
		
		directory = "D:\\Partition E\\Self Studies\\Self Driving Car\\Datasets\\CULane\\Main\\driver_161_90frame\\"
		paths = [path[0] for path in os.walk(directory)]
		print(len(paths), ' folders found')
		train_X = []
		train_Y = []
		comp = Component()
		peogress = 0;
		for mypath in paths:
			comp.ProgressBar(peogress + 1, len(paths), prefix = 'Progress:', suffix = 'Complete', length = 50)
			
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
			
			peogress = peogress + 1
		
		print('\ntrain_X: ', len(train_X))
		print('train_Y: ', len(train_Y))
		print('\nDataset is loaded successfully')
		return train_X, train_Y