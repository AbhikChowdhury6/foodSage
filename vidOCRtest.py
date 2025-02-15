import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\YourUsername\anaconda3\envs\your_env\Library\bin\tesseract.exe"

# Open the default camera (0 for built-in webcam, change to 1 or other for external cameras)
cap = cv2.VideoCapture(0)

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

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ocr_data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    for i in range(len(ocr_data["text"])):
        if ocr_data["text"][i].strip():  # Ignore empty words
            x, y, w, h = ocr_data["left"][i], ocr_data["top"][i], ocr_data["width"][i], ocr_data["height"][i]
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, ocr_data["text"][i], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # Display the captured frame
    cv2.imshow("Webcam Feed", frame)

    # Press 'q' to quit the video capture
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()