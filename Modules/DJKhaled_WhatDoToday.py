# -*- coding: utf-8-*-
import random
import re

WORDS = ["TODAY"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    messages = ["Lets go house shopping.",
                "We gon celebrate.",
                "Wise up, rise up.",
                "Bow down and kneel to greatness."]

    message = random.choice(messages)

    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bdo today\b', text, re.IGNORECASE))