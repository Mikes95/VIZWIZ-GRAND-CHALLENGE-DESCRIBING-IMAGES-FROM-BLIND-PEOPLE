import json
from pprint import pprint
import cv2
import pytesseract
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib import cm
import numpy as np
from pytesseract import Output
from googlesearch import search 
import requests
from bs4 import BeautifulSoup


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def apply_brightness_contrast(input_img, brightness = 0, contrast = 0):

    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131*(contrast + 127)/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
dataset_path='D:\\Download_HardDisk\\Dataset-VIZWIZ GRAND CHALLENGE\\val'

image = cv2.imread(dataset_path+'\\VizWiz_val_'+str(0).zfill(8)+'.jpg')

gray = get_grayscale(image)
thresh = thresholding(gray)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(gray,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
brightness_contrast= apply_brightness_contrast(gray,-100,80)

fig=plt.figure(figsize=(25, 25))
fig.add_subplot(3, 3, 1)
plt.title('gray')
plt.imshow(gray, cmap=cm.gray, vmin=0, vmax=255)
fig.add_subplot(3, 3, 2)
plt.title('thresholding')
plt.imshow(thresh, cmap=cm.gray, vmin=0, vmax=255)
fig.add_subplot(3, 3, 3)
plt.title('apply_brightness_contrast')
plt.imshow(brightness_contrast, cmap=cm.gray, vmin=0, vmax=255)


custom_config = r'--oem 3 --psm 6'
#text= pytesseract.image_to_string(gray, config=custom_config)
#d = pytesseract.image_to_data(gray, output_type=Output.DICT)
#print(text+'\n')


text= pytesseract.image_to_string(brightness_contrast, config=custom_config)
d = pytesseract.image_to_data(brightness_contrast, output_type=Output.DICT)
print(text)


n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
#cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#cv2.resizeWindow('image', 600,600)
figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
#plt.title('Esempio di immagine',fontsize=24, y=1)
plt.imshow(img, cmap=cm.gray, vmin=0, vmax=255)
plt.show()




# to search 
query = text
url=list(search(query, tld="co.in", num=10, stop=1, pause=2))
for j in url: 
    print(j) 

req = requests.get(url[0], 'html.parser')
#print(req.text)
soup = BeautifulSoup(req.text, 'html.parser')
title = soup.find('title')
print(title)