def code(invoerstring):
    tijdelijk=''
    for kar in invoerstring:
        nieuweASCII = ord(kar)+3
        nieuwekar = chr(nieuweASCII)
        tijdelijk += nieuwekar
    return tijdelijk
    
def uncode(invoerstring):
    tijdelijk=''
    for kar in invoerstring:
        nieuweASCII = ord(kar)-3
        nieuwekar = chr(nieuweASCII)
        tijdelijk += nieuwekar
    return tijdelijk
    
type = input('Wil je de code encrypten(e) of decrypten(d):')
inp = input('Voer een woord in:')
if type == 'e':
    print(code(inp))
elif type == 'd':
    print(uncode(inp))
else:
    print('Voer e of d in')
