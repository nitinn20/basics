import cv2 
import os 


img=cv2.imread(r"C:\Users\NITIN\Desktop\act\camera5\frame_20251125_124050_673971 (1).jpg")
crop_img=img[136:806, 1085:1805]

cv2.imwrite("Cropped Image.jpg", crop_img)

