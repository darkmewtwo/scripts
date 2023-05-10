s = "acire"
s1 = "cbe"
res = r = ""
dp = [[-1 for i in range(len(s1))] for j in range(len(s))]
print(dp)
def rec(i, j, res, dp):
    global r
    print(i, j, s[i], s1[j])
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i] == s1[j]:
        r=s[i]+ r
        dp[i][j] = 1 + rec(i-1, j - 1, res, dp)
        return dp[i][j]
    dp[i][j] = max(rec(i, j-1, res, dp), rec(i-1, j, res, dp))
    return dp[i][j]
        

# def lsubs(s, s1):
print(rec(4, 2, res, dp))
print(dp)
print(r)