import sys
read = sys.stdin.readline

n = int(read().rstrip())
wordList = []

for i in range(n):
    wordList.append(read().rstrip())
set_wordList = set(wordList)
wordList = list(set_wordList)
wordList.sort()
wordList.sort(key = len)

for i in wordList:
    print(i)