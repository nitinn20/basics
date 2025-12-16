import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

folder = r"C:\Users\NITIN\Desktop\act\camera5\camera5_hand_dataset\camera5_hand_dataset"
save_dir = "cam5_hand_per_image"
os.makedirs(save_dir, exist_ok=True)

image_files = sorted(os.listdir(folder))

r_means = []
g_means = []
b_means = []

# ---- Compute means per image ----
for img_name in image_files:
    if not img_name.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    img = cv2.imread(os.path.join(folder, img_name))
    if img is None:
        continue

    img = img.astype(np.float32) / 255.0
    b, g, r = cv2.split(img)

    r_means.append(np.mean(r))
    g_means.append(np.mean(g))
    b_means.append(np.mean(b))

# X = Image indexes
x = np.arange(len(r_means))

# ----------------------------------------
# RED HISTOGRAM 
# ----------------------------------------
plt.figure(figsize=(14,4))
plt.bar(x, r_means, color='red')
plt.title("Red Mean per Image")
plt.xlabel("Image Index")
plt.ylabel("Mean Red (0–1)")
plt.tight_layout()
plt.savefig(os.path.join(save_dir, "red_mean_bar.png"), dpi=300)
plt.close()

# ----------------------------------------
# GREEN HISTOGRAM 
# ----------------------------------------
plt.figure(figsize=(14,4))
plt.bar(x, g_means, color='green')
plt.title("Green Mean per Image")
plt.xlabel("Image Index")
plt.ylabel("Mean Green (0–1)")
plt.tight_layout()
plt.savefig(os.path.join(save_dir, "green_mean_bar.png"), dpi=300)
plt.close()

# ----------------------------------------
# BLUE HISTOGRAM 
# ----------------------------------------
plt.figure(figsize=(14,4))
plt.bar(x, b_means, color='blue')
plt.title("Blue Mean per Image")
plt.xlabel("Image Index")
plt.ylabel("Mean Blue (0–1)")
plt.tight_layout()
plt.savefig(os.path.join(save_dir, "blue_mean_bar.png"), dpi=300)
plt.close()

print("Graphs saved in:", os.path.abspath(save_dir))
