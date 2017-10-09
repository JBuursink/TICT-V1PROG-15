infile = open('pe5_2.txt', 'r')
regels = infile.readlines()
infile.close()

for regel in regels:
    kaartinfo = regel.split(',')
    print('{} heeft kaartnummer: {}' .format(kaartinfo[1].strip(),kaartinfo[0]))