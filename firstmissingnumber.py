a = [-1, 5, 0, 1]
l = len(a)

for i in range(l):
    if a[i] < 0:
        a[i] = 0
print(a)
for i in range(len(a)):
    val = abs(a[i])
    if 1 <= val <=l:
        if a[val - 1] > 0:
            a[val - 1]*=-1
        if a[val - 1] == 0:
            a[val - 1] = -1 * (l + 1)

print(a)
for i in range(l):
    if a[i] >= 0:
        print(i + 1)
        break
print(i, "after for loop", l+1)
        