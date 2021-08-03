import json

from config import *

def add(name, score, filename = HIGHSCOREFILE):
    try:
        with open(filename) as file:
            highscores = json.load(file)
    except Exception as e:
        highscores = {}
    highscores[name] = score
    highscores = dict(sorted(highscores.items(), key = lambda x: x[1], reverse = True))
    with open(filename, 'w+') as file:
        json.dump(highscores, file)

def get(filename = HIGHSCOREFILE):
        try:
            with open(filename,'r') as file:
                highscores = json.load(file)
                return dict(sorted(highscores.items(), key = lambda x: x[1], reverse = True))
        except Exception as e:
            with open(filename,'w') as file:
                json.dump({}, file)
            return {}

if __name__ == '__main__':
    pass