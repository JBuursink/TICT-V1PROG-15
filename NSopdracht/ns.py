def standaardprijs(afstandKM):
    if afstandKM >= 50:
        prijs = 15 + ((afstandKM - 50) * 0.60)
    else:
        prijs = afstandKM * 0.80
    return prijs

def nieuwePrijs(leeftijd,weekendRit,afstandKM):
    oud = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 64:
        if weekendRit == True:
            nieuwePrijs = oud * 0.65
        else:
            nieuwePrijs = oud * 0.70
    else:
        if weekendRit == True:
            nieuwePrijs = oud * 0.60
        else:
            nieuwePrijs = oud

    return nieuwePrijs

afstandKM = (eval(input('Wat is de afstand (in KM) : ')))
leeftijd = (eval(input('Wat is je leeftijd : ')))
weekendRit = (eval(input('Is het weekend (True/False) : ')))

print ('De reiskosten voor een afstand van {}km zijn €{} euro.' .format(afstandKM,nieuwePrijs(leeftijd,weekendRit,afstandKM)))
