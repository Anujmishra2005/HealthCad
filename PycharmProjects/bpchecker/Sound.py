from playsound import playsound
import keyboard
import threading

# Replace 'path_to_your_sound_file.mp3' with the actual path to your sound file
sound_file_path = 'Emergency.mp3'

# Function to play the sound
def play_sound():
    playsound(sound_file_path)

# Start playing the sound in a separate thread
sound_thread = threading.Thread(target=play_sound)
sound_thread.start()

# Check for the 'S' key press to stop the sound
keyboard.wait('S')

# Stop the sound by joining the thread
sound_thread.join()
