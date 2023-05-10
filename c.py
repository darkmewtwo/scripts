
from f import g
class F:
    def op(self, g):
        print('op', g)
        return g



class S(F):
    def __init__(self, x, y):
        self.x, self.y=x,y
        
    def __call__(self):
        # return self.x*self.y
        return self
    
    def __repr__(self):
        return f"{self.x*self.y}"
    
    # def __str__(self):
    #     return f"hi there"
    
    def ad(self):
        print('inside ad')
        return self.x *2
    
    def cal(self):
        print('inside cal')
        return self.op(self.ad())
    
    def crossmod(self):
        print(__name__, 'crossmod')
        return g(self.cal)

 

s=S(3,4)
print(s, dir(s), s(), S)
s()

f=F()
print(f, dir(f), F)
# print(f.op())
print(s.cal())
print(s.crossmod())