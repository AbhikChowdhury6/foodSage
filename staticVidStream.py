import cv2
import easyocr
import time

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

location = "PXL_20250215_212946417.mp4"

# Open webcam (0 for default camera)
cap = cv2.VideoCapture(location)

# Get video frame properties (e.g., frame width, height, and FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object to save output
output_video_path = 'output_video.mp4'  # Replace with your output video path
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

frameCount = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit if frame is not captured
    frameCount += 1
    # Perform OCR
    results = reader.readtext(frame)

    # Draw bounding boxes on detected words
    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))

        # Draw bounding box
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

        # Display recognized text
        cv2.putText(frame, text, (top_left[0], top_left[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    out.write(frame)
    print(frameCount)
    # Show the frame
    #cv2.imshow("Webcam OCR", frame)

    # Press 'q' to exit
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

    #time.sleep(10)

# Release resources
cap.release()
cv2.destroyAllWindows()
