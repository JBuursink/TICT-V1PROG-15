lst = []
lst2 = []
aantal = 1
for i in range(10):
    lst.append(str(input('Wat is woord '+ str(aantal) + '? : ')))
    aantal += 1
for woord in lst:
   if len(woord) == 4:
       lst2.append(woord)

print (lst2)