import pyttsx3

def text_to_speech(text):
    """Convert given text to speech using pyttsx3."""
    try:
        engine = pyttsx3.init()

        # Adjust the speaking rate
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 40)  # Makes speech slightly slower and clearer

        # Choose a voice (depends on your system)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female

        # Speak the text
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("Error in text_to_speech:", e)
