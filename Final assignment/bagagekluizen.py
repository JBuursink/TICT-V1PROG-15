with open('kluizen.txt','r+') as f:
    inlog = [x.strip().split(':') for x in f.readlines()]
    maxkluis = 12
    aantalBezet = 0

    def toon_aantal_kluizen_vrij(inlog,aantalBezet):
        mogelijk = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        for combi in inlog:
            if combi[0] in mogelijk:
                mogelijk.remove(combi[0])
                aantalBezet += 1
        beschikbaar = maxkluis - aantalBezet
        if beschikbaar == 1:
            print(('Er is nog {} kluis beschikbaar.').format(beschikbaar))
        elif beschikbaar > 1:
            print(('Er zijn {} kluizen beschikbaar.').format(beschikbaar))
        else:
            print('Er zijn geen kluizen meer beschikbaar')

    def nieuwe_kluis(inlog):
        mogelijk = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        for i in inlog:
            if i[0] in mogelijk:
                mogelijk.remove(i[0])
        print('De volgende nummers zijn beschikbaar: {}'.format(mogelijk))
        invoerNmr = input('Kies een beschikbaar kluisnummer : ')
        if invoerNmr in mogelijk:
            invoerCode = input('Kies een wachtwoord : ')
            if invoerCode != '' and ':' not in invoerCode:
                f.write(('{}:{}\n').format(invoerNmr,invoerCode))
                print('Kluis {} is succesvol geclaimed.'.format(invoerNmr))
            else:
                print('kannie')
        else:
            print('Dit kluisnummer is niet beschikbaar, probeer een ander')
            nieuwe_kluis(inlog)

    def kluis_openen(inlog):
        kluisGevonden = 0
        invoerNmr = input('Welk kluis nummer: ')
        for kluizen in inlog:
            if invoerNmr == kluizen[0]:
                invoerCode = str(input('Wat is de code van kluis {}: '.format(invoerNmr)))
                kluisGevonden = 1
                if invoerCode == kluizen[1]:
                    print('Kluis {} geopend'.format(invoerNmr))
                else:
                    print('Onjuist wachtwoord.')
        if kluisGevonden == 0:
            print('Voer een geldig kluisnummer in')


    def menu():
        keuze = eval(input('1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen \n4: Ik geef mijn kluis terug\n Maak een keuze: '))
        if keuze == 1:
            toon_aantal_kluizen_vrij(inlog, aantalBezet)
        elif keuze == 2:
            nieuwe_kluis(inlog)
        elif keuze == 3:
            kluis_openen(inlog)
        elif keuze == 4:
            kluis_teruggeven(inlog,aantalBezet)
        else:
            print('waarde is ongeldig')

    def kluis_teruggeven(inlog,aantalBezet):
        print("Nee")

    menu()

