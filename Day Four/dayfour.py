import re

#part1
def delete_card_str(text):
    return re.sub(r"Card\s+\d+:\s+", "", text)

def delimit_str(text):
    text = text.replace("  ", " ")
    splitting = text.split("|")
    splitting[1] = splitting[1].replace("\n", "")
    won, card = splitting[0].split(" "), splitting[1].split(" ")
    won.pop(), card.pop(0)
    return won, card

def won_in_card(won, card):
    count = 0
    wincard = [elem for elem in won if elem in card]
    if len(wincard):
        return 2**(len(wincard)-1) 
    else:
        return 0

#part2
def copies(won,card, num):
    wincard = [elem for elem in won if elem in card]
    if total[num]:
        for i in range(total[num]):
            for j in range(num, num+len(wincard)):
                total[j+1]+=1

input, tmp = open("input.txt", "r"), 0
total = [1 for i in range(len(open("input.txt", "r").readlines()))]
for num, line in enumerate(input):

    bet = delimit_str(delete_card_str(line))
    tmp += won_in_card(bet[0], bet[1])
    copies(bet[0], bet[1], num)

print(sum(total))
print(tmp)