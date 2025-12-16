import cv2
import os

input_folder=r"C:\Users\NITIN\Desktop\camera4\img"
output_folder=r"C:\Users\NITIN\Desktop\camera4\output2"

os.makedirs(output_folder, exist_ok=True)

#-----ROI-------
roi= { "box": (936,189,1565,603),
       "left":(222,500,609,1099),
       "middle":(987,814,1814,1072),
       "right":(1981,740,2495,961)
      }

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(('.png','.jpg','jpeg')):
        image_path=os.path.join(input_folder,file_name)
        img=cv2.imread(image_path)

        if img is None:
            print(f"Skipping {file_name}: Unable to load image.")
            continue

        #Crop ROI
        for name, (xmin, ymin, xmax, ymax) in roi.items():
            roi_img=img[ymin:ymax, xmin:xmax]

            crop_path=os.path.join(output_folder,f"{os.path.splitext(file_name)[0]}_{name}.jpg") #remove {name} if dont want the roi name with images saved
            cv2.imwrite(crop_path, roi_img)

print("All images processed and saved")            
