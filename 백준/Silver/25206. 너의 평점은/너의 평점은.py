import sys
read = sys.stdin.readline

# score = []
# grade = []
# gradeTranse = []

# for i in range(20):
#     name , what_score , what_grade = read().rstrip().split()
#     score.append(what_score)
#     grade.append(what_grade)

# # print(score,grade)
# for i in grade:
#     data = i.replace("A+",4.5)
#     gradeTranse.append(data)

rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
total = 0
result = 0

for _ in range(20):
    name , a , b = read().rstrip().split()
    a = float(a)
    if b != "P":
        total += a
        result += a * grade[rating.index(b)]

print("%.6f" % (result / total))
# score = {'A+': 4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F': 0.0}
# # 학점 * 과목 평점의 합
# total = 0
# # 학점 총합
# s = 0

# for _ in range(20):
#     subject, x, y = map(str, read().rstrip().split())
#     x = float(x)
#     s += x
#     if y != 'P':
#         total += (x * float(score[y]))

# print(total/s)