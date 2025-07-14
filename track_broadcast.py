from ultralytics import YOLO
import cv2
import numpy as np
from norfair import Detection, Tracker

# Convert YOLO detections to Norfair format
def yolo_to_norfair(results, conf_threshold=0.4):
    detections = []
    boxes = results[0].boxes.data.cpu().numpy()

    print(f"\nNumber of detections: {len(boxes)}")  # Debug

    for box in boxes:
        x1, y1, x2, y2, conf, cls = box
        print(f"Box: {x1:.0f},{y1:.0f},{x2:.0f},{y2:.0f} | Conf: {conf:.2f} | Class: {int(cls)}")  # Debug

        if conf < conf_threshold:
            continue

        # Center point for tracking
        center = np.array([(x1 + x2) / 2, (y1 + y2) / 2])
        detections.append(Detection(points=center))
    
    return detections

# Draw IDs on frame
def draw_ids(frame, tracked_objects):
    for obj in tracked_objects:
        x, y = obj.estimate[0]
        cv2.circle(frame, (int(x), int(y)), 6, (0, 255, 0), -1)
        cv2.putText(frame, f"ID {obj.id}", (int(x), int(y) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        print(f"Drawing ID {obj.id} at ({int(x)}, {int(y)})")  # Debug

# Load YOLOv11 model
model = YOLO("best.pt")

# Initialize tracker
tracker = Tracker(distance_function="euclidean", distance_threshold=30)

# Load video
cap = cv2.VideoCapture("broadcast.mp4")

if not cap.isOpened():
    print("❌ Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("✅ End of video or failed to read frame.")
        break

    # Run detection
    results = model(frame)
    detections = yolo_to_norfair(results)
    
    # Update tracker and draw
    tracked_objects = tracker.update(detections)
    draw_ids(frame, tracked_objects)

    # Show frame
    cv2.imshow("Tracking", frame)

    # Exit if 'q' is pressed or window closed
    if cv2.getWindowProperty("Tracking", cv2.WND_PROP_VISIBLE) < 1:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
