import random

imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']

ocjene={}
for ime in imena:
    ocjene[ime] = random.randint(1, 5)

jedinice = 0
dvice = 0
trice = 0
cetvrtice = 0
petice = 0

for v in ocjene.values():
    if v == 1:
        jedinice += 1
    elif v == 2:
        dvice += 1
    elif v == 3:
        trice += 1
    elif v == 4:
        cetvrtice += 1
    elif v == 5:
        petice += 1
ukupno = jedinice+dvice+trice+cetvrtice+petice

duljina = len(imena)
postotak = (ukupno/duljina)*100


print("pet: ", petice)
print("cetiri: ", cetvrtice) 
print("tri: ", trice) 
print("Dva: ", dvice) 
print("Jedan: ", jedinice)

print(postotak)
