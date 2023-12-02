import re

#Task 1
def sub(text):
    return re.sub(r'Game\s\d+:\s', '', text)

def gettingfullnums(text):
    text = sub(text)
    green, red, blue = re.findall(r'\d+\sgreen', text), re.findall(r'\d+\sred', text), re.findall(r'\d+\sblue', text)
    return sorted([int(re.sub(r'\sgreen', '', i)) for i in green], reverse=True)[0], sorted([int(re.sub(r'\sred', '', i)) for i in red], reverse=True)[0], sorted([int(re.sub(r'\sblue', '', i)) for i in blue], reverse=True)[0]

input, tmp, mult = open("inputtwo.txt", "r"), 0, 0
for games ,line in enumerate(input):
    green, red, blue = gettingfullnums(line)
    if green <= 13 and red <= 12 and blue <= 14:
        tmp += games + 1
    #Task 2
    mult += green * red * blue

print(tmp)
print(mult)