from ultralytics import YOLO
import os

model=YOLO('yolov8m-seg.pt')

model.train(
            data=r'/home/nitin/projects/activity_recognition/c1_dataset/data.yaml',
            epochs=100,  
            batch=32,
            imgsz=640,
            patience=20,
            optimizer='adam',
            lr0=0.0001,
            lrf=0.1,
            save=True,
            device=["4"],
            translate=0.0,
            scale=0.0,
            fliplr=0.0,
            mosaic=0.0,
            erasing=0.0,
            )
