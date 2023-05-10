
# Python3 program to answer
# subsequence queries for
# a given string.
MAX = 10000
CHAR_SIZE = 26

# Precompute the position of
# each character from
# each position of String S
def precompute(mat, str, Len):
    print(Len)
    for i in range(CHAR_SIZE):
        mat[Len][i] = Len
	
    print(mat)
    for i in range(Len - 1, -1, -1):
        for j in range(CHAR_SIZE):
            mat[i][j] = mat[i + 1][j]
        mat[i][ord(str[i]) -
			ord('a')] = i

# Print "Yes" if T is
# subsequence of S, else "No"
def query(mat, str, Len):
	pos = 0

	# Traversing the string T
	for i in range(len(str)):

		# If next position is greater than
		# length of S set flag to false.
		if(mat[pos][ord(str[i]) -
					ord('a')] >= Len):
			return False

		# Setting position of next character
		else:
			pos = mat[pos][ord(str[i]) -
						ord('a')] + 1
	return True

# Driven code
S = "geeksforgeeks"
Len = len(S)
mat = [[0 for i in range(CHAR_SIZE)]
		for j in range(MAX)]
precompute(mat, S, Len)

get = "No"
if(query(mat, "gg", Len)):
	get = "Yes"
print(get)

get = "No"
if(query(mat, "gro", Len)):
	get = "Yes"
print(get)

get = "No"
if(query(mat, "gfg", Len)):
	get = "Yes"
print(get)

get = "No"
if(query(mat, "orf", Len)):
	get = "Yes"
print(get)

# This code is contributed by avanitrachhadiya2155
