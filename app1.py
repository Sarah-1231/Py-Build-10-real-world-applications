import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        Y_or_N=input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word,data.keys())[0])
        if Y_or_N=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif Y_or_N=="N":
            return "The word does not exist. Please double check it."
        else:
            return "We did not understand your entry."

    else:
        return "The word doesn't exist. Please double check it."
word=input("Enter word: ")
print(translate(word))