import random


responses:dict[str,list[str]] = {
    "who-question":["Your'e mother!", "Yo mama!", "Joe mama!"],
    "what-question":["What about it?"],
    "what-think":["I think that you're the imposter"],
    "negative":["That's good!", "I'm glad to hear it!"],
    "no":["Yes."],
    "unknown":["Tell me more...", "Please, elucidate your thoughts", "Shut up."]
}

def random_slot(arr: list[str]):
    slot = random.randrange(len(arr))
    return arr[slot]

last_in = "supercalifragalisticexpialadocious"
while 1:
    user_in = input().lower()
    if last_in == user_in:
        print("Stop repeating yourself!")
    elif "who" in user_in:
        print(random_slot(responses["who-question"]))
    elif "what do you think" in user_in:
        print(random_slot(responses["what-think"]))
    elif "what" in user_in:
        print(random_slot(responses["what-question"]))
    elif user_in == "no" or user_in == "no." or user_in == "no!" or user_in == "no?":
        print(random_slot(responses["no"]))
    elif "sad" in user_in or "bad" in user_in or "upset" in user_in or "quirked up" in user_in or "nay" in user_in:
        print(random_slot(responses["negative"]))
    elif user_in[-1] == "?":
        print("No.")
    else:
        print(random_slot(responses["unknown"]))
    last_in = user_in