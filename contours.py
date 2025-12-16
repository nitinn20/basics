import cv2
import numpy as np
import matplotlib.pyplot as plt 

def load_image(image_path):
    image=cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at path {image_path} could not be loaded.")
    return image

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh

def find_contours(thresh):
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image, contours):
    contour_img = image.copy()
    contour_img = cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 3)
    return contour_img

def display_images(image,contour_img):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("original image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 2, 2)
    plt.title("contoured image")
    plt.imshow(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))
    plt.show()


if __name__ == "__main__":
    image_path= "22.jpeg"
    image= load_image(image_path)
    thresh= preprocess_image(image)
    contours= find_contours(thresh)
    contour_img= draw_contours(image, contours)
    display_images(image, contour_img)