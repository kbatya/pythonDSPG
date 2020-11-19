import random
# Class for bounding box
class BBX:
    # constractor adds random pixel lines between 1 to 3 to all 4 sides of bounding box
    def __init__(self,x=0,y=0,w=50,h=50):

        self.x = int(x) - random.randint(1,3)
        if self.x < 0 :
            self.x = 0
        self.y = int(y) - random.randint(1,3)
        if self.y < 0:
            self.y = 0
        self.w = int(w) + random.randint(1,3)
        self.h = int(h) + random.randint(1,3)

    # the method creates random bounding box with high and width between 50 to 150
    def random_bbx(self, imgw, imgh):
        self.h = random.randint(50, 150)
        self.w = random.randint(50, 150)
        self.x = random.randint(0, imgw - self.w)
        self.y = random.randint(0, imgh - self.h)

# Class of image with list of bounding boxes as number of faces in the image
class ImgBig:

    def __init__(self,filename,numfaces,lines=[]):
        self.filename = filename
        self.numfaces = numfaces
        if self.numfaces > 0:
            self.listbbxs = self.create_list_bbxs(lines)

    def create_list_bbxs(self,lines):
        listbbxs = []
        for face in lines:
            splline = face.split()
            # when not invalid image
            if splline[7]!='1':
                listbbxs.append(BBX(splline[0],splline[1],splline[2],splline[3]))
        return  listbbxs