import pyttsx3
from shared import utils
from decouple import config

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
        speak(f"Good morning {USER}")
    elif time_of_day == "afternoon":
        speak(f"Good afternoon {USER}")
    elif time_of_day == "evening":
        speak(f"Good evening {USER}")
    else:
        speak(f"Greetings {USER}")


if __name__ == "__main__":
    greet_user()
