# Example for Face Tracking
import cv2
import numpy as np

cap = cv2.VideoCapture(1)

# Classifier function
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    # This line captures the video frame from the object 'CAP'
    ret, frame = cap.read()

    # Convert frame into grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces using the classifier
    faces_in_frame = face_cascade.detectMultiScale(gray_frame, 1.1, 4)

    # Draw rectangle around each face_cascade

    for (x, y, w, h) in faces_in_frame:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == 27: # Escape key
        break
cap.release
cv2.destroyAllWindows()
