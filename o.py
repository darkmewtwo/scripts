# out = 0
# n, a = map(int, input().split())
# l = list(map(int, input().split()))
# for i in range(a - 1, n):

#     if l[i] == l[a - 1]:
#         pass
#     else:
#         out = i + 1
#         break
# print(out)

# i=lambda:map(int,input().split())
# n,k=i();l=list(i())
# print(type(i))

# for i in range(int(input())):
#     m,n,k = map(int, input().split())
#     print('YES') if n*k < m else print('NO')

#     s='abababab'
# print('YNEOS'[2*s.count('B')!=len(s)-1::2])

# s=[*open(0)][1:]
# print(type(s))
# print(s)
# print('YNEOS'[1::2])
# print('1' if a+b+c<=d else '2' if any([a+b<=d, a+c<=d, b+c<=d]) else '3')


from f import g


# c = 0
# flag = True
# def fun(e):
#     global c, flag
#     # print(e)
#     # print(c, flag)
#     # e = int(e)
#     if e%2!=0:
#         if flag==False:
#             c+=1
#             flag=True
#         else:flag=False
# c = 0
# def fun(e):
#     global c
#     # print(e)
#     # print(c, flag)
#     e = int(e)
#     if e%2!=0:
#         # if flag==False:
#         c+=1
#         #     flag=True
#         # else:flag=False

# for i in range(int(input())):
#     n =int(input())
#     c = 0
#     # l = list(map( fun, input().split()))
#     l = list(map( lambda x: c+int(x)%2, input().split()))
#     # print(l)
#     print(c)
#     print(c//2)


def f(i, j, a):
    return len(set(a[i:j]))


# def main():


def x(): return map(int, input().split())


n, nq = x()
a = list(x())
for _ in range(nq):
    t, *q = map(int, x())
    if t == 1:
        a[q[0] - 1] = q[1]
        continue
    if t == 2:
        salldist = 0
        n = q[0]
        salldist = q[0] * (q[0]+1)
        mdict = {}
        for i in range(q[0]):
            if mdict.get(a[i]):
                salldist -= q[0] - i
            else:
                mdict[a[i]] = 1
        print(salldist)
        continue

        # mdict[a[i]] = mdict.get(a[i]) + 1
        # for i in range(q[0]):
        #     if mdict[i] > 1:
        #         salldist-=mdict[i]
        # sum = 0
        # for i in range(0, q[0]):
        #     for j in range(i, q[0]):
        #         # print('sum indi')
        #         # print(f(i, j+1, a))
        #         sum += f(i, j + 1, a)
        print(sum)
        # continue
