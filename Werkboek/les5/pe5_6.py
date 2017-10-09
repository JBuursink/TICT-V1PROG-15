infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
infile.close()

outfile = open('kaartnummersuit.txt', 'w')

for regel in regels:
    kaartinfo = regel.split(',')
    outfile.write('{} heeft kaartnummer: {}\n' .format(kaartinfo[1].strip(),kaartinfo[0]))

outfile.close()