import speech_recognition
import speech_synthesizer
import pywhatkit as kit
import wikipedia
from shared import constants
import subprocess


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
        print("Query is %s" % (query))
        return query
    except Exception:
        return None


def converse():
    """ Decides what action to take based on the input from the user and dispatch to the correct function """
    speech_synthesizer.greet_user()
    while True:
        query = listen()

        if query is not None:
            query = query.lower()

            if 'hello' in query:
                greeting_query()
            elif 'wikipedia' in query:
                wikipedia_query()
            elif 'google' in query:
                google_query()
            elif 'text' in query:
                word_query()
            elif 'song' in query:
                song_query()
            elif 'exit' in query:
                exit_query()
                break
            else:
                speech_synthesizer.cannot_understand()


def greeting_query():
    """ Function to greet the user """
    speech_synthesizer.greet_user()


def wikipedia_query():
    """ Function to search on wikipedia """
    speech_synthesizer.speak('What do you want to search on Wikipedia?')
    search_query = listen()
    if search_query is None:
        speech_synthesizer.cannot_understand()
    else:
        results = wikipedia.search(search_query.lower())
        speech_synthesizer.speak("According to Wikipedia, %s" % (results))
        print(results)


def google_query():
    """ Function to perform search on Google """
    speech_synthesizer.speak('What do you want to search on Google?')
    query = listen()
    if query is None:
        speech_synthesizer.cannot_understand()
    else:
        results = kit.search(query.lower())
        print("Results from Google Search: %s" % (results))


def word_query():
    """ Function to open a text editor """
    speech_synthesizer.speak('Opening text editor please wait...')
    subprocess.call(
        ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Visual Studio Code.app"]
    )


def song_query():
    """ Function to play song as requested by the user ß"""
    speech_synthesizer.speak('What song do you want me to play?')
    query = listen()
    if query is None:
        speech_synthesizer.cannot_understand()
    else:
        kit.playonyt(query)


def exit_query():
    """ Function to exit system when user is done """
    speech_synthesizer.speak('Goodbye, master')
