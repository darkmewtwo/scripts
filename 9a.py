

"""
greedy approach for min coins
"""
# def minimumCoins(v: int) -> int:
#     # write your code here
#     coins = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
#     n = 0
#     for i in coins:
#         while v >=i:
#             v-=i
#         print(v)
#     return n

# print(minimumCoins(70))



total = 3
# def rec(total, res, cur, opn, close):
#     print(total, res, cur, opn, close)
#     # if total*2 == len(cur):
#     if total == close == opn:
#         res.append(cur)
#         return
    
#     if opn < total: rec(total, res, cur+'(', opn+1, close)
    
#     else:
#         print('29', opn, close, cur)
#         rec(total, res, cur+')', opn, close+1)

def rec(opn, clse, p):
    print(res, st, opn, clse, p)
    if opn == clse == total:
        res.append("".join(st))
        return
    
    if opn <total:
        st.append('(')
        rec(opn+1, clse, 'OPEN')
        st.pop()
    print('line 44:', res, st, opn, clse, p)
    if clse < opn:
        st.append(')')
        rec(opn, clse+1, 'CLOSE')
        st.pop()


res = []
st = []
# rec(3, res, '', 0, 0)
rec( 0, 0, '')
print(res)

    
    