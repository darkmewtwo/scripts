import time

# st= time.time()
# for i in range(int(input())):
#     s = list(input())
#     print('YES') if s.count('A') + s.count('C') == s.count('B') else print('NO')
# print(time.time()  - st)


# st= time.time()
# for s in[*open(0)][1:]:print('YNEOS'[2*s.count('B')!=len(s)-1::2])
# print(time.time()  - st)

# for s in['abababa'][1:]:print('YNEOS'[2*s.count('B')!=len(s)-1::2])


# out = list()
# for i in range(int(input())):
#     n = int(input().strip())
#     # print(bin(n))
#     if n == 1: print(1);continue
#     n1 = bin(n)[3:].replace('0', '1')
#     l1 = 2**(len(n1) - 1)
#     # print(n1)
#     n2 = int(n1, 2)
#     l2 = n - n2
#     # out.append(l1 if l1 > l2 else l2)
#     print(l1) if l1 > l2 else print(l2)

# for i in out:print(i)

# for i in range(int(input())):
#     x = int(input())
#     b = bin(x)[2:]
#     bmax = b.replace('0', '1')
#     mor = b if b==bmax else '0' if b =='0' else bmax[:-1]
#     print(int(mor, 2) +1)


# for i in range(int(input())):
#     n, d = input().split()
#     n =str(int(n))
#     i = n.find(d)
#     # print(type(i))
#     f1 = n
#     f2 = n[:i+1]
#     o=0
#     while(f2.find(d) > -1):
#         f3= int(f2) + 1*10**o
#         f2 = str(f3)
#         o+=1
#     p = '1'* len(f1[i+1:]) if d =='0' else '0' * len(f1[i+1:])

#     # print(0 if i == -1 else int(str(int(f1[:i+1]) + int('1'* len(f1[:i+1]))) + p) - int(n) if (f1[:i+1].find('89')!=-1 and d=='9') else int(str(int(f1[:i+1]) + 1) + p) - int(n))
#     print(0 if i == -1 else int(f2 + p) - int(n))
        


     
# for i in range(int(input())):
#     f = lambda:map(int, input().split())
#     n, d = f();a = list(f()); b = [];mm = mmis = mmax = -1
#     # a.sort()
#     # print(a)
#     for j in range(n):
#         for k in range(j+1, n + 1):
#             print(a[j:k])
            
#             temp = a[j:k]
#             temp.sort()
#             print(temp)
#             if temp[0] - 1 < 0:
#                 for l in range(len(temp) - 1):
#                     print('inside for for temp',temp[l + 1], temp[l])
#                     if temp[l + 1] == temp[l] + 1:
#                         continue
#                     else:
                        
#                         mmis = temp[l] + 1
#                         print(' in mmis', mmis)
#                         b.append(mmis)
#                         break
#                 if mmis == -1:
#                     mmax = temp[-1] + 1
#                     print('mmax', mmax)
#                     b.append(mmax)
#             else:                
#                 mm = 0
#                 print('mm', mm)
#                 b.append(mm)
#     print(b)    
#     b.sort()
#     print(b)
#     print(b[d-1])

# mexl = []
# def asf(i):
#     global mexl
#     mexl[i]=1 
 
# def mex(temp):
    # global mexl
    # mexl = [0]* 100001
    # print(temp)
    # [asf(i) for i in temp]
    # print(b)
    # for i in range(100001):
        # print('in asf', mexl[i], i)
        # if mexl[i]==0:break
    # print('return', i)

def firstmex(j, k, tmex, lint, fint):
    # print(temp)
    # if tmex != -1 and tmex != temp[-1]:
    print('firstmex')
    print(j, k, tmex, lint, fint)
    if j == 0:
        return tmex, lint, fint 
    # if lint < tmex:
    #     print('in if 2')
    #     return lint, a[k], fint
    if fint < tmex:
        print('in if 3')
        return fint, lint, a[j]
    return tmex, lint, fint



import copy
def mex(j, k, tmex, lint, fint):
    # print(temp)
    # if tmex != -1 and tmex != temp[-1]:
    # print('mex')
    # print(j, k, tmex, lint, fint)
    
    if k == n-1 and j == 0:
        return tmex, lint, fint 
    if k != n-1 and lint < tmex and (a[k]+lint)!=0:
        # print('in if 2')
        return lint, a[k], fint
    if k == n-1 and fint < tmex and (a[j]+fint)!=0:
        # print('in if 3')
        return fint, lint, a[j]
    return tmex, lint, fint
        # return tmex, temp[-1]

  
def fmex(temp):
    temp.sort()       
    for i in range(len(temp)-1):
        if temp[i + 1] == temp[i] + 1:continue
        else:return temp[i] + 1
    return temp[-1] + 1
    

for i in range(int(input())):
    f = lambda:map(int, input().split())
    n, d = f();a = list(f()); b = [];mm = mmis = mmax = -1
    sub = n * (n+1)/2
    czero =a.count(0)
    if 0 in a:
        if czero == 1:
            lzeroindex = fzeroindex = zeroindex = a.index(0)
            indexafterzero = n - zeroindex -1
            # indexbeforezero = zeroindex
            subafterzero = (indexafterzero *(indexafterzero +1) )//2
            subbeforezero = (zeroindex *(zeroindex +1) )//2
            b.extend([0] * (subafterzero + subbeforezero))
            # b.append(nmex)
            # print(nmex)
            # print(b)
        else:
            lzeroindex = n - 1
            # print(lzeroindex)
        temp = copy.copy(a)
        nmex = fmex(temp)
        # print(b, nmex)
        for j in range(lzeroindex + 1):
            tmex = lint = fint = -1
            # print(j)
            tmex = nmex
            if czero > 1:
                fzeroindex = j
                
            # fint = a[j - 1] if j - 1 >=0 else a[0]
            # tmex, lint, fint = firstmex(j, 0, tmex, 0, fint)
            # print(tmex, lint, fint)
            # b.append(tmex)
            for k in range(n-1, fzeroindex -1, -1):
                # temp = a[j:k]
                # print('inside for', j, k)
                fint = a[j - 1] if j - 1 >=0 else a[0]
                lint = a[k + 1] if k + 1  < n else a[k]
                # temp.sort()
                # print(a[j:k])
                # print(a[0])
                tmex, lint, fint = mex(j, k, tmex, lint, fint)
                # print(tmex, lint, fint)
                b.append(tmex)
                
        # for j in range(zeroindex + 1):
            
    else:
        print(0)
        continue
    # print(b)
    # print(len(b))
    b.sort()
    # b = list(set(b))
    # print(b)
    print(b[d-1])    
    
    
    # for j in a:
    #     if j !=0:
    #         b.extend([0]*n)
    #     else:
    #         zeroindex = a.index(j)
    #         for k in range(zeroindex, n):
    #             if mmis != -1:
    #                 b.extend([mmis] * (n - k))
    #                 break
    #             if k == zeroindex:
    #                 b.append(1)
    #                 continue
    #             if a[k - 1] == a[k] - 1:
    #                 b.append(a[k] + 1)
    #             else:
    #                 mmis=a[k - 1] +1
    #                 b.append(mmis)                
    #     n-=1
    # print(b)
    # b.sort()
    # print(b)
    # print(b[d-1])
    