#import numpy as np
#import cv2
#import pytesseract as tess 
#tess.pytesseract.tesseract_cmd = r'C:\Users\james\AppData\Local\Tesseract-OCR\tesseract'
#from PIL import Image
#img = Image.open('test.png')
#text = tess.image_to_string(img)

#print(text)

#import cv2
#import pytesseract as tess 
#tess.pytesseract.tesseract_cmd = r'C:\Users\james\AppData\Local\Tesseract-OCR\tesseract'


import cv2
import pytesseract
 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\james\AppData\Local\Tesseract-OCR\tesseract'
img = cv2.imread('opencv.png')
