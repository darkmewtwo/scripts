# n, a = map(int, input().split())
# l = list(map(int, input().split()))
# print(sum([0<v>=l[a-1] for v in l]))

# for t in range(int(input())):
#     rd = dict(zip(input().split(), [1, 2, 3]))
#     x, y = input().split()
#     print(x if rd[x] < rd[y] else y)
    
# import math
# r = -1
# a = []
# b = []
# p = -1
# def rank(e):
#     global r,b, p
    
#     t=int(e)
#     if r == -1 and t in b:r=2;p = t
#     b.append(t)
#     return t

# for t in range(int(input())):
#     p = -1
#     r = -1
#     b = []
#     a = []

#     n = int(input())
    
#     a = list(map(rank, input().split()))
#     if sum(a)==n or n ==1:print(0);continue
#     # if a[0] in a[1:]:print(2);continue
#     # if a[-1] in a[:-1]:print(2);continue
#     # if a[0] !=p and a[-1]!=p and r ==2:print(3);continue
#     if a[0] == a[-1]: print(math.factorial((n-2)));continue
#     if r ==2:print((n-1)*math.factorial((n-2)));continue 
#     print(-1)


# for i in range(int(input())):
#     n,m = map(int, input().split())
#     if n == m:
#         print((n+1)*2);print("01"*(n+1))
#     if n > m:
#         print((n*2)+1);print("01"*m+"010"*(n-m))
#     if m > n:
#         print((m*2)+1);print("10"*n+"110"*(m-n-1)+"1")
        

# import sys
# input = sys.stdin.readline

# for i in range(int(input())):
#     fun=lambda:map(int,input().split())
    
#     kx, ky = fun()
#     x1, y1 = fun()
#     x2, y2 = fun()
#     ly1 = abs(ky - y1)
#     ly2 = abs(ky - y2)
#     lx1 = abs(kx - x1)
#     lx2 = abs(kx - x2)
#     if (kx==8 and 7 in [x1, x2] and y1!=y2 and 1 not in [ly1, ly2]) or (kx==1 and 2 in [x1, x2] and y1!=y2 and 1 not in [ly1, ly2]) or \
#         (ky==1 and 2 in [y1, y2] and x1!=x2 and 1 not in [lx1, lx2]) or (ky==8 and 7 in [y1, y2] and x1!=x2 and 1 not in [lx1, lx2]) :
#         print("YES")
#     else:
#         print("NO")

# import sys
# input = sys.stdin.readline

# def move(moves):
#     movempr = {'SR': 'R',
#                'SP': 'S',
#                'RP': 'P',
#                'RS': 'R',
#                'PS': 'S',
#                'PR': 'P',
#                'SS': 'S',
#                'RR': 'R',
#                'PP': 'P',
#                }
#     return movempr[moves]

# for i in range(int(input())):
#     # fun=lambda:map(int,input().split())
#     n = int(input())
#     a = list(input())
#     o=""
#     for k in range(n):
#         fm = a[k]
#         for j in range(k, n):
#             mw=move(f"{fm+a[j]}")
#             fm=mw
#         o+=mw
#     print(o)
        
# import sys

# sys.stdout.       

who_beats = {'R': 'P', 'P': 'S', 'S': 'R'}

for _ in range(int(input())):
    n = int(input())
    s = input()
    ind = {'R': -1, 'P': -1, 'S': -1}
    ans = ['?'] * n
    for i in reversed(range(n)):
        indwb = ind[who_beats[s[i]]]
        print(s[i])
        print(indwb)
        ans[i] = s[i] if indwb == -1 else ans[indwb]
        print(ans[i])
        ind[s[i]] = i
        print(ind)
    print(''.join(ans))