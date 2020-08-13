import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word.lower() in data:
        return data[word]

    elif word.upper() in data:
        return data[word.upper()]

    elif word.title() in data:
        return data[word.title()]

    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s Press Y/N:"  % get_close_matches(word, data.keys())[0])

        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]

        elif yn == 'N':
            return "Please check the word again."

        else:
            return "We didn't understand your entry."        
    
    else:
        return "Please check the word again."
    
word = input("Enter a word: ")

meaning = translate(word)

if isinstance(meaning, list):
    for item in meaning:
        print(item)
else:
    print(meaning)