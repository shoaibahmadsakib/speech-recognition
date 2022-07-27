import pyttsx3
from shared import utils
from decouple import config
from shared import constants

USER = config('USER')
BOTNAME = config('BOTNAME')

# initialize speech engine
engine = pyttsx3.init()


def speak(text):
    """ General purpose speak function """
    engine.say(text)
    engine.runAndWait()


def greet_user():
    """ greet user based time of day """
    time_of_day = utils.get_time_of_day()

    if time_of_day == "morning":
        speak('Good morning %s' % (USER))
    elif time_of_day == "afternoon":
        speak('Good morning %s' % (USER))
    elif time_of_day == "evening":
        speak('Good morning %s' % (USER))
    else:
        speak('Good morning %s' % (USER))


def cannot_understand():
    """ Asks the user to repease himself/herself when unknown command issued """
    print('Could not understand you')
    speak(constants.COULD_NOT_UNDERSTAND_TEXT)
