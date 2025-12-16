import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

folder = r"C:\Users\NITIN\Desktop\act\camera5\camera5_hand_dataset\camera5_hand_dataset"
save_dir = "cam5_hand_bins_100"
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

# Convert to numpy
r_means = np.array(r_means)
g_means = np.array(g_means)
b_means = np.array(b_means)

# Binning
bin_size = 100
num_bins = len(r_means) // bin_size  

def create_bins(arr, bin_size):
    return np.array([np.mean(arr[i:i+bin_size]) for i in range(0, len(arr), bin_size)])

r_bins = create_bins(r_means, bin_size)
g_bins = create_bins(g_means, bin_size)
b_bins = create_bins(b_means, bin_size)

x_bins = np.arange(len(r_bins))  

# ----------------------------------------
# RED BIN HISTOGRAM
# ----------------------------------------
plt.figure(figsize=(14,4))
plt.bar(x_bins, r_bins, color='red')
plt.title("Red Mean Histogram (1bin=100 images)")
plt.xlabel("Bin Number")
plt.ylabel("Mean Red (0–1)")
plt.tight_layout()
plt.savefig(os.path.join(save_dir, "red_bins.png"), dpi=300)
plt.close()

# ----------------------------------------
# GREEN BIN HISTOGRAM
# ----------------------------------------
plt.figure(figsize=(14,4))
plt.bar(x_bins, g_bins, color='green')
plt.title("Green Mean Histogram (1bin= 100 images)")
plt.xlabel("Bin Number")
plt.ylabel("Mean Green (0–1)")
plt.tight_layout()
plt.savefig(os.path.join(save_dir, "green_bins.png"), dpi=300)
plt.close()

# ----------------------------------------
# BLUE BIN HISTOGRAM
# ----------------------------------------
plt.figure(figsize=(14,4))
plt.bar(x_bins, b_bins, color='blue')
plt.title("Blue Mean Histogram (1bin= 100 images)")
plt.xlabel("Bin Number")
plt.ylabel("Mean Blue (0–1)")
plt.tight_layout()
plt.savefig(os.path.join(save_dir, "blue_bins.png"), dpi=300)
plt.close()

print("Graphs saved in:", os.path.abspath(save_dir))
