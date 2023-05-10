# l = [23, 34, 17, 78, 24, 792, 45, 67, 2, 68, 25, 34, 89, 48, 90, 91]
l = [1, 2, 3, 4, 3, 5]

# n = len(l)
# i = 0; j = 1
# c =0
# while True:
#     print(c, 'count', l[i], l[j])
#     if l[i] == l[j] and i != j:
#         print(f"duplicate at {l[i]}, {l[j]} pos: {i}, {j}")
#     i=(i+1)%n
#     j=(j+2)%n
#     c+=1

s = f = 0
while True:
    s = l[s]
    f = l[l[f]]
    if s == f:
        break
    
    
print(s, f)

s1 = 0
while True:
    s = l[s]
    s1 = l[s1]
    if s == s1:
        break

print(s, s1)