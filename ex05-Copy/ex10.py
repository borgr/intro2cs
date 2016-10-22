#############################################################
# FILE : AlignDNA.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex4 200132014
# DESCRIPTION:DNA****
# 
#############################################################
#!/usr/bin/env python3

from PIL import Image

def minmax(self):
    if type(self.getpixel((0,0))) == int:
        mn = 255
        mx = 0
    else:
        mn = [255 for rgb in self.getpixel((0,0))]
        mx = [0 for rgc in  self.getpixel((0,0))]
    for row in range(self.size[0]):
        for col in range(self.size[1]):
            check = self.getpixel((row,col))
            if type(mn) == int:
                    if mn > check:
                        mn = check
                    if mx < check:
                        mx = check
            else:
                for rgb in range(3):
                    if mn[rgb] > check[rgb]:
                        mn[rgb] = check[rgb]
                    if mx[rgb] < check[rgb]:
                        mx[rgb] = check[rgb]
    return(mn,mx)
            
def change(image, func):
##    print(image.size, image.getpixel((0,0)))
    for row in range(image.size[0]):
        for col in range(image.size[1]):
##            print(image.getpixel((row,col)))
            pixl = image.getpixel((row,col))
            if type(pixl) == int:
                pixl = [pixl]
##                print("rgb,b",[(rgb,b)  for rgb, b in enumerate(pixl)])
                putty = list(func(pixl))[0]
            else:
                putty = tuple(func(pixl))
##            print("puttty",putty)
            image.putpixel((row,col), putty)
            
class ExtendedImage(object):        
    def __init__(self,img):
        self._img=img
    def __getattr__(self,key):
        if key == '_img':
            raise AttributeError()
        return getattr(self._img,key)

    def adjust_brightness(self, levels):
        L = levels
        change(self, lambda pixel:(b*L//256*255//(L-1) for b in pixel))
        #modifies self, returns None

    def expand_range(self):
##        print(self.size, self.getpixel((0,0)))
        if type(self.getpixel((0,0))) == int:
            mn = [255]
            mx = [0]
        else:
            mn = [255 for rgb in self.getpixel((0,0))]
            mx = [0 for rgc in  self.getpixel((0,0))]
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                check = self.getpixel((row,col))
                if len(mn) == 1:
                        if mn[0] > check:
                            mn[0] = check
                        if mx[0] < check:
                            mx[0] = check
                else:
                    for rgb in range(3):
                        if mn[rgb] > check[rgb]:
                            mn[rgb] = check[rgb]
                        if mx[rgb] < check[rgb]:
                            mx[rgb] = check[rgb]
        if mn != mx:
            change(self, lambda pixel:(int((b-mn[rgb])*(256//(mx[rgb]-mn[rgb]))) if mx[rgb]!= mn[rgb] else b for rgb, b in enumerate(pixel) ))
        #modifies self, returns None

    def range_reduction(self, factor):
        new = ExtendedImage(self.copy())
        change(new, lambda pixel: (b//factor*factor for b in pixel))
        return new
        #returns new ExtendedImage, self not modified

    def waterfall(self):
        new = ExtendedImage(self.copy())
        for row in range(1, new.size[0]):
            for col in range(1, new.size[1]):
                putty = new.getpixel((row,col))
                up = self.getpixel((row,col-1))
                if type(putty) == int:
                    putty = (putty-up)%255
                    new.putpixel((row,col), putty)
                else:
                    putty = ((b-a)%255 for a,b in zip(up,putty))
                    new.putpixel((row,col), tuple(putty))
        return new
        #returns new ExtendedImage, self not modified

    def waterfall_restore(self):
        new = ExtendedImage(self.copy())
        for row in range(1, new.size[0]):
            for col in range(1, new.size[1]):
                putty = new.getpixel((row,col))
                up = new.getpixel((row,col-1))
                if type(putty) == int:
                    putty = (putty+up)%255
                    new.putpixel((row,col), putty)
                else:
                    putty = ((b+a)%255 for a,b in zip(up,putty))
                    new.putpixel((row,col), tuple(putty))
        return new
        #returns new ExtendedImage, self not modified

    def wavelet(self):
        '''Your code here'''
        #returns new ExtendedImage, self not modified

    def wavelet_restore(self):
        '''Your code here'''
        #returns new ExtendedImage, self not modified
