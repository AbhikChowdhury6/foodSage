import cv2
url = "http://192.168.217.212:8080/video"

# Open webcam (0 for default camera)
cap = cv2.VideoCapture(url)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture frame")
        break

    # Display the captured frame
    cv2.imshow("Webcam Feed", frame)

    # Press 'q' to quit the video capture
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
