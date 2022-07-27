from datetime import datetime


def get_time_of_day():
    hour = datetime.now().hour

    if (hour >= 6) and (hour < 12):
        return "morning"
    elif (hour >= 12) and (hour < 16):
        return "afternoon"
    elif (hour >= 16) and (hour <= 23):
        return "evening"
    else:
        return "morning"
