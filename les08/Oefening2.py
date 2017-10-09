set1 = set()
set2 = set()
for i in range(1, 1000):
    if i % 3 == 0:
        set1.add(i)
    elif i % 7 == 0:
        set2.add(i)

print(set1 & set2)