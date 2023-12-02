import re

#Task 1
def numfind(text : str) -> int:
    num = re.findall(r'\d+',text)
    return int(str(num[0])[0] + str(num[-1])[-1])

digitsword = ['one','two','three','four','five','six','seven','eight','nine']
#Task 2

def replacement(text):
    tmp = ""
    for i in range(0, len(text)):
        if text[i].isdigit():
            tmp += str(text[i])
        if i + 3 < len(text) and text[i: i + 3] in digitsword:
                tmp += str(digitsword.index(text[i:i+3])+1)
        if i + 4 < len(text) and text[i: i + 4] in digitsword:
                tmp += str(digitsword.index(text[i:i+4])+1)
        if i + 5 < len(text) and text[i: i + 5] in digitsword:
                tmp += str(digitsword.index(text[i:i+5])+1)
    return tmp

def numfind2(text):
    text = replacement(text)
    return int(str(text[0])[0] + str(text[-1])[-1])

    
input, tmp = open("inputone.txt", "r"), 0
for line in input:
    tmp += numfind2(line)

print(tmp)