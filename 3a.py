'''
    Time Complexity: O(32 * (N + M))
    Space Complexity: O(32 * N)

    where 'N', and 'M' are the size of the given array.
'''

INT_SIZE = 32

# A Trie Node
class TrieNode:

    def __init__(self):
        self.value = None
        self.Child = [None for i in range(2)]

def getNode():    
    newNode = TrieNode()
    newNode.value = 0
    newNode.Child[0], newNode.Child[1] = None, None
    return newNode

def insert(root, key):
    temp = root

    # Start from the most significant bit, and insert all bit of key one-by-one into trie.
    for i in range(INT_SIZE - 1, -1, -1):

        # Find current bit in given prefix
        print('key ', key)
        print('I ', i)
        current_bit = (key & (1 << i))
        print('current bit', current_bit)
        if current_bit > 0 : 
            current_bit = 1

        # Add a new Node into trie
        if (temp.Child[current_bit] == None):
            temp.Child[current_bit] = getNode()

        temp = temp.Child[current_bit]
    
    # Store value of key at leafNode
    temp.value = key 

# Utility function to find maximum XOR value of an integer inserted in Trie and given key.
def findMax(root, key):
    temp = root

    for i in range(INT_SIZE - 1, -1, -1):
        # Find current bit in given prefix
        current_bit = ( key & ( 1 << i) )


        if current_bit > 0 : 
            current_bit = 1


        # Traversal Trie, look for prefix that has opposite bit.
        if(temp.Child[1 - current_bit] != None):
            temp = temp.Child[1 - current_bit]

        # If there is no opposite bit then look for the same bit.
        elif (temp.Child[current_bit] != None):
            temp = temp.Child[current_bit]

    # Return Xor with value at leaf node.
    return key ^ temp.value

def maxXOR(n, m, arr1, arr2):

    # Initialize result.
    maxVal = 0

    # Create a Trie and inssert all elements of first array into trie.
    root = getNode();

    for i in range(n):
        print(root, arr1[i])
        insert(root, arr1[i])

    # For each element in second array find max XOR value from trie.
    for i in range(m):
        
        # Find maximum XOR value of current element with elements inserted in Trie.
        maxVal = max(maxVal, findMax(root, arr2[i]))
    print(maxVal)
    return maxVal

maxXOR(7, 7,
[6, 6, 0, 6, 8, 5, 6],
[1, 7, 1, 7, 8, 0, 2])