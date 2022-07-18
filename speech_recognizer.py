import speech_recognition as speech_recognition
import speech_recognizer
from shared import constants


def listen():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
    except Exception:
        speech_recognizer.speak(constants.COULD_NOT_UNDERSTAND_TEXT)
        query = 'None'
    return query
