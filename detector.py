# Created by Garvit Kothari at 16-11-2019
# Project Name : malaria-detection

# Library Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
import os

positive_imgs = []
negative_imgs = []

def data_load():
    print("Loading Data...")
    for i in os.listdir('Parasitized'):
        positive_imgs.append(cv2.imread('Parasitized/'+i))

    for i in os.listdir('Uninfected'):
        positive_imgs.append(cv2.imread('Uninfected/'+i))

if __name__ == '__main__':
