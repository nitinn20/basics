import cv2 
import os 
from ultralytics import YOLO

rtsp_url="rtsp://admin:Indusvision-2025@192.168.16.22:554"

model_path = r""
model=YOLO(model_path)

roi=(400,0,2688,1520)

cap=cv2.VideoCapture(rtsp_url)
if not cap.isOpened():
    print("Error opening the stream")
    exit()

while True:
    ret, frame=cap.read()
    if not ret:
        print("Error reading the frame")
        break
    x1_r, y1_r, x2_r, y2_r = roi
    roi_frame=frame[y1_r:y2_r, x1_r:x2_r]
    results=model(roi_frame, conf=0.5, iou=0.45, verbose=False)
    for result in results:
        for box in result.boxes:
            x1,y1,x2,y2=map(int, box.xyxy[0])
            conf=float(box.conf[0])
            cls=int(box.cls[0])
            name=model.names[cls]
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, f"{name} {conf:.2f}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
            cv2.imshow("RTSP YOLO Detection", frame)

cap.release()
cv2.destroyAllWindows()