import simpleaudio as sa
import os

# Function to determine the severity of drowsiness
def determine_drowsiness_severity(ear_value):
    if ear_value < 0.2:
        return 'high'
    elif ear_value < 0.3:
        return 'medium'
    else:
        return 'low'

# Function to play alert sounds based on drowsiness severity
def play_alert_sound(severity):
    script_dir = "D:/codes/Aiml"  # Use the directory path of the current script
    sound_dir = os.path.join(script_dir, 'sounds')  # Create a directory path for the sounds folder
    if severity == 'low':
        # Play a mild alert sound
        sound_file = os.path.join(sound_dir, 'low_alert_sound.wav')  # Replace with the appropriate path to the low alert sound file
        wave_obj = sa.WaveObject.from_wave_file(sound_file)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    elif severity == 'medium':
        # Play a moderate alert sound
        sound_file = os.path.join(sound_dir, 'medium_alert_sound.wav')  # Replace with the appropriate path to the medium alert sound file
        wave_obj = sa.WaveObject.from_wave_file(sound_file)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    elif severity == 'high':
        # Play a high alert sound
        sound_file = os.path.join(sound_dir, 'high_alert_sound.wav')  # Replace with the appropriate path to the high alert sound file
        wave_obj = sa.WaveObject.from_wave_file(sound_file)
        play_obj = wave_obj.play()
        play_obj.wait_done()

# Example usage of the alert system based on drowsiness severity
if __name__ == "__main__":
    ear_value = 0.25  # Example EAR value obtained from drowsiness detection
    severity = determine_drowsiness_severity(ear_value)
    play_alert_sound(severity)
