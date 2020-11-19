# created by Batya Koltun in 11/11/2020
# the program that prepares 1000 pictures 12x12  for positive result faces
# and 1000 with negative result pictures using WIDER Face Training Images
#

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
# #directory with positive samples
pathto = cwd + r'\positive'
#directory with positive samples 12x12
pathto12 = cwd + r'\positive12'
#directory with negarive samples
pathtoneg = cwd + r'\negative'
#directory with negative samples 12x12
pathtoneg12 = cwd + r'\negative12'
# file with
# The format of txt ground truth.
# image File name
# 0--Parade/0_Parade_marchingband_1_849.jpg
# Number of bounding boxes
# 1
# x1,  y1, w,  h, blur, expression, illumination, invalid, occlusion, pose
# 449 330 122 149 0 0 0 0 0 0
path = cwd + r"\wider_face_split\wider_face_train_bbx_gt.txt"


lines = read_file(path)
images = processing_lines(lines)
print(len(images))
scan_images(pathfrom, pathto, pathto12, pathtoneg, pathtoneg12, images)
processing_files_in_dir(pathfrom, images)