class SNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

l = [34, 1, 23, 12, 321, 8, 10, 19, 132, 198]
head = SNode(val=l[0])
temp = head
for i in l[1:]:
    temp.next = SNode(val=i)
    temp = temp.next

# t = head
# while t:
#     print(t.val)
#     t = t.next


def getv(node, head):
    global res
    # print('here', node)
    if node:
        first = getv(node.next, head)
        if not first:
            return None
        end = node.val
        beg = first.val
        print(beg, end)
        res = max(res, end+beg)
        if first.next.val == node.val:
            return
        return first.next
    
    return head
res = 0
getv(head, head)
print(res)