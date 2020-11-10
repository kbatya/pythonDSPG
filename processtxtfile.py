from ImgBig import ImgBig
import os
from os import listdir
from os.path import isfile, join
def read_file(path):
    f = open(path, 'r+')
    lines = f.readlines()

    f.close()
    return lines

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
            curr_ind += 3
    return images

def file_in_image_list(images, name):
    for image in images:
        if image.filename == name:
            return True
    return False

def processing_files_in_dir(maindir,images):
        negimages = []
        dirs = os.listdir(maindir)  # read the contents of dir
        for dir in dirs:  # loop over those contents

            listfiles = os.listdir(maindir + '\\' + dir)
            for filename in listfiles:
                fullname = dir +r"/" +filename
                if not file_in_image_list(images,fullname):
                    negimages.append(fullname)
                    if len(negimages)==1000:
                        return negimages
        return negimages
