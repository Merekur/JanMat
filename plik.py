# pamiec = []
#
# def sumaLicz(A, T):
#     n = len(A)
#
#     for i in range(0, n):
#         temp = []
#         for j in range(0, T + 1):
#             temp.append(0)
#         pamiec.append(temp)
#     pamiec[0][0] = 1
#     if A[0]<T+1:
#         pamiec[0][A[0]] = 1
#
#
#
#     for i in range(1, n):
#
#         for j in range(0, T + 1):
#             temp = 0
#             if j - A[i] > -1:
#                 temp = pamiec[i-1][j - A[i]]
#             if temp == 1 or pamiec[i - 1][j] == 1:
#                 pamiec[i][j] = 1
#             else:
#                 pamiec[i][j] = 0
#     return pamiec[n-1][T]
#
#
# a = [3,5,7]
# print(sumaLicz(a, ))
print(1,)
for b in range(100):
    print(100)
    for a in range(100):
        print(a,end = " ")