import cv2
from scipy.spatial import distance as dist
import numpy as np
import os
import pygame
import dlib
# Initialize the pygame mixer
pygame.mixer.init()

# Calculate the Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    # Convert the eye array to a numpy array for easier manipulation
    eye_array = np.array(eye)
    # Flatten the eye array to a 1-D array
    eye_flat = eye_array.flatten()

    # Calculate the euclidean distance between the two sets of vertical eye landmarks
    A = dist.euclidean(eye_flat[1:3], eye_flat[5:7])
    B = dist.euclidean(eye_flat[2:4], eye_flat[6:8])

    # Calculate the euclidean distance between the horizontal eye landmarks
    C = dist.euclidean(eye_flat[0:2], eye_flat[4:6])

    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    return ear

# Load the pre-trained face detection model and the facial landmark predictor
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Replace the path with the appropriate location of the shape_predictor_68_face_landmarks.dat file
predictor = dlib.shape_predictor(os.path.normpath("D:/codes/Aiml/shape_predictor_68_face_landmarks.dat"))

# Load the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert the captured frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw rectangles around the detected faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Extract the eye regions from the face
        left_eye_region = frame[y:y + h, x:x + w]
        right_eye_region = frame[y:y + h, x + w:x + w + w]

        # Calculate the EAR for each eye
        left_ear = eye_aspect_ratio(left_eye_region)
        right_ear = eye_aspect_ratio(right_eye_region)

        # Compute the average EAR
        ear = (left_ear + right_ear) / 2.0

        # Check for drowsiness and play the appropriate alert sound
        if ear < 0.2:
            pygame.mixer.music.load(os.path.normpath("D:/codes/Aiml/sounds/high_alert_sound.wav"))
            pygame.mixer.music.play()
        elif ear < 0.3:
            pygame.mixer.music.load(os.path.normpath("D:/codes/Aiml/sounds/medium_alert_sound.wav"))
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load(os.path.normpath("D:/codes/Aiml/sounds/low_alert_sound.wav"))
            pygame.mixer.music.play()

    # Display the resulting frame
    cv2.imshow('Drowsiness Detection', frame)

    # Break the loop on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()

# Call the function
#perform_drowsiness_detection()
