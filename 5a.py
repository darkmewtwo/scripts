
class pair:
    def __init__(self, v, w):
        self.v = v
        self.w = w
        
        


v,e = map(int, input().split())
print(v,e)
adjl = {i: [] for i in range(v+1)}
adjlw = {i: [] for i in range(v+1)}
print(adjl)
for i in range(e):
    e1, e2, w = map(int, input().split())
    t = []
    adjl[e1].append(e2)
    adjl[e2].append(e1)
    adjlw[e1].append(pair(e2,w))
    adjlw[e2].append(pair(e1,w))
    
print(adjl)