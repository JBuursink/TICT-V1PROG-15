try:
    numlist = [100,101,0,'103',104]
    index = int(input('geef een index; '))
    print(100/numlist[index])
except ValueError:
    print('sdaoklsjd')
except IndexError:
    print('sdaslda')
except TypeError:
    print('sdjaklsd')