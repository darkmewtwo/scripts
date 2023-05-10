
def pwset(arr):

    n = len(arr)

    # Create an array to store all subsets
    ans = [[]]

    # Traverse through the array ARR
    for i in range(n):

        element = arr[i]
        length = len(ans)

        # Traverse through the array ans from 0 to length index
        for j in range(length):

            temp = ans[j].copy()

            # Include element in the subset temp
            temp.append(element)
            ans.append(temp)

    # Return the array ans
    return ans

arr = [1,2,3]
f = pwset(arr)
print(f)

