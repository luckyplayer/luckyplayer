from PIL import Image
import numpy

import matplotlib.pyplot as plt

def subimg(img1,img2):
    
    #print img1
    #print img2
    
    #img1 = img1.convert('1')
    #img2 = img2.convert('1')
    
    #plt.figure()
    #plt.imshow(img1, interpolation="nearest")
    #plt.show()
    
    #plt.figure()
    #plt.imshow(img2, interpolation="nearest")
    #plt.show()
    
    print img1.convert('RGB')
    print img2.convert('RGB')
    
    img1 = numpy.asarray(img1)
    img2 = numpy.asarray(img2)

    print img1
    print img2

    #img1=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
    #img2=numpy.array([[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]])

    #print dir(img1)
    #print dir(img2)

    #print img1.size

    img1_ysize = img1.shape[0]
    img1_xsize = img1.shape[1]

    img2_ysize = img2.shape[0]
    img2_xsize = img2.shape[1]

    lasty = img2_ysize - img1_ysize
    lastx = img2_ysize - img1_xsize
    
    for x1 in range(0, lastx + 1):
        for y1 in range(0,lasty + 1):
            
            x2 = x1 + img1_xsize
            y2 = y1 + img1_ysize

            pic = img2[y1:y2,x1:x2]
            
            #print pic
            #print img1
            
            test = pic == img1
            
            #print test

            if test.all():
                
                #img2_copy = img2.copy()
                
                #img2_copy[y1-1,x1-1] = [255, 0, 0, 255]
                #img2_copy[y1-1,x2] = [255, 0, 0, 255]
                #img2_copy[y2,x1-1] = [255, 0, 0, 255]
                #img2_copy[y2,x2] = [255, 0, 0, 255]
                
                #plt.figure()
                #plt.imshow(img2_copy, interpolation="nearest")
                #plt.show()
                
                #plt.figure()
                #plt.imshow(pic, interpolation="nearest")
                #plt.show()
                
                return x1, y1

    return False

small = Image.open('piekenegen.png')
big = Image.open('tafeltje.png')

print subimg(small, big)
