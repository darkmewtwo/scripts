for i in range(int(input())):
    a, b, c = map(int, input().split())
    # l = (a + b + c)//2
    # print("YNEOS"[not l in [a, b, c]::2])
    s=-1
    if a==b:
        # print('in here')
        s=c%2
    elif a==c:
        s=b%2
    elif c==b:
        s=a%2
    else:
        l = (a + b + c)//2
        # print(l, 'in here')
        s=l in [a,b,c] and (a + b + c)%2==0
        # print(s)
        print("YNEOS"[not s::2])
        continue
     
    # print(s)
    print("YNEOS"[s::2])
    