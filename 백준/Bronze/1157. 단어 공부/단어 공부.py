import sys
read = sys.stdin.readline

a = read().rstrip()
a = a.upper()
word = list(a)
nonWord = list(set(word))
mostWord = [0] * len(nonWord)

## 각 문자별 개수를 mostWord 리스트에 저장
for i in range(len(nonWord)):
    mostWord[i] = word.count(nonWord[i])

if mostWord.count(max(mostWord)) > 1:
    print("?")
else:
    print(nonWord[mostWord.index(max(mostWord))]) 