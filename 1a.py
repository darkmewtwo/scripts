'''

    Time Complexity : O(2^N)
    Space Complexity : O(N)

    Where N is the number of elements in the array.

'''

def helper(arr, n, k, curr):
    print('in helper', arr, n, k, curr )
    
    # Base condition.
    if n <= 0:
        print(n, 'in if')
        
        # If k = curr, we reached target OR.
        if k == curr:
            return 0
        
        else:
            # We return infinity.
            return 1000000000
        
    # arr[n-1] not taken in considertion. 
    x = helper(arr, n - 1, k, curr)
    print('after helper', x, arr, n - 1, k , curr , arr[n - 1])
    # arr[n - 1] is taken into considereation.
    y = 1 + helper(arr, n - 1, k , curr | arr[n - 1])
    
    # Return current result.
    return min(x, y)

def subsetOR(a):
    
    n = len(a)
    k = 0
    
    # Calculate maximum OR.
    for i in range(n):
        
        k |= a[i]
        
    ans = helper(a, n, k, 0)
    
    return ans


print(subsetOR([5, 1, 3, 4, 2]))