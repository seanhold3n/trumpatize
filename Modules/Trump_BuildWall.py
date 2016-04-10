# -*- coding: utf-8-*-
import random
import re

WORDS = ["WALL", "BUILD"]


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
    messages = ["I will have mexico pay for that wall.",
                "I would build a great great wall.",
                "I would build a great wall. Nobody builds walls better than me."]

    message = random.choice(messages)

    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bbuild wall\b', text, re.IGNORECASE))