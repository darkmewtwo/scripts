# s = input()

# def turbo_sort(s):
#     l = [0]*26
#     su = 0
#     for i in range(len(s)):
#         l[ord(s[i])-ord('a')]+=1
#         su+=1

#     o = ''

#     # while(su): 
#     for j in range(su, -1, -1):
#         for i in range(25, -1, -1): 
#             if l[i]>0: 
#                 o +=chr(i+ord('a'))
#                 # su-=1
#                 l[i]-=1 
#     return o      

# test_cases = [
#     ('turbolab', 'utrolbab'),
#     ('haihai', 'ihaiha'),
#     ('hihi', 'ihih'),
#     ('lllll', 'lllll'),
#     ('hiih', 'ihih'),
#     ('hhiiihx', 'xihihih')
# ]
# for sl, test_case in enumerate(test_cases, 1):
#     input_str, output = test_case
#     assert turbo_sort(input_str)==output, f"Test case number {sl}, failed"


# print(o)





def merge(arr, temp, l, m, h):
    print(temp, l, m, h)
    # print(arr)
    i = l
    j = m
    k = l
    # print('merge', i,m ,j, h)
    while((i <=m-1) and (j <=h)):
        # print('in while', i, j, k)
        if(arr[i]<=arr[j]):
            
            temp[k] = arr[i]
            k+=1
            i+=1
        else:
            temp[k] = arr[j]
            k+=1
            j+=1
    # print('outaide 1st while', i, j, k, m, h)
    while(i<=m-1):
        temp[k] = arr[i]
        k+=1
        i+=1
    while(j<=h):
        # print('3rd while', k, j)
        temp[k] = arr[j]
        k+=1
        j+=1
    # print('after merge temp', temp, l, h)
    for i in range(l, h+1):
        arr[i] = temp[i]
            

def mrs(arr, temp,  l, h):
    # print('in mrs', l, h)
    if (h > l):
        # return arr[l]
        m= (l+h)//2
        # print(m)
        """
        below works as args passed by reference
        """
        mrs(arr, temp, l, m)
        mrs(arr, temp,  m+1, h)
        """
        below works as pass by value, changes inside each stack space of the method
        """
        # mrs(arr, [0]*8, l, m)
        # mrs(arr, [0]*8,  m+1, h)
        merge(arr, temp, l, m+1, h)
    return arr
    

# print()

a = mrs([4, 3, 45, 22, 12, 2, 5, 1], [0]*8, 0, 7)
print(a)