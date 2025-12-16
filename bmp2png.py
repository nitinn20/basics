import cv2
import os

# === Paths ===
input_folder = r"C:\Users\NITIN\Desktop\Rock\gear test images"      # folder with BMP images
output_folder = "converted"      # folder to save PNG/JPG images
output_format = "png"            # "png" or "jpg"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# === List all BMP images ===
bmp_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".bmp")]

# === Convert and save each image ===
for file_name in bmp_files:
    bmp_path = os.path.join(input_folder, file_name)
    img = cv2.imread(bmp_path)

    if img is None:
        print(f"Failed to read {file_name}")
        continue

    # Create new file name with desired extension
    base_name = os.path.splitext(file_name)[0]
    save_path = os.path.join(output_folder, f"{base_name}.{output_format}")

    # Save image in new format
    cv2.imwrite(save_path, img)
    print(f"Converted {file_name} -> {save_path}")
