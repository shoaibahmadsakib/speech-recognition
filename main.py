import speech_recognizer
import speech_synthesizer

if __name__ == '__main__':
    query = speech_recognizer.listen()
    speech_synthesizer.speak(query)
