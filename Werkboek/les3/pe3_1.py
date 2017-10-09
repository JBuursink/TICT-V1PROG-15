score = eval(input('Geef je score: '))
geslaagd = False

if score > 15:
    geslaagd = True

if geslaagd == True:
    print('Met een score van ' + str(score) + ' ben je geslaagd!')
else:
    print('Met een score van ' + str(score) + ' ben je helaas gezakt.')