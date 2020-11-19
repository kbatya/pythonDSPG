from ImgBig import ImgBig
import os
from os import listdir
from os.path import isfile, join
def read_file(path):
    f = open(path, 'r+')
    lines = f.readlines()
    f.close()
    return lines

# function that creates list of ImgBig objects
def processing_lines(lines):
    images = []
    curr_ind = 0
    num_lines = len(lines)
    while (curr_ind < num_lines):
        filename = lines[curr_ind][:-1]
        numfaces = int(lines[curr_ind+1][:-1])
        if numfaces > 0:
            curr_ind += 2
            images.append(ImgBig(filename,numfaces,lines[curr_ind:curr_ind+numfaces]))
            curr_ind += numfaces
        else:
            # when number of bounding boxes equal 0
            curr_ind += 3
    return images



