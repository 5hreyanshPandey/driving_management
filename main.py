# main_program.py

from facial_recognition import perform_facial_recognition
from drowsiness_detection import perform_drowsiness_detection
from alert_system import perform_alert_system
from data_analysis import perform_data_analysis
from tensorflow_image_classification import perform_image_classification

def main():
    try:
        print("Running facial recognition...")
        perform_facial_recognition()
    except Exception as e:
        print(f"Error occurred during facial recognition: {e}")

    try:
        print("Running drowsiness detection...")
        perform_drowsiness_detection()
    except Exception as e:
        print(f"Error occurred during drowsiness detection: {e}")

    try:
        print("Performing alert system...")
        perform_alert_system()
    except Exception as e:
        print(f"Error occurred during alert system: {e}")

    try:
        print("Performing data analysis...")
        perform_data_analysis()
    except Exception as e:
        print(f"Error occurred during data analysis: {e}")


if __name__ == '__main__':
    main()
