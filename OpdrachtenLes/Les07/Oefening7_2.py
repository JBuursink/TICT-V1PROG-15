week = {'ma': 'maandag', 'di': 'dinsdag', 'wo': 'woensdag', 'do': 'donderdag', 'vr': 'vrijdag'}
week['za'] = 'zaterdag'
for afkorting in week.keys():
    print('Afkorting: {}, lange naam: {}'.format(afkorting, week[afkorting]))