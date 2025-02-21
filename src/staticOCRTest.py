import cv2
import easyocr
import time

reader = easyocr.Reader(['en'])

location = "RealWorldTestPhotos\RealWorldTestPhotos\RealWorldTestPhoto_1.webp"

frame = cv2.imread(location)

results = reader.readtext(frame)

for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))

    # Draw bounding box
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

    # Display recognized text
    cv2.putText(frame, text, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

# Show the frame
cv2.imshow("Webcam OCR", frame)
time.sleep(100)
if cv2.waitKey(1) & 0xFF == ord('q'):
        pass

cv2.destroyAllWindows()