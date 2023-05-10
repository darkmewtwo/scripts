# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int, input().split()))
#     i = 0
#     j = 1 
#     f = 0
#     while j < n:
#         if l[i] > l[j]:
#             f+=1
#             if f > 1:
#                 break
#             l[j], l[i] = l[i], l[j]
#             f = 1
#             i+=1
#             j+=1
#             continue
#         if l[i] == l[j]:
#             j+=1
#             continue
#         i+=1
#         j+=1
#     print('YNEOS'[f-1::2])
        

"""
ALWAYS USE COPY OF LIST WHILE APPENDING RESULT OF DFS INTO A GLOBAL LIST
BECAUSE NEW SCOPES ONLY USE REFERENCE OF LIST `SL` WHICH WHEN APPENDED TO RESULT LIST IS ONLY
APPENDING THE COPY OF THE LIST `SL`
"""

"""PROBLEM FOR  DIVISION OF LIST INTO SUBARRAYS
INPUT: [1,2,3]
OP: [[[1], [2], [3]], [[1], [2, 3]], [[1, 2], [3]], [[1, 2, 3]]]
"""
l = [1,2,3, 4]
n = 4
o = []
p = {}
k = 0
def rec(i, s, sl):
    t = s
    if i == n:
        print('in term condition', sl)
        cpy = sl.copy() # IMPORTANT STEP
        o.append(cpy)
        return
    
    for j in range(i, n):
        t+=1
        sl.append(l[i:j+1])
        f = rec(j+1, s+1, sl)
        sl.pop(-1)
sl = []
rec(0,1, sl)
print(o)
print(p)