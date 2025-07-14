from ultralytics import YOLO
import cv2
import numpy as np
from norfair import Detection, Tracker

def yolo_to_norfair(results, conf_threshold=0.4):
    detections = []
    boxes = results[0].boxes.data.cpu().numpy()

    for box in boxes:
        x1, y1, x2, y2, conf, cls = box
        if conf < conf_threshold or int(cls) != 2:  # Class 2 = player
            continue
        center = np.array([(x1 + x2) / 2, (y1 + y2) / 2])
        detections.append(Detection(points=center))
    return detections

def draw_ids(frame, tracked_objects):
    for obj in tracked_objects:
        x, y = obj.estimate[0]
        cv2.circle(frame, (int(x), int(y)), 6, (255, 0, 0), -1)
        cv2.putText(frame, f"ID {obj.id}", (int(x), int(y) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

model = YOLO("best.pt")
tracker = Tracker(distance_function="euclidean", distance_threshold=30)

cap = cv2.VideoCapture("tacticam.mp4")

if not cap.isOpened():
    print("❌ Could not open tacticam.mp4")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("✅ Finished processing tacticam.mp4")
        break

    results = model(frame)
    detections = yolo_to_norfair(results)
    
    tracked_objects = tracker.update(detections)
    draw_ids(frame, tracked_objects)

    cv2.imshow("Tacticam Tracking", frame)

    if cv2.getWindowProperty("Tacticam Tracking", cv2.WND_PROP_VISIBLE) < 1:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
