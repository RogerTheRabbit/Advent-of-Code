import os

input = ""
print("Current directory:", os.getcwd())
with open("./2023/Day 1/input.txt", "r") as f:
  input = f.readlines()

# Part 1

def find(word):
    start, end = -1, -1
    for letter in word:
        if letter.isdigit():
            if start == -1:
                start = letter
                end = letter
            else:
                end = letter
    return int(start+end)


print(sum([find(word) for word in input]))

# Part 2

def find2(word):
    valid = {
        '1':None,
        '2':None,
        '3':None,
        '4':None,
        '5':None,
        '6':None,
        '7':None,
        '8':None,
        '9':None,
        '0':None,
        'one':None,
        'two':None,
        'three':None,
        'four':None,
        'five':None,
        'six':None,
        'seven':None,
        'eight':None,
        'nine':None
    }
    for key in valid.keys():
        valid[key] = (word.find(key), word.rfind(key))

    minIdx = len(word)+1
    minVal = ""
    maxIdx = -1
    maxVal = ""
    for key in valid.keys():
        if(valid[key][0] != -1 and minIdx > valid[key][0]):
            minIdx = valid[key][0]
            minVal = key
        if(valid[key][1] != -1 and maxIdx < valid[key][1]):
            maxIdx = valid[key][1]
            maxVal = key
    
    return int(convert(minVal)+convert(maxVal))
    

def convert(num):
    conversionMap = {
        '0':'0',
        '1':'1',
        '2':'2',
        '3':'3',
        '4':'4',
        '5':'5',
        '6':'6',
        '7':'7',
        '8':'8',
        '9':'9',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    return conversionMap[num]

print(sum([find2(word) for word in input]))