import cv2
import os
import time

# ---------------- CONFIG ----------------
rtsp_url = "rtsp://admin:Indusvision-2025@192.168.16.24:554"
output_dir = "recorded_videos"
os.makedirs(output_dir, exist_ok=True)

timestamp = time.strftime("%Y%m%d_%H%M%S")
output_path = os.path.join(output_dir, f"rtsp_record_{timestamp}.mp4")
# ---------------------------------------


cap = cv2.VideoCapture(rtsp_url)
if not cap.isOpened():
    print("Error: Could not open RTSP stream")
    exit()

# Read one frame to get resolution
ret, frame = cap.read()
if not ret:
    print("Error: Could not read initial frame")
    cap.release()
    exit()

height, width = frame.shape[:2]

# Try to get FPS from stream, fallback if invalid
fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0 or fps > 60:
    fps = 25.0  # safe default

print(f"Saving video at {width}x{height} @ {fps} FPS")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

print("Recording started. Press 'q' to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame read failed, stopping...")
        break

    # ---------------- SAVE ORIGINAL FRAME ----------------
    out.write(frame)

    # ---------------- DISPLAY (resized only for monitoring) ----------------
    display_frame = cv2.resize(frame, (960, 540)) 
    cv2.imshow("RTSP Monitor", display_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Stopped by user")
        break

# ---------------- CLEANUP ----------------
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video saved to: {output_path}")
