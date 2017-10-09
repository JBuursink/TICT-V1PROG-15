def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        for c in newpassword:
            if c in '0123456789':
                return True
    else:
        return False

oud = input('Wat is je oude wachtwoord? ')
nieuw = input('Wat wordt je nieuwe wachtwoord? ')

res = new_password(oud, nieuw)
if res == True:
    print('Je nieuwe wachtwoord is ' + nieuw + '.')

else:
    if len(nieuw) < 6:
        print('Het wachtwoord moet minimaal 6 tekens bevatten.')
    else:
        if oud == nieuw:
            print('Het wachtwoord moet anders zijn dan het huidige wachtwoord.')
        else:
            print('Het wachtwoord moet een cijfer bevatten.')