import csv
from ultralytics import YOLO
import cv2
import numpy as np
from norfair import Detection, Tracker

def yolo_to_norfair(results, conf_threshold=0.4):
    detections = []
    boxes = results[0].boxes.data.cpu().numpy()
    for box in boxes:
        x1, y1, x2, y2, conf, cls = box
        if conf < conf_threshold or int(cls) != 2:
            continue
        center = np.array([(x1 + x2) / 2, (y1 + y2) / 2])
        detections.append(Detection(points=center))
    return detections

model = YOLO("best.pt")
tracker = Tracker(distance_function="euclidean", distance_threshold=30)
cap = cv2.VideoCapture("broadcast.mp4")

csv_file = open("broadcast_tracking.csv", mode='w', newline='')
writer = csv.writer(csv_file)
writer.writerow(["frame", "id", "x", "y"])

frame_num = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    detections = yolo_to_norfair(results)
    tracked_objects = tracker.update(detections)

    for obj in tracked_objects:
        x, y = obj.estimate[0]
        writer.writerow([frame_num, obj.id, int(x), int(y)])
        cv2.circle(frame, (int(x), int(y)), 6, (0, 255, 0), -1)
        cv2.putText(frame, f"ID {obj.id}", (int(x), int(y) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Broadcast Tracking + CSV", frame)
    if cv2.getWindowProperty("Broadcast Tracking + CSV", cv2.WND_PROP_VISIBLE) < 1:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    frame_num += 1

cap.release()
csv_file.close()
cv2.destroyAllWindows()
