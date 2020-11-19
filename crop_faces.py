from ImgBig import ImgBig,BBX
from os import listdir
import string
import random

import cv2
# funcion rescales the cropped image from bounding box to 12x12
def resize_images(crop, pathto):
    width = 12
    height = 12
    dim = (width, height)
    resized = cv2.resize(crop, dim, interpolation = cv2.INTER_AREA)
    # writes image 12x12 file
    cv2.imwrite(pathto, resized)

# function crops bounding box from the image by coordinates
def crop_bdbox(img, bbx, pathto, pathto12):

    crop = img[bbx.y:bbx.y+bbx.h, bbx.x:bbx.x+bbx.w]
    # write cropped image as bounding box
    cv2.imwrite(pathto,crop)
    resize_images(crop,pathto12)

# function scans images objects list, read image and crops negative and positve samples
def scan_images(pathfrom, pathto, pathto12, pathtoneg, pathtoneg12, images):
    num_images = len(images)
    # counter of positive samples - maximum 1000
    numface = 0
    # counter of negative samples - maximum 1000
    numneg = 0


    for image in images:
        path = pathfrom + "\\" + image.filename
        img = cv2.imread(path)
        
        if image.numfaces > 0:
            # if the image with only one face bounding box it creates bounding box without face
            if image.numfaces == 1 and numneg < 1000 :
                bbxpos = image.listbbxs[0]
                crop_neg_images(pathtoneg, pathtoneg12, img, bbxpos, numneg)
                numneg+=1
            if numface < 1000:
                # scans list of bounding boxes in the images
                for bbx in image.listbbxs:
                    pathcrop = pathto + "\\pos" + str(numface) + ".jpg"
                    pathcrop12 = pathto12 + "\\pos" + str(numface) + ".jpg"
                    crop_bdbox(img, bbx, pathcrop, pathcrop12)
                    numface += 1
                    if numface == 1000:
                        break
        if numface == 1000 and numneg == 1000:
            break

# function creates negative sample bounding box with random size
def crop_neg_images(pathtoneg, pathtoneg12, img, bbxpos, numneg):
    imgh, imgw, _ = img.shape
    bbx2=BBX()
    bbx2.random_bbx(imgw,imgh)
    # while random bounding box and bounding box of face in the image have the same pixels
    while(intersectBBX(bbxpos,bbx2)):
        bbx2.random_bbx(imgw,imgh)
    pathcrop = pathtoneg + "\\neg" + str(numneg) + ".jpg"
    pathcrop12 = pathtoneg12 + "\\neg" + str(numneg) + ".jpg"
    crop_bdbox(img, bbx2, pathcrop, pathcrop12)

# function checks 2 bounding boxes have common pixels
def intersectBBX(bbx1,bbx2):
    if bbx1.x + bbx1.w < bbx2.x:
        return False
    if bbx1.y + bbx1.h < bbx2.y:
        return False
    if bbx2.x + bbx2.w < bbx1.x:
        return False
    if bbx2.y + bbx2.h < bbx1.y:
        return False
    return True
