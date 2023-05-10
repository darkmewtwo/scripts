def generate(total, opn, close, s, ans):
    if len(s) == total:
        ans.append(s)
        return
    print(s, opn, close)
    if opn > close:
        generate(total, opn, close + 1, s+')', ans)

        if opn < total//2:
            generate(total, opn+1, close, s+'(', ans)   
    else:
        generate(total, opn+1, close, s+'(', ans)
        
def validParenthesis(n):
    
    # List of string to store all the valid parentheses.
    ans = []
    
    # Total number of characters.
    total = 2*n
    
    '''
            Calling the generating function to generate all the 
            valid parentheses. Count of opening bracket and closing
            bracket will be zero and the string will be an empty string.
    '''
    generate(total, 0, 0, "", ans)
    
    return ans


print(validParenthesis(3))    
    