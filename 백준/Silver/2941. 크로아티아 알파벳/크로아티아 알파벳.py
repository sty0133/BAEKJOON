import sys
read = sys.stdin.readline

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croa = read().rstrip()

# for i in range(len(croa)):
#     if len(isCroa) >= 0
#         if croa[i] == "c":
#             if croa[i+1] == "=":
#                 isCroa.append("c=")
#             elif croa[i+1] == "-":
#                 isCroa.append("c-")
#         if croa[i] == "d":
#             if croa[i+1] == "z":
#                 if croa[i+2] == "z":
#                     isCroa.append("dz=")
#             elif croa[i+1] == "-":
#                 isCroa.append("d-")
#         if croa[i] == "l":
#             if croa[i+1] == "j":
#                     isCroa.append("lj")
#         if croa[i] == "n":
#             if croa[i+1] == "j":
#                     isCroa.append("nj")
#         if croa[i] == "s":
#             if croa[i+1] == "=":
#                     isCroa.append("s=")
#         if croa[i] == "z":
#             if croa[i+1] == "=":
#                     isCroa.append("z=")
for i in croatia:
    croa = croa.replace(i, "1")
print(len(croa))