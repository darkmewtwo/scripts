import sys

class Tree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    """
    slightly wrong implementation"""
    @staticmethod
    def crbst(arr, i, ub):
        # if i == len(arr): return None
        print('*********', arr[i[0]], ub, i)
        if arr[i[0]] > ub: return None
        node = Tree(val=arr[i[0]])
        if i[0]+1 == len(arr): return node
        i[0]+=1
        node.left = Tree.crbst(arr, i, node.val)
        node.right = Tree.crbst(arr, i, ub)
        print(node.val)
        return node
    
    def trav(self, node, ind):
        if node==None:return
        self.trav(node.left, [ind[0]+'l'])
        print(node.val, ind)
        self.trav(node.right, [ind[0]+'R'])

il = [45, 23,21,34,25, 12,5,7,2, 67,47, 50, 62, 70]
il2 = [8,5,1,7, 10,12] ## [8,5,7,1, 10,12] incorrect preorder                                                         
root = Tree.crbst(il2, [0], sys.maxsize)
print(root)
print(root.val, root.left.val, root.right.val)

root.trav(root, ['r'])