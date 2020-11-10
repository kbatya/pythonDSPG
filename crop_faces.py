from ImgBig import ImgBig,BBX
from os import listdir
import string
import random

import cv2
def resize_images(crop, pathto):
    width = 12
    height = 12
    dim = (width, height)
    resized = cv2.resize(crop, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(pathto, resized)

def crop_bdbox(img, bbx, pathto, pathto12):

    crop = img[bbx.y:bbx.y+bbx.h, bbx.x:bbx.x+bbx.w]
    cv2.imwrite(pathto,crop)
    resize_images(crop,pathto12)

def scan_images(pathfrom, pathto, pathto12, pathtoneg, pathtoneg12, images):
    num_images = len(images)
    numface = 0
    numneg = 0

    for image in images:
        path = pathfrom + "\\" + image.filename
        img = cv2.imread(path)
        
        if image.numfaces > 0:
            if image.numfaces == 1 and numneg < 1000 :
                bbxpos = image.listbbxs[0]
                crop_neg_images(pathtoneg, pathtoneg12, img, bbxpos, numneg)
                numneg+=1
            if numface < 1000:
                for bbx in image.listbbxs:
                    pathcrop = pathto + "\\pos" + str(numface) + ".jpg"
                    pathcrop12 = pathto12 + "\\pos" + str(numface) + ".jpg"
                    crop_bdbox(img, bbx, pathcrop, pathcrop12)
                    numface += 1
                    if numface == 1000:
                        break
        if numface == 1000 and numneg == 1000:
            break

def crop_neg_images(pathtoneg, pathtoneg12, img, bbxpos, numneg):
    imgh, imgw, _ = img.shape
    bbx2=BBX()
    bbx2.random_bbx(imgw,imgh)
    while(intersectBBX(bbxpos,bbx2)):
        bbx2.random_bbx(imgw,imgh)
    pathcrop = pathtoneg + "\\neg" + str(numneg) + ".jpg"
    pathcrop12 = pathtoneg12 + "\\neg" + str(numneg) + ".jpg"
    crop_bdbox(img, bbx2, pathcrop, pathcrop12)

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
