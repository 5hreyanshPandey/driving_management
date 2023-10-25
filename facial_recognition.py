import cv2

def perform_facial_recognition():
    try:
        # Define the camera index for the Camo virtual camera feed
        camera_index = 0  # Modify this index value accordingly

        # Initialize the video capture
        cap = cv2.VideoCapture(camera_index)

        # Check if the camera is opened successfully
        if not cap.isOpened():
            print("Error: Could not open camera.")
        else:
            while True:
                ret, frame = cap.read()

                # Check if the frame is read correctly
                if not ret:
                    print("Error: Failed to capture frame.")
                    break

                # Convert the frame to grayscale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Display the resulting frame
                cv2.imshow('Frame', gray)

                # Break the loop on key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Release the video capture and close all windows
            cap.release()
            cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error occurred during facial recognition: {e}")

if __name__ == '__main__':
    perform_facial_recognition()
