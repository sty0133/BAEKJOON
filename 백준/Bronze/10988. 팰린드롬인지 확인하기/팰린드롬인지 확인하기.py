import sys
read = sys.stdin.readline

pelin = list(read().rstrip())
pelin_reverse = list(reversed(pelin))
blankList = [0] * len(pelin)

for r in range(len(pelin)):
    if pelin[r] == pelin_reverse[r]:
        blankList[r] = 0
        # print(pelin[r] ,"=", pelin_reverse[r] )
    else:
        blankList[r] = 1
# print(blankList)
if blankList.count(0) == len(pelin):
    print("1")
else:
    print("0")