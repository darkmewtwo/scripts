from distutils.command.build import build
from distutils.command.build_clib import build_clib
from redis import BusyLoadingError


# l = [34, 1, 23, 12, 321, 8, 10, 19, 132, 198]

# l = [1,2,3,4]
l = [14, 10, 15, 16, 13]
n  = len(l)
tree = [0]*4*n
print(tree)


def buildseg(ind, low, high):
    if  low == high:
        print(low, high, ind)
        tree[ind] = l[low]
        return
    mid = (high + low)//2
    buildseg(2*ind + 1, low, mid)
    buildseg(2*ind + 2, mid + 1, high)
    tree[ind] = tree[2*ind + 1] + tree[2*ind + 2]
    
def getsum(ind, ti, tj, i, j):
    if ti>=i and tj<=j:
        return tree[ind]
    if tj<i or ti > j:
        return 0
    mid = (ti + tj)//2
    left = getsum(2*ind + 1, ti, mid, i, j)
    right = getsum(2*ind + 2, mid + 1, tj, i, j)
    return left + right

buildseg(0,0, n - 1)

print(tree)

print(getsum(0, 0 , n - 1, 1, 3 ))