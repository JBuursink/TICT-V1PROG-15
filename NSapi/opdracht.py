import requests
import xmltodict
from tkinter import *

def vertrekTijden():
    button1.pack_forget()
    station.pack_forget()
    auth_details = ('julian-buursink@hotmail.com', 'aTeJTE91dPyeU0lLsZtHR1l4bw5w8qXPKBLlc7un54hbRsmp7E6lDQ')
    beginStation = station.get()
    print(beginStation)
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + beginStation
    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)
    print('Dit zijn de vertrekkende treinen:')
    with open('tekst.txt', 'w') as tekst:
        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming = vertrek['EindBestemming']
            vertrektijd = vertrek['VertrekTijd'] # 2016-09-27T18:36:00+0200
            vertrektijd = vertrektijd[11:16] # 18:36
            treinsoort = vertrek['TreinSoort']
            try:
                routetekst = vertrek['RouteTekst']
            except KeyError:
                routetekst = ''
            try:
                vertrekVertraging = vertrek['VertrekVertragingTekst']
            except KeyError:
                vertrekVertraging = '      '
            print(vertrektijd+' ' + eindbestemming + '\n' + vertrekVertraging + treinsoort + '\n      Via ' + routetekst)
            tekst.write(vertrektijd+' ' + eindbestemming + '\n' + vertrekVertraging + treinsoort + '\n      Via ' + routetekst + '\n')
    printTkinter()

def printTkinter():
    with open('tekst.txt', 'r') as tekst1:
        uitlezen = tekst1.readlines()
        uitlezen1 = ''
        for i in uitlezen:
            if i == '{' or i == '}':
                i = ''
            uitlezen1 += i

    label = Label(root, text=uitlezen1, justify='left')
    label.pack()
    root.mainloop()


root = Tk()
station = Entry(master=root)
station.pack(side=LEFT, pady=10)
button1 = Button(master=root, text='Vertrektijden', command=vertrekTijden)
button1.pack(side=RIGHT, pady=10)
root.mainloop()


