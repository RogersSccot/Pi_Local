import numpy as np
import cv2
import math
import matplotlib
import serial
import time
from matplotlib import pyplot as plt
capture=cv2.VideoCapture(0)

def take_photo(photo_name):
    global capture
    photo_name=photo_name+'.jpg'
    _,image=capture.read()
    cv2.imwrite(photo_name,image)
    print('take photo success')

take_photo('123')
