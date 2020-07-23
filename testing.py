#import numpy as np
#import cv2
#import pytesseract as tess 
#tess.pytesseract.tesseract_cmd = r'C:\Users\james\AppData\Local\Tesseract-OCR\tesseract'
#from PIL import Image
#img = Image.open('test.png')
#text = tess.image_to_string(img)

#print(text)

#import tesseract command down below
#tess.pytesseract.tesseract_cmd = r'C:\Users\james\AppData\Local\Tesseract-OCR\tesseract'


import cv2
import pytesseract
 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\james\AppData\Local\Tesseract-OCR\tesseract'
 #read in img with file name 
img = cv2.imread('opencv.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 #getting our string 

#print(pytesseract.image_to_string(img))
#detecting characters
#print(pytesseract.image_to_boxes(img))




""" #######Detecting characters 
#take info of image
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
#acquiring the location for every character
for b in boxes.splitlines():
    #split into strings, formatting x, y, length, width 
    b = b.split(' ')

    print(b)

    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    #how our rectangle will look. each will have rectangle
    #subtract y to shorten the amount
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
    #put text around box, b0 is first element of text 
    #putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None
    cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
 """
    #for words

    
 
cv2.imshow('Result',img)
cv2.waitKey(0)