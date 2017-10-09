infile = open('pe5_2.txt', 'r')
regels = infile.readlines()
infile.close()
maxNmr = 0
regelNmr = 1

for regel in regels:
    kaartinfo = regel.split(',')
    kaartnummer = int(kaartinfo[0])
    if kaartnummer > maxNmr:
        maxNmr = kaartnummer
        maxRegelNmr = regelNmr
    regelNmr += 1

print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(maxNmr, maxRegelNmr))
