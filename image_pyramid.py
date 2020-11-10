from os import listdir
import string
from os.path import isfile, join
import numpy as np
import cv2

from ImgBig import ImgBig
from processtxtfile import *
from crop_faces import *




cwd = r'C:\projectDSPG'
pathfrom = cwd+ r'\WIDER_train\images'
pathto = cwd + r'\positive'
pathto12 = cwd + r'\positive12'
pathtoneg = cwd + r'\negative'
pathtoneg12 = cwd + r'\negative12'

path = cwd + r"\wider_face_split\wider_face_train_bbx_gt.txt"

lines = read_file(path)
images = processing_lines(lines)
print(len(images))
scan_images(pathfrom, pathto, pathto12, pathtoneg, pathtoneg12, images)
processing_files_in_dir(pathfrom, images)