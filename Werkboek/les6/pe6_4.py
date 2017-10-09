studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]
def gemiddelde_per_student(studentencijfers):
    totaal = 0
    lst = []
    for i in studentencijfers:
        for x in i:
            totaal += x
        lst.append(totaal/3)
        totaal = 0
    return lst

def gemiddelde_van_alle_studenten(studentencijfers):
    totaal = 0
    for i in studentencijfers:
        for x in i:
            totaal += x
    return totaal

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))