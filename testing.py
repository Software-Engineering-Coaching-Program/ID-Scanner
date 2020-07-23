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

#take info of image
himg,wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
#acquiring the location for every character
for b in boxes.splitlines():
    print(b)
 
cv2.imshow('Result',img)
cv2.waitKey(0)