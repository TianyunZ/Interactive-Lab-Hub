
#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import os
import time
from PIL import Image, ImageDraw, ImageFont

import digitalio
import board

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors

# The display uses a communication protocol called SPI.
# SPI will not be covered in depth in this course. 
# you can read more https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")


# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
# Load Labels:
labels=[]
f = open("labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())


display.fill(color565(0, 0, 0))
flg = 0
while(True):
   flg = (flg + 1) % 100
   if webCam:
      ret, img = cap.read()

   rows, cols, channels = img.shape
   data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

   size = (224, 224)
   img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
   #turn the image into a numpy array
   image_array = np.asarray(img)

   # Normalize the image
   normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
   # Load the image into the array
   data[0] = normalized_image_array

   # run the inference
   prediction = model.predict(data)
   if labels[np.argmax(prediction)] == "not":
      # os.system('./speak/nomask.sh')
      display.fill(color565(255, 0, 0)) # set the screen to red
   elif labels[np.argmax(prediction)] == "mask":
      if flg <= 10:
         # os.system('./speak/hello.sh')
         display.fill(color565(0, 255, 0)) # set the screen to green
   else:
      # draw.rectangle((0, 0, width, height), outline=0, fill="#008000")
      # draw.text((x, y), "Hi. Welcome to Pi's restaurant.", font=font, fill="#000000")
      display.fill(color565(255, 255, 255)) # set the screen to white
   print("I think its a:",labels[np.argmax(prediction)])
   # time.sleep(1)

   if webCam:
      if sys.argv[-1] == "noWindow":
         cv2.imwrite('detected_out.jpg',img)
         continue
      cv2.imshow('detected (press q to quit)',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
         cap.release()
         break
   else:
      break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
