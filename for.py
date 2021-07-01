a = [1,1,2,2,3,3]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)