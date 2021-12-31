import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    a = w.lower()
    m = get_close_matches(a, data.keys())
    if a in data:
        return data[a]
    elif a.title() in data:
        return data[a.title()]
    elif a.upper() in data:
        return data[a.upper()]
    elif len(m)>0:
        Yn = input("Do you want to find %s ? Enter Y if Yes,or N if Not:" % m[0])
        if Yn == "Y":
            return data[m[0]]
        elif Yn == "N":
            return("Your word is not exit, please doulble check!")
        else:
            return("I cannot understand you.")
    else:
        return("Your word is not exit, please doulble check!")

word = input("Enter a Word:")

output = translate(word)

if type(output) == list:
    for item in output:
        print ("*.%s"%item)
else:
    print(output)
