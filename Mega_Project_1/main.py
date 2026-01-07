import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=2)
                print("Listening...")
                try:
                    audio = recognizer.listen(source)
                except sr.WaitTimeoutError:
                    print("Listening timed out: no speech detected within timeout.")
                    continue

                print("Recognizing...")
                try:
                    command = recognizer.recognize_google(audio)
                    print(command)
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results from recognition service; {e}")
                except Exception as e:
                    print(f"Recognition error: {e}")
        except KeyboardInterrupt:
            print("Exiting...")
            break
