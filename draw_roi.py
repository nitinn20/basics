import cv2
import os

# --- Input and Output Folders ---
input_folder = r"C:\Users\NITIN\Desktop\camera4\img"
output_folder = r"C:\Users\NITIN\Desktop\camera4\out"
os.makedirs(output_folder, exist_ok=True)

# --- ROI coordinates ---
rois = {
    # "left":   (222, 500, 609, 1099),
    # "middle": (987, 814, 1814, 1072),
    # "right":  (1981, 740, 2495, 961),
    "box":    (900, 200, 1566, 630)
}

# --- Color and thickness ---
color = (0, 255, 255)  # Yellow (BGR)
thickness = 2

# --- Process all images ---
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_folder, file_name)
        img = cv2.imread(image_path)

        if img is None:
            print(f"Skipping {file_name}: Unable to read image.")
            continue

        # Draw each ROI
        for name, (xmin, ymin, xmax, ymax) in rois.items():
            cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, thickness)
            cv2.putText(img, name, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.6, color, 2, cv2.LINE_AA)

        # Save output image
        output_path = os.path.join(output_folder, file_name)
        cv2.imwrite(output_path, img)
        print(f"Processed: {file_name}")

print("✅ All images processed and saved.")
