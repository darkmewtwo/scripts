



l = [3,4,2, 89, 23, 45, 57, 34]

class Tree:
    def __init__(self, value=None):
        self.left = None
        self.right = None     
        self.value = value
    
    def insert(self, value):
        
        newNode = Tree(value)
        if self.left == None:
            self.left = newNode
            # return self.left
            self.right = Tree()
        else:
            self.right = newNode
            self.left = Tree()
            # return self.right
    
    def printTree(self, slc):
        # if not self.right or not self.left:
        #     return
        # self
        
        lv = False
        wi = 6
        q = [[self, lv, wi, 'root', 0]]
        while(len(q) > 0):
            t = q.pop(0)
            node = t[0]
            lv = t[1]
            wi = t[2]
            m = t[3]
            tl = t[4]
            # print(node.value, tl)
            
            print(" "*wi,node.value, end=" ") if lv else print(" "*wi,node.value, " ")
            if node.left:
                # print(node.left.value, tl)
                if not node.left.left and not node.left.right:
                    slc+=node.left.value
                q.append([node.left, True, wi -1, 'left', tl+1])
            if node.right:
                # print(node.value, tl)
                q.append([node.right, False, 1, 'right', tl+1])
        return slc
        # print(self, q[0].left.value)
         
    def treedfsheight(self, node, x=None):
        if node == None: return -1
        if x and x == node.value: print('x equals');return -1
        lh = self.treedfsheight(node.left) + 1
        rh = self.treedfsheight(node.right) + 1
        print(lh, rh, node.value)
        # return 1 + max(lh, rh)
        return max(lh, rh)

    def findDepth(self, root, x):
    
        # Base case
        if (root == None):
            return -1
    
        # Initialize distance as -1
        dist = -1
    
        # Check if x is current node=
        if (root.value == x):
            print(dist, 'value equals')
            return dist + 1
        print(dist, root.value)
        dist = self.findDepth(root.left, x)
        print(dist, root.value, 'after left callback')
        if dist >= 0:
            return dist + 1
        dist = self.findDepth(root.right, x)
        print(dist, root.value, 'after right callback')
        
        if dist >= 0:
            return dist + 1
        return dist

    def dfsrightview(self, node, lvl, arr):
        if node == None: return
        if len(arr) == lvl: arr.append(node.value)
        self.dfsrightview(node.right, lvl+1, arr)
        self.dfsrightview(node.left, lvl+1, arr)
        
    def dfsroototnodepath(self, node, value, arr):
        if not node: return False
        arr.append(node.value)
        if node.value == value:return True
        if self.dfsroototnodepath(node.left, value, arr) or \
           self.dfsroototnodepath(node.right, value, arr): return True
        
        arr.pop()
        return False
        
root = Tree(value=l[0])
ll = len(l) - 1
i = 1
# temp = root
q = [root]
while i <=ll:
    temp = q.pop(0)
    lnode = Tree(value=l[i])
    temp.left = lnode
    q.append(lnode)
    if i + 1 <=ll:
        rnode = Tree(value=l[i+1])
        temp.right = rnode
        q.append(rnode)
    i+=2
    
    


# temp = root
f = root.printTree(0)
print('\n', f)

k = root.treedfsheight(root, 4)
print(k)

# g = root.findDepth(root, 89)
# print(g)

arr = []
l = root.dfsrightview(root, 0, arr)
print(l, arr)

arr = []
l = root.dfsroototnodepath(root, 23, arr)
print(arr)
