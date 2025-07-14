from ultralytics import YOLO
import cv2

# Load YOLOv11 model
model = YOLO("best.pt")

# Load video
cap = cv2.VideoCapture("broadcast.mp4")

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error opening video file.")
    exit()

while True:
    ret, frame = cap.read()

    # If no frame is returned, break the loop
    if not ret:
        break

    # Run detection
    results = model(frame)
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("Detections", annotated_frame)

    # Break if 'q' is pressed or window is closed
    if cv2.getWindowProperty("Detections", cv2.WND_PROP_VISIBLE) < 1:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
